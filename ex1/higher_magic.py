from typing import Callable, Tuple, Any, List


def spell_combiner(
        spell1: Callable[..., Any],
        spell2: Callable[..., Any]) -> Callable[..., Tuple[Any, Any]]:

    def combined(*args: Any, **kwargs: Any) -> Tuple[Any, Any]:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))

    return combined


def power_amplifier(
        base_spell: Callable[..., int],
        multiplier: int) -> Callable[..., int]:

    def amplified(*args: Any, **kwargs: Any) -> int:
        return base_spell(*args, **kwargs) * multiplier

    return amplified


def conditional_caster(
        condition: Callable[..., bool],
        spell: Callable[..., Any]) -> Callable[..., Any | str]:

    def check_condition(*args: Any, **kwargs: Any) -> Any | str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return 'Spell fizzled'

    return check_condition


def spell_sequence(spells: List[Callable[..., Any]]) -> Callable[..., Any]:

    def in_sequence(*args: Any, **kwargs: Any) -> List[Any]:
        return [spell(*args, **kwargs) for spell in spells]

    return in_sequence


if __name__ == "__main__":

    def fireball(target: str, power: int) -> int:
        print(f"Fireball hits {target}!")
        return power

    def heal(target: str, amount: int) -> int:
        print(f"Heals {target}!")
        return amount

    def can_cast(target: str, power: int) -> bool:
        return power >= 10

    print("Testing spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    result = combined_spell("Dragon", 10)
    print(f"Combined spell result: {result}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    original = fireball("Goblin", 10)
    amplified = mega_fireball("Goblin", 10)
    print(f"Original: {original}, Amplified: {amplified}")

    print("\nTesting conditional caster...")
    safe_fireball = conditional_caster(can_cast, fireball)
    print(f"Cast with 15 power: {safe_fireball('Ogre', 15)}")
    print(f"Cast with 5 power: {safe_fireball('Ogre', 5)}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    seq_results = sequence("Knight", 12)
    print(f"Sequence results: {seq_results}")
