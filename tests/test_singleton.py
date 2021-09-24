import sys
import os
sys.path.append(os.getcwd()+os.path.sep+'src')

import pytest
import datetime
from singleton import Singleton

import functools
make_key = functools._make_key

def get_hash(*args, **kwargs):
    return make_key(args, kwargs, True)

class args:
    def __init__(self, *args, **kwargs):
        self.args=args
        self.kwargs=kwargs

    def __call__(self):
        return self.args, self.kwargs

@pytest.fixture
def args_list():

    alist = []
    alist.append(args())
    alist.append(args(4, 's'))
    alist.append(args(4, 't'))
    alist.append(args(abc=None))

    class F:
        __slots__ = 'a', 'b'
    f=F()
    f.a=25
    f.b=datetime.datetime.now()

    alist.append(args(f))

    return alist

def test_hash(args_list):
    for arg_combo in args_list:
        args, kwargs = arg_combo()
        h = get_hash(*args, **kwargs)
        print(h)

def test_multiple_classes(args_list):

    class A(metaclass=Singleton):
        def __init__(self, *args, **kwargs):
            pass

    class B(metaclass=Singleton):
        def __init__(self, *args, **kwargs):
            pass

    for i in range(1, len(args_list)):
        args_0, kwargs_0 = args_list[i-1]()
        args_1, kwargs_1 = args_list[i]()

        a_0a=A(*args_0, **kwargs_0)
        a_0b=A(*args_0, **kwargs_0)
        a_1a=A(*args_1, **kwargs_1)

        b_0a=B(*args_0, **kwargs_0)
        b_1a=B(*args_1, **kwargs_1)

        assert a_0a is a_0b
        assert a_0a is not a_1a
        assert a_0a != a_1a

        assert a_0a != b_0a
        assert b_0a != b_1a
        assert b_0a is not b_1a
