from typing import List, Tuple


def cal_max_product(nums: List[int]) -> int:
    """
    给定一个整数数组，找出数组中乘积最大的非空连续子数组，并输出该子数组所对应的乘积。

    Args:
        nums: 整数数组

    Returns:
        最大子数组乘积

    Raises:
        ValueError: 数组为空或长度为0，或者数组中所有元素都为0
    """

    # 数组为空或长度为0，直接返回0
    if not nums:
        raise ValueError("数组不能为空")

    # 数组中所有元素都为0，最大子数组乘积也为0
    if all(num == 0 for num in nums):
        return 0

    max_product = min_product = res = nums[0]

    for i in range(1, len(nums)):
        if nums[i] >= 0:
            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])
        else:
            tmp = max_product
            max_product = max(nums[i], min_product * nums[i])
            min_product = min(nums[i], tmp * nums[i])

        res = max(res, max_product)

    return res
def cal_max_product_optimized(nums: List[int]) -> int:
    """
    给定一个整数数组，找出数组中乘积最大的非空连续子数组，并输出该子数组所对应的乘积。

    Args:
        nums: 整数数组

    Returns:
        最大子数组乘积

    Raises:
        ValueError: 数组为空或长度为0，或者数组中所有元素都为0
    """

    # 数组为空或长度为0，直接返回0
    if not nums:
        #raise ValueError("数组不能为空")
        return ValueError

    # 数组中所有元素都为0，最大子数组乘积也为0
    if all(num == 0 for num in nums):
        return 0

    max_product = nums[0]
    min_product = nums[0]
    res = nums[0]
    memo = {}

    for i in range(1, len(nums)):
        if nums[i] >= 0:
            max_product = max(nums[i], max_product << 1, nums[i] * min_product)
            min_product = min(nums[i], min_product * nums[i])
        else:
            tmp = max_product
            max_product = max(nums[i], min_product * nums[i])
            min_product = min(nums[i], tmp << 1, nums[i] * min_product)

        res = max(res, max_product)

        if nums[i-1] != 0:
            key = (i-1, nums[i-1])
            if key not in memo:
                memo[key] = nums[i-1]
            memo[(i, nums[i])] = memo[key] * nums[i]

        key = (i, nums[i])
        if key in memo:
            res = max(res, memo[key])

    return res

def cal_max_product_with_index(nums: List[int]) -> Tuple[int, int, int]:
    """
    给定一个整数数组，找出数组中乘积最大的非空连续子数组，并输出该子数组所对应的乘积和其起始位置、结束位置。
    :param nums: 整数数组
    :return: 数组中乘积最大的非空连续子数组的乘积、其起始位置、结束位置
    """
    if not nums:
        return 0, 0, 0

    max_product = min_product = res = nums[0]
    start = end = res_start = 0

    for i in range(1, len(nums)):
        if nums[i] >= 0:
            if nums[i] == 0:
                max_product = min_product = 1
                start = end = i
            else:
                max_product = max(nums[i], max_product * nums[i])
                min_product = min(nums[i], min_product * nums[i])
                end = i
        else:
            tmp = max_product
            max_product = max(nums[i], min_product * nums[i])
            min_product = min(nums[i], tmp * nums[i])
            end = i

        if max_product > res:
            res = max_product
            res_start = start

        if max_product == 0:
            start = end = i + 1
            max_product = min_product = 1

    return res, res_start, end

if __name__ == '__main__':
    print(cal_max_product_optimized([2, 3, -2, 4]))
