Makes any python class a singleton by calling

```python
from singleton import Singleton

class MyClass(metaclass=Singleton, Baseclasses...):
   pass
```

This is method 2 taken from [here](https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python) but adapted to support separate instances for different constructor arguments

ToDo
----
Approaches to offer
- metaclass
- class decorator
- base class

Requirements are
- [ ] Singleton for each class for each combo of arguments
  - i.e. can have multiple instances of same class if they have different constructor arguments
  - [x] metaclass
  - [ ] class decorator
  - [ ] base class
- [ ] A separate object contains all instances of each class
  - Do not e.g. have a single dict containing every instances of the singleton (that is just bloated, and any bugs could leak out to other different classes
  - [ ] metaclass (probably not possible)
  - [ ] class decorator
  - [ ] base class
