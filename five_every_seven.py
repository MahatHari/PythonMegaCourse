import itertools


def foo(lst):

    list_of_list = [lst[i:i+5] for i in range(0, len(lst), 7)]
    # print(list_of_list)
    return list(itertools.chain.from_iterable(list_of_list))


print(foo(['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'mon', 'tue', 'wed', 'thu',
           'fri', 'sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'mon']))
