from unittest.mock import patch
from recorddetail3 import RecordDetail
import logging

class MyClass():

    def __init__(self):
        self._my_attribute = 55

    def my_method(self):
        print(self)

    @classmethod
    def my_classmethod(cls):
        print(cls)
        # notice cls in argument list

    @staticmethod
    def my_static():
        print('Static')

    @property
    def my_attribute(self,):
        return self._my_attribute

    @my_attribute.setter
    def my_attribute(self, value):
        self._my_attribute = value


@patch.object(RecordDetail, 'stop')
def test_foo(mock_rd):
    rd = RecordDetail('foo')
    print(rd.stop())


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test_foo()
    c = MyClass()
    c.my_method()
    c.my_static()
    c.my_classmethod()
    print(c.my_attribute)
    c.my_attribute = 'Bang'
    print(c.my_attribute)
