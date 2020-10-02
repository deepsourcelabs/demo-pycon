class MyClass:
    def __init__(self):
        pass

    @something
    def smethod():
        """static method-to-be"""

    smethod = staticmethod(smethod)  # issue here

    if True:
        smethod = staticmethod(smethod)  # issue here

    @staticmethod
    def my_second_method():
        """correct static method definition"""

    def other_method():
        """some method"""

    smethod2 = staticmethod(other_method)  # issue here


def helloworld():
    """says hello"""


MyClass.new_static_method = staticmethod(helloworld)


class MyOtherClass:
    """Some other class"""

    _make = staticmethod(tuple.__new__)


class MyClassEdge:
    def __init__(self):
        pass

    @something
    def smethod():
        """static method-to-be"""

    smethod = staticmethod(smethod)  # issue here

    if True:
        smethod = staticmethod(smethod)  # issue here

    @staticmethod
    def my_second_method():
        """correct static method definition"""

    def other_method(self, x, y):
        """some method"""

    smethod2 = staticmethod(other_method)  # issue here

    def other_method_2(self, x, y):
        """some method"""

    smethod2 = staticmethod(other_method_2)  # issue here

    def other_method_3(self):
        """some method"""

    smethod2 = staticmethod(other_method_3)  # issue here
