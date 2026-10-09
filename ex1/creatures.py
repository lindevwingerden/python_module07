from ex0.creatures import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: str = "itself") -> str:
        return f"{self.name} heals {target} for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: str = "itself and others") -> str:
        return f"{self.name} heals {target} for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} performs a boosted strike!"
        else:
            return f"{self.name} attacks normally."

    def transform(self) -> str:
        if self.transformed:
            return f"{self.name} stays in its sharper form."
        else:
            self.transformed = True
            return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        if not self.transformed:
            return f"{self.name} stays in its normal form."
        else:
            self.transformed = False
            return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        else:
            return f"{self.name} attacks normally."

    def transform(self) -> str:
        if self.transformed:
            return f"{self.name} stays in its dragonic battle form."
        else:
            self.transformed = True
            return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        if not self.transformed:
            return f"{self.name} stays in its stable form."
        else:
            self.transformed = False
            return f"{self.name} stabilizes its form."
