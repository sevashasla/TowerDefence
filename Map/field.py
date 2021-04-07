from .road import Road
from .castle import Castle
from random import randint
from .spawn_point import SpawnPoint
import time
import json

from ..Game.coordinates import Coordinates
from ..Tower.tower_factories import *
from ..Game.pocket import Pocket
from ..Game.errors import *

class Field:

	def __init__(self, data):
		self.width = data["shape"]["width"]
		self.height = data["shape"]["height"]
		self.road = Road(self.width, self.height, data["road"])
		self.castle = Castle(self.width, self.height, data["castle"])
		self.spawn_point = SpawnPoint(data["spawn_point"], data["waves"])
		
		self.units = []
		self.towers = []
		self.waves_spawned = 0
		self.update_rate = 0.1
		self.last_update = 0.0


	def can_make_step(self, unit, distance) -> bool:
		try:    
			new_coords_x = unit.coordinates.x + distance * unit.speed[0]
			new_coords_y = unit.coordinates.y + distance * unit.speed[1]
			new_coords = Coordinates(new_coords_x, new_coords_y)
			if self.road.belongs_to_road(new_coords):
				return True
		except IndexError:
			return False


	def can_place_tower(self, coords) -> bool:
		try:
			if not self.road.belongs_to_road(coords) and \
			   not self.castle.belongs_to_castle(coords):
				return True
		except IndexError:
			return False

		return False


	def place_tower(self, tower):
		if not self.can_place_tower(tower.coordinates):
			raise FieldError
		Pocket.lend_money(tower.cost)
		self.towers.append(tower)


	def destroy (self, tower):
		self.towers.remove(tower)


	def spawn_units(self):
		self.waves_spawned += 1
		for unit in self.spawn_point.wave():
			unit.make_step()
			self.units.append(unit)


	def units_step(self):
		for unit in self.units:
			distance = randint(2, 18)
			if self.can_make_step(unit, distance):
				unit.make_step()
				continue
			if unit.speed[0] != 0:
				unit.speed[0], unit.speed[1] = unit.speed[1], -abs(unit.speed[0])
				unit.make_step()
			else:
				unit.speed[0], unit.speed[1] = unit.speed[1], unit.speed[0]
				distance = 75
				if self.can_make_step(unit, distance):
					unit.make_step()
				else:
					unit.speed[0] *= -1
					unit.make_step()
		
		# for unit in self.units:
		# 	print(unit.__str__())
		# print()

	def units_attack(self):
		for unit in self.units:
			for tower in self.towers:
				if unit.can_attack(tower):
					unit.attack(tower)
					break

	def towers_attack(self):
		for tower in self.towers:
			for unit in self.units:
				if tower.can_attack(unit):
					tower.attack(unit)
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
		if current_time - self.last_update >= self.update_rate:
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

