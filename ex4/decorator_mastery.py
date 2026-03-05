from time import time
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
            if args[0] >= min_power:
                return func(*args, **kwargs)
            return 'Insufficient power for this spell'

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:

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
