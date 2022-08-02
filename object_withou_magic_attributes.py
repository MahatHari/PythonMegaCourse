import re

# return attributes of obj without magic attributes  __something__


def foo(obj):
    all_attributes = dir(obj)
    normal_attributes = [attribute for attribute in all_attributes
                         if not re.compile("__[a-z0-9A-z]*__").search(attribute)]
    return normal_attributes


print(foo(str))

# return id of object


def boo(obj):
    return id(obj)


print(boo(str))
