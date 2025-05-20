import functools, time

def slowDown(_func=None, *, rate=1): # Decorator. Takes in rate=float(sec), makes the function wait before each execution. (Default rate = 1)
    def decoratorSlowDown(func):
        @functools.wraps(func)
        def wrapperSlowDown(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapperSlowDown
    if _func is None:
        return decoratorSlowDown
    else:
        return decoratorSlowDown(_func)