import functools
make_key = functools._make_key

__version__ = '0.1.0'

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        hashval = str(make_key(args, kwargs, True))
        if cls not in cls._instances:
            cls._instances[cls] = {}
        if hashval not in cls._instances[cls]:
            cls._instances[cls][hashval] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls][hashval]
