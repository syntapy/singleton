import functools
make_key = functools._make_key

__version__ = '1.0.0'

class MSingleton:
    __classes = {}
    def __new__(mcls, *args, **kwargs):
        class Singleton(type):
            _instances = {}
            def __call__(cls, *args, **kwargs):
                hashval = str(make_key(args, kwargs, True))
                if hashval not in cls._instances:
                    cls._instances[hashval] = super(Singleton, cls).__call__(*args, **kwargs)
                return cls._instances[hashval]
        return Singleton
