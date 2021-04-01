from abc import ABC, abstractmethod
from .weak_tower import WeakTower
from .average_tower import AverageTower
from .tower import Tower

class TowerCreator(ABC):
	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def create(self, *args, **kwargs) -> Tower:
		pass

class WeakTowerCreator(TowerCreator):
	def __init__(self):
		super().__init__()

	def create(self, *args, **kwargs) -> Tower:
		return WeakTower(*args, **kwargs)


class AverageTowerCreator(TowerCreator):
	def __init__(self):
		super().__init__()

	def create(self, *args, **kwargs) -> Tower:
		return AverageTower(*args, **kwargs)
