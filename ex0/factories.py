import abc
from . import creatures


class CreatureFactory(abc.ABC):
    @abc.abstractmethod
    def create_base(self) -> creatures.Creature:
        pass

    @abc.abstractmethod
    def create_evolved(self) -> creatures.Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> creatures.Flameling:
        return creatures.Flameling()

    def create_evolved(self) -> creatures.Pyrodon:
        return creatures.Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> creatures.Aquabub:
        return creatures.Aquabub()

    def create_evolved(self) -> creatures.Torragon:
        return creatures.Torragon()
