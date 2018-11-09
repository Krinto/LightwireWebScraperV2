import time

def time_cache(seconds):
    def cache(f):
        last_time, last_result = None, None
        def wrapper():
            nonlocal last_time, last_result
            if last_result is None or time.time() - last_time > seconds:
                last_result, last_time = f(), time.time()
            return last_result

        return wrapper
    return cache
