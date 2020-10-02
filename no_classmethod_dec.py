# no-classmethod-decorator
class MyClass:
    def __init__(self):
        pass

    @something
    def cmethod(cls, something):
        """class method-to-be"""

    cmethod = classmethod(cmethod)

    if True:
        cmethod = classmethod(cmethod)
        classmethod(cmethod)

    @classmethod
    def my_second_method(cls):
        """correct class method definition"""

    def other_method(self):
        """some method"""

    # Comment
    cmethod2 = classmethod(other_method)


def helloworld():
    """says hello"""


MyClass.new_class_method = classmethod(helloworld)
MyClass.other_method = classmethod(MyClass.other_method)


class MyOtherClass:
    """Some other class"""

    _make = classmethod(tuple.__new__)


class MyClassEdgeCases:
    def __init__(self):
        pass

    @something
    def cmethod(something, something):  # Comment
        """class method-to-be"""

    cmethod = classmethod(cmethod)

    if True:
        cmethod = classmethod(cmethod)
        classmethod(cmethod)

    @classmethod
    def my_second_method(cls):
        """correct class method definition"""

    def other_method(something, some, thing):  # comment
        """some method"""

    # Comment
    cmethod2 = classmethod(other_method)
