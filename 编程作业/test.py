from typing import List, Tuple
import unittest


def maxProduct(nums: List[int]) -> int:
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


def maxProductWithIndex(nums: List[int]) -> Tuple[int, int, int]:
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


# 测试代码

#创建一个继承unittest.TestCase的类
class Tests(unittest.TestCase):
    # 创建test_为前缀的方法
    def test_1(self):
        self.assertEqual(maxProduct([]), ValueError)

    def test_2(self):
        self.assertEqual(maxProduct([1, 2, 0, 3, 0, 4]), 4)

    def test_3(self):
        self.assertEqual(maxProduct([0, 0, 0]), 0)

    def test_4(self):
        self.assertEqual(maxProduct([3, 4, 1, 6]), 72)

    def test_5(self):
        self.assertEqual(maxProduct([-2, -3, -5]), 15)

    def test_6(self):
        self.assertEqual(maxProduct([3]), 3)

    def test_7(self):
        self.assertEqual(maxProduct([-2]), -2)

    def test_8(self):
        self.assertEqual(maxProduct([2, 3, -2, 4, -1]), 48)

    def test_9(self):
        self.assertEqual(maxProduct([1, 2, 3, -1, 4]), 6)

    def test_10(self):
        self.assertEqual(maxProduct([-2, -3, -1, -4]), 24)

    def test_11(self):
        self.assertEqual(maxProduct([1, -1, 2, -2, 3, -3]), 36)


#unittest.main()作为主函数入口
if __name__ == '__main__':

    print(maxProduct([2, 3, -2, 4]))
    unittest.main()

