from typing import Callable, Dict, Any


def mage_counter() -> Callable[[], int]:
    count: int = 0

    def increm() -> int:
        nonlocal count
        count += 1
        return count

    return increm


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    count: int = initial_power

    def add_power(power: int) -> int:
        nonlocal count
        count += power
        return count

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:

    def enchant(item_name: str) -> str:
        return f'{enchantment_type} {item_name}'

    return enchant


def memory_vault() -> Dict[str, Callable[..., Any]]:
    vault: Dict[Any, Any] = dict()

    def store(key: Any, value: Any) -> None:
        vault[key] = value

    def recall(key: Any) -> Any | str:
        return vault.get(key, 'Memory not found')

    return {'store': store, 'recall': recall}


def main() -> None:

    print()
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")
    print()

    print("Testing spell accumulator with base 10...")
    accumulator = spell_accumulator(10)
    print(f"Add 5 -> {accumulator(5)}")
    print(f"Add 3 -> {accumulator(3)}")
    print(f"Add 10 -> {accumulator(10)}")
    print()

    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))
    print()

    print("Testing memory vault...")
    vault = memory_vault()
    store = vault["store"]
    recall = vault["recall"]
    store("dragon", "Fire weakness")
    store("potion", 3)
    print(recall("dragon"))
    print(recall("unknown"))


if __name__ == "__main__":
    try:
        main()
    except Exception as cur_error:
        print(f'Error: {cur_error}')
