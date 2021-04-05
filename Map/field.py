<<<<<<< HEAD
from .road import Road
=======
from .road import Road, FieldError
>>>>>>> delete it later
from .castle import Castle
from random import randint
from .spawn_point import SpawnPoint
import time
import json

from ..Game.coordinates import Coordinates
from ..Tower.tower_factories import *
from ..Game.pocket import Pocket
<<<<<<< HEAD
from ..Game.errors import *

class Field:

=======

class Field:


>>>>>>> delete it later
	def __init__(self, data):
		self.width = data["shape"]["width"]
		self.height = data["shape"]["height"]
		self.road = Road(self.width, self.height, data["road"])
<<<<<<< HEAD
		self.castle = Castle(data["castle"])
		self.spawn_point = SpawnPoint(data["spawn_point"], data["waves"])
=======
		self.castle = Castle(self.width, self.height, data["castle"])
		self.spawn_point = SpawnPoint(self.width, self.height, data["waves"])
>>>>>>> delete it later
		
		self.units = []
		self.towers = []
		self.waves_spawned = 0
		self.update_rate = 0.1
		self.last_update = 0.0


<<<<<<< HEAD
	def can_make_step(self, unit, distance) -> bool:
		try:    
			new_coords_x = unit.coordinates.x + distance * unit.speed[0]
			new_coords_y = unit.coordinates.y + distance * unit.speed[1]
			new_coords = Coordinates(new_coords_x, new_coords_y)
			if self.castle.belongs_to_castle(new_coords):
				unit.speed = [0, 0]
				return False
=======
	def can_make_step(self, unit) -> bool:
		try:    
			new_coords_x = unit.coordinates.x + randint(2, 18) * unit.speed[0]
			new_coords_y = unit.coordinates.y + randint(2, 18) * unit.speed[1]
			new_coords = Coordinates(new_coords_x, new_coords_y)
>>>>>>> delete it later
			if self.road.belongs_to_road(new_coords):
				return True
		except IndexError:
			return False


	def can_place_tower(self, coords) -> bool:
		try:
<<<<<<< HEAD
			if not self.road.belongs_to_road(coords) and \
			   not self.castle.belongs_to_castle(coords) and \
			   self.belong_to_field(coords):
=======
			if not self.road.belongs_to_road(coords) and not self.castle.belongs_to_castle(coords):
>>>>>>> delete it later
				return True
		except IndexError:
			return False

<<<<<<< HEAD
		return False


	def place_tower(self, tower):
		if not self.can_place_tower(tower.coordinates):
			raise FieldError
		Pocket.lend_money(tower.cost)
		self.towers.append(tower)
=======
		return True #change later


	def place_tower(self, tower):
		if self.can_place_tower(tower.coordinates):
			self.towers.append(tower)
		else:
			raise FieldError
>>>>>>> delete it later


	def destroy (self, tower):
		self.towers.remove(tower)


	def spawn_units(self):
		self.waves_spawned += 1
<<<<<<< HEAD
		for unit in self.spawn_point.wave():
			unit.make_step()
			self.units.append(unit)

	def belong_to_field(self, coords):
		return 0 <= coords.x <= self.width and 0 <= coords.y <= self.height


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
=======
		for unit in self.spawn_point.wave(self.waves_spawned):
			unit.make_step()
			self.units.append(unit)


	def units_step(self):
		
		for unit in self.units:
			if self.can_make_step(unit):
				unit.make_step()
				continue
			if unit.speed[1] == 0:
				unit.speed[1] = -abs(unit.speed[0])
				unit.speed[0] = 0
			if self.can_make_step(unit):
				unit.make_step()
				continue
			unit.speed[0], unit.speed[1] = unit.speed[1], unit.speed[0]
			if self.can_make_step(unit):
				unit.make_step()
				continue
			unit.speed[0] *= -1
			if self.can_make_step(unit):
				unit.make_step()
				continue
			continue
			for unit in self.units:
				print(unit.__str__())
			print()
>>>>>>> delete it later

	def units_attack(self):
		for unit in self.units:
			for tower in self.towers:
				if unit.can_attack(tower):
<<<<<<< HEAD
					unit.attack(tower)
					break
			if unit.can_attack(self.castle):
				unt.attack(self.castle)

=======
					unit.attack(tower)	
>>>>>>> delete it later

	def towers_attack(self):
		for tower in self.towers:
			for unit in self.units:
				if tower.can_attack(unit):
					tower.attack(unit)
<<<<<<< HEAD
					break
=======
>>>>>>> delete it later

	def collect_garbage(self):
		for unit in self.units:
			if unit.health <= 0:
<<<<<<< HEAD
				Pocket.add_money(unit.bounty)
=======
				Pocket.addMoney(unit.bounty)
>>>>>>> delete it later
				self.units.remove(unit)
		for tower in self.towers:
			if tower.health <= 0:
				self.towers.remove(tower)

	def update(self):
		current_time = time.time()
		if current_time - self.last_update >= self.update_rate:
<<<<<<< HEAD
			Pocket.add_money(self.castle.send_money())
=======
>>>>>>> delete it later
			self.units_step()
			self.towers_attack()
			self.units_attack()
			self.collect_garbage()
<<<<<<< HEAD
			if len(self.spawn_point.waves) and \
			   self.spawn_point != -1 and \
			   current_time - self.spawn_point.last_wave >= self.spawn_point.cooldown:
				self.spawn_units()
=======
			if current_time - self.spawn_point.last_wave >= self.spawn_point.time_out:
				self.spawn_units()
				self.spawn_point.last_wave = current_time
>>>>>>> delete it later
			self.last_update = current_time

