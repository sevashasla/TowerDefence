from .road import Road
from .castle import Castle
from random import randint
from .spawn_point import SpawnPoint
import time
import json
from numpy import sign

from ..Game.coordinates import Coordinates
from ..Tower.tower_factories import *
from ..Game.pocket import Pocket
from ..Game.errors import *

class Field:

	def __init__(self, data):
		self.width = data["shape"]["width"]
		self.height = data["shape"]["height"]
		
		self.road = Road(self.width, self.height, data["road"])
		self.castle = Castle(data["castle"])
		self.spawn_point = SpawnPoint(data["spawn_point"], data["waves"])
		Pocket.add_money(data["pocket"]["init_money"])

		self.units = []
		self.towers = []		
		self.attacks_by_units = []
		self.attacks_by_towers = []

		self.all_waves_spawned = False
		self.update_rate = 0.1
		self.last_update = 0.0
		self.min_step = data["movement_constants"]["min_step"]
		self.max_step = data["movement_constants"]["max_step"]
		self.big_step = data["movement_constants"]["big_step"]

		self.towers_placed = 0



	def can_make_step(self, unit, distance) -> bool:
		try:    
			new_coords_x = unit.coordinates.x + distance * sign(unit.speed[0])
			new_coords_y = unit.coordinates.y + distance * sign(unit.speed[1])
			new_coords = Coordinates(new_coords_x, new_coords_y)
			if self.castle.belongs_to_castle(new_coords):
				unit.speed = [0, 0]
				return False
			if self.road.belongs_to_road(new_coords):
				return True
		except IndexError:
			new_coords_x = unit.coordinates.x + distance * sign(unit.speed[0])
			new_coords_y = unit.coordinates.y + distance * sign(unit.speed[1])
			return False
		return False


	def can_place_tower(self, coords) -> bool:
		try:
			if not self.road.belongs_to_road(coords) and \
			   not self.castle.belongs_to_castle(coords) and \
			   self.belong_to_field(coords):
				return True
		except IndexError:
			return False

		return False


	def place_tower(self, tower):
		if not self.can_place_tower(tower.coordinates):
			raise FieldError
		Pocket.lend_money(tower.cost)
		self.towers.append(tower)
		self.towers_placed += 1


	def destroy(self, tower):
		self.towers.remove(tower)


	def spawn_units(self):
		new_wave = self.spawn_point.spawn_wave()
		if new_wave is None:
			self.all_waves_spawned = True
			return
		for unit in new_wave:
			unit.make_step()
			self.units.append(unit)

	def belong_to_field(self, coords):
		return 0 <= coords.x <= self.width and 0 <= coords.y <= self.height


	def units_step(self):
		for unit in self.units:
			distance = randint(self.min_step, self.max_step)
			far_distance = self.big_step
			directions = [False] * 4
			shift = unit.get_speed_mode()
			if self.can_make_step(unit, distance):
				directions[shift] = True
				unit.make_step()
				continue	
			for i in range(1, 4):
				unit.set_speed_mode((shift + i) % 4)
				if self.can_make_step(unit, far_distance):
					directions[(shift + i) % 4] = True
			unit.set_speed_mode(shift)
			for i in range(4):
				if directions[i] and i != (shift + 2) % 4:
					unit.set_speed_mode(i)
					unit.make_step()


	def units_attack(self):
		for unit in self.units:
			if unit.can_attack(self.castle):
				unit.attack(self.castle)
				self.attacks_by_units.append([unit.coordinates, self.castle.center])
				continue
			for tower in self.towers:
				if unit.can_attack(tower):
					unit.attack(tower)
					self.attacks_by_units.append([unit.coordinates, tower.coordinates])
					break


	def towers_attack(self):
		for tower in self.towers:
			for unit in self.units:
				if tower.can_attack(unit):
					tower.attack(unit)
					self.attacks_by_towers.append([tower.coordinates, unit.coordinates])
					break


	def collect_garbage(self):
		for unit in self.units:
			if unit.health <= 0:
				Pocket.add_money(unit.bounty)
				self.units.remove(unit)
		for tower in self.towers:
			if tower.health <= 0:
				self.towers.remove(tower)


	def update(self):
		current_time = time.time()
		current_castle_health = self.castle.get_health()
		if self.all_waves_spawned and len(self.units) == 0:
			return
		if current_time - self.last_update >= self.update_rate and \
		   current_castle_health > 0:
			
			self.attacks_by_units = []
			self.attacks_by_towers = []
			Pocket.add_money(self.castle.send_money())
			self.units_step()
			self.towers_attack()
			self.units_attack()
			self.collect_garbage()
			if len(self.spawn_point.waves) and \
			   self.spawn_point != -1 and \
			   current_time - self.spawn_point.last_wave >= self.spawn_point.cooldown:
				self.spawn_units()
			self.last_update = current_time

			if self.castle.get_health() <= 0:
				raise CastleError

			if self.all_waves_spawned and len(self.units) == 0:
				raise WinError

