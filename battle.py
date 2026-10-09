import ex0


def test_factory(
        factory: ex0.CreatureFactory
) -> None:
    print("Testing factory")
    creatures = [factory.create_base(), factory.create_evolved()]
    for creature in creatures:
        print(creature.describe())
        print(creature.attack())


def test_battle(
        factory1: ex0.CreatureFactory,
        factory2: ex0.CreatureFactory
) -> None:
    print("Testing battle")
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()
    print(creature1.describe())
    print(" vs.")
    print(creature2.describe())
    print(" fight!")
    print(creature1.attack())
    print(creature2.attack())


if __name__ == "__main__":
    flame = ex0.FlameFactory()
    aqua = ex0.AquaFactory()
    test_factory(flame)
    print("")
    test_factory(aqua)
    print("")
    test_battle(flame, aqua)
