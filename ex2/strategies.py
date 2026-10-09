import abc
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleError(Exception):
    def __init__(self, message: str = "Unknown battle error") -> None:
        super().__init__(message)


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abc.abstractmethod
    def act(self, creature: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise BattleError(
                f"Invalid Creature '{creature.name}' "
                "for this normal strategy"
            )
        else:
            return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if (
            self.is_valid(creature)
            and isinstance(creature, TransformCapability)
        ):
            return (
                f"{creature.transform()}\n{creature.attack()}"
                f"\n{creature.revert()}"
            )
        else:
            raise BattleError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if (
            self.is_valid(creature)
            and isinstance(creature, HealCapability)
        ):
            return f"{creature.attack()}\n{creature.heal()}"
        else:
            raise BattleError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )
