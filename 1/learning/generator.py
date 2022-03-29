from memory_profile import profile


def fn(arr):
    for elem in arr:
        yield elem ** 2

fn([1,2,3,4,5,5])
