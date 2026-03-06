from time import time, sleep
from functools import wraps
from typing import Callable, Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f'Casting {func.__name__}...')
        timer = time()
        res = func(*args, **kwargs)
        timer = time() - timer
        print(f'Spell completed in {timer:.4f} seconds')
        return res

    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any | str]:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any | str:
            power = kwargs.get("power")
            if power is None:
                power = args[1]
            if power < min_power:
                return 'Insufficient power for this spell'
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any | str]:

    def decorator(func: Callable[..., Any]) -> Callable[..., Any | str]:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any | str:
            for i in range(max_attempts):
                try:
                    res = func(*args, **kwargs)
                    return res
                except Exception:
                    print('Spell failed, retrying... ', end='')
                    print(f'(attempt {i+1}/{max_attempts})')
            return f'Spell casting failed after {max_attempts} attempts'

        return wrapper

    return decorator


class MageGuild():

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return name.replace(' ', '').isalpha()

    @power_validator(10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        '''Modified signature because the decorator is supposed to look at the
        first argument (after self) and it is supposed to be "power"'''
        return f'Successfully cast {spell_name} with {power} power'


def main() -> None:

    print()
    print("Testing spell timer...")

    @spell_timer
    def quick_spell() -> str:
        sleep(0.10)
        return "Quick spell cast!"

    print(quick_spell())
    print()

    print("Testing power validator (MageGuild.cast_spell)...")
    guild = MageGuild()
    print(guild.cast_spell(5, "Fireball"))
    print(guild.cast_spell(15, "Fireball"))
    print()

    print("Testing retry spell...")

    attempts = {"count": 0}

    @retry_spell(3)
    def unstable_spell() -> str:
        attempts["count"] += 1
        if attempts["count"] < 3:
            raise RuntimeError("Spell fizzled")
        return "Unstable spell succeeded!"

    print(unstable_spell())
    print()

    print("Testing mage name validation...")
    print("Gandalf ->", MageGuild.validate_mage_name("Gandalf"))
    print("Gandalf the Grey ->",
          MageGuild.validate_mage_name("Gandalf the Grey"))
    print("Ga ->", MageGuild.validate_mage_name("Ga"))
    print("123 ->", MageGuild.validate_mage_name("123"))


if __name__ == "__main__":
    try:
        main()
    except Exception as cur_error:
        print(f'Error: {cur_error}')
