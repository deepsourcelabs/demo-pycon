# code
def bad_isinstance(initial_condition, object, other_obj, foo, bar, baz):
    if (
        initial_condition
        and isinstance(object, (int, float, str))
        and isinstance(other_obj, float)
        and isinstance(foo, str)
        or (isinstance(bar, float) or isinstance(bar, str))
        and (isinstance(baz, float) or isinstance(baz, int))
    ):
        pass
