def two_sum(nums, target):
    result = []
    n = len(nums)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)

    return result


# print("Введите значение желаемой суммы: ")
# target = int(input())
#
# print("Введите длину массива: ")
# n = int(input())
#
# nums = []
# print("Введите значения для массива: ")
# for i in range(n):
#     k = int(input())
#     nums.append(k)
#
# print(two_sum(nums,target))
