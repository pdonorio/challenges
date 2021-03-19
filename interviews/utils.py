def find_subobjects(obj):
    return [x for x in dir(obj) if not x.startswith('_')]


def find_funcs(obj):
    """ introspecting object to find functions and docs """
    infos = {}
    for y in find_subobjects(obj):
        attr = getattr(obj, y)
        if callable(attr):
            infos[y] = attr.__doc__
    return infos
