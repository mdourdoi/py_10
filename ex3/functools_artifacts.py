import operator
from typing import List, Callable, Dict, Any
from functools import reduce, partial, lru_cache, singledispatch


def spell_reducer(spells: List[int], operation: str) -> int:
    ops: Dict[str, Callable[[int, int], int]] = {"add": operator.add,
                                                 "multiply": operator.mul,
                                                 "max": max,
                                                 "min": min}
    if operation in ops and spells:
        return reduce(ops[operation], spells)
    return 0


def partial_enchanter(
        base_enchantment: Callable[[int, str, str], str]
) -> Dict[str, Callable[[str], str]]:

    return {'fire_enchant': partial(base_enchantment, 50, 'fire'),
            'ice_enchant': partial(base_enchantment, 50, 'ice'),
            'lightning_enchant': partial(base_enchantment, 50, 'lightning')}


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 2) + memoized_fibonacci(n - 1)


def spell_dispatcher() -> Callable[..., Any]:

    @singledispatch
    def spell(x: Any) -> str:
        return 'Unknown type'

    @spell.register
    def _(x: int) -> str:
        return f'{x} damage done'

    @spell.register
    def _(x: str) -> str:
        return f'Enchanting with {x}'

    # can't use List here because singledispatch needs the real runtime type
    @spell.register
    def _(x: list) -> str:
        if not x:
            return "Can't multicast an empty list"
        ret = 'Multicast: '
        for cast in x:
            ret += f'{cast} '
        ret = ret[:len(ret) - 1]
        return ret

    return spell


def main() -> None:
    def base_enchant(power: int, element: str, target: str) -> str:
        return f"{element} enchant {target} with {power} power"

    print()
    powers = [10, 20, 30, 40]
    print(f"Testing spell reducer on {powers}...")
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")
    print(f"Min: {spell_reducer(powers, 'min')}")
    print()

    print("Testing partial enchanter...")
    enchants = partial_enchanter(base_enchant)
    print(enchants["fire_enchant"]("Sword"))
    print(enchants["ice_enchant"]("Shield"))
    print(enchants["lightning_enchant"]("Staff"))
    print()

    print("Testing memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print()

    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(12))
    print(dispatcher("Flaming"))
    print(dispatcher(["fireball", "heal", "shield"]))
    print()


if __name__ == "__main__":
    try:
        main()
    except Exception as cur_error:
        print(f'Error: {cur_error}')
