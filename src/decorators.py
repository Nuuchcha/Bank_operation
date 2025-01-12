import os
import sys
from datetime import datetime
from functools import wraps

def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
            except Exception as e:
                log_message = f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}"
            finally:
                end_time = datetime.now()
                log_message += f" | Time: {end_time - start_time}"
                if filename:
                    with open(filename, 'a') as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)
        return wrapper
    return decorator
