from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable[[Any], Any]:
    """Декоратор, для функций, выводит информацию о положительном выполнении функции, либо об ошибке выполнения
    в файл .log, если указано имя файла, либо в консоль"""

    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = datetime.now()
            result = None
            log_message = ""
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
            except Exception as e:
                log_message = f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}"
            finally:
                end_time = datetime.now()
                log_message += f" | Time: {end_time - start_time}"
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)
                return result

        return wrapper

    return decorator
