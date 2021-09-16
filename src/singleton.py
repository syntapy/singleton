import functools


VERSION = (0, 1, 0, 'dev1')
__version__ = '.'.join(map(str, VERSION))

make_key = functools._make_key


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        hashval = str(make_key(args, kwargs, True))
        if cls not in cls._instances:
            cls._instances[cls] = {}
        if hashval not in cls._instances[cls]:
            cls._instances[cls][hashval] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls][hashval]
