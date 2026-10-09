import ex0
import ex1
import ex2


def battle(
        opponents: list[tuple[ex0.CreatureFactory, ex2.BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    if len(opponents) < 2:
        print(
            "Aborting tournament: "
            f"{len(opponents)} creature(s) is not enough to battle"
        )
        return
    print(f"{len(opponents)} opponents involved")
    creatures = [
        (opponent[0].create_base(), opponent[1]) for opponent in opponents
    ]
    while len(creatures) > 1:
        challenger = creatures.pop(0)
        for opponent in creatures:
            print("\n* Battle *")
            print(f"{challenger[0].describe()}\n vs.")
            print(f"{opponent[0].describe()}\n now fight!")
            try:
                print(challenger[1].act(challenger[0]))
                print(opponent[1].act(opponent[0]))
            except ex2.BattleError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def tournaments() -> None:
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    flame = ex0.FlameFactory()
    normal = ex2.NormalStrategy()
    healing = ex1.HealingCreatureFactory()
    defensive = ex2.DefensiveStrategy()
    battle([(flame, normal), (healing, defensive)])

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    aggressive = ex2.AggressiveStrategy()
    battle([(flame, aggressive), (healing, defensive)])

    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    aqua = ex0.AquaFactory()
    transform = ex1.TransformCreatureFactory()
    battle([(aqua, normal), (healing, defensive), (transform, aggressive)])


if __name__ == "__main__":
    tournaments()
