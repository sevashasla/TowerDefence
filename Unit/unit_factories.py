from .weak_unit import WeakUnit
from .unit import UnitCreator
from .weak_unit import WeakUnit
from .average_unit import AverageUnit
from .chad_unit import ChadUnit


class WeakUnitCreator(UnitCreator):

	def create(self, *args, **kwargs) -> WeakUnit:
		return WeakUnit(*args, **kwargs)


class AverageUnitCreator(UnitCreator):

	def create(self, *args, **kwargs) -> AverageUnit:
		return AverageUnit(*args, **kwargs)


class ChadUnitCreator(UnitCreator):

	def create(self, *args, **kwargs) -> ChadUnit:
		return ChadUnit(*args, **kwargs)


