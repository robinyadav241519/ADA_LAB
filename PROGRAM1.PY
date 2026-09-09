from typing import List

def search(nums: List[int], target: int) -> int:
    """Return the index of target in a rotated sorted array, or -1 if absent."""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def myPow(x: float, n: int) -> float:
    """Return x raised to the power n using exponentiation by squaring."""
    if n == 0:
        return 1.0

    if n < 0:
        x = 1.0 / x
        n = -n

    result = 1.0

    while n:
        if n & 1:
            result *= x
        x *= x
        n >>= 1

    return result