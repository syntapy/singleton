import functools
make_key = functools._make_key
import datetime
from singleton import MSingleton

def get_hash(*args, **kwargs):
    return make_key(args, kwargs, True)

def test_hash():
    h1=get_hash()
    h2=get_hash(4, 's')
    h3=get_hash(4, 't')
    h4=get_hash(abc=None)

    class F:
        __slots__ = 'a', 'b'
    f=F()
    f.a=25
    f.b=datetime.datetime.now()

    h5=get_hash(f)

def test_multiple_classes():

    import pdb
    pdb.set_trace()
    v=MSingleton()
    class A(metaclass=MSingleton()):
        pass

    class B(metaclass=MSingleton()):
        pass

    a1=A()
    b1=B()
    a2=A()

    b2=B()

    assert a1 is a2
    assert b1 is b2

    assert a2 is not b2
