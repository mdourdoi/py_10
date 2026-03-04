import operator
from typing import List, Callable, Dict
from functools import reduce, partial, lru_cache


def spell_reducer(spells: List[int], operation: str) -> int:
    ops: Dict[str, Callable[[int, int], int]] = {"add": operator.add,
                                                 "multiply": operator.mul,
                                                 "max": max,
                                                 "min": min}
    if operation in ops.keys() and len(spells) > 0:
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
