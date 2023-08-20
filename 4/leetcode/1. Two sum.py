target = 19999


def fn(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]

def fn2(nums, target):
    sorted_nums = sorted(nums)

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]

call = fn

# print(call([2,7,11,15], 9))
# print(call([3,2,4], 6))
# print(call([3,3], 6))



