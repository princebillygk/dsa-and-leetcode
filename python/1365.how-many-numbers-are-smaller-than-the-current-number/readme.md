## Failed approaches

# Cannot not be solved with quicksort tried once

Stupid thought of mines :')

Code:

```
class Solution:

    @staticmethod
    def quicksort(nums: List[int], positions: List[int], high: int, low: int = 0):
        if (low > high):
            return
        pivotIdx = high
        pivotVal = nums[pivotIdx]
        smallerCount: int = 0

        for i in range(pivotIdx):
            if nums[i] < nums[pivotIdx]:
                smallerCount += 1
                nums[pivotIdx], nums[i] = nums[i], nums[pivotIdx - 1]
                nums[pivotIdx - 1] = pivotVal
                pivotIdx -= 1

        positions[pivotIdx] = smallerCount

        Solution.quicksort(nums, positions, pivotIdx - 1, low)
        Solution.quicksort(nums, positions, high, pivotIdx + 1)

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        positions = [0] * len(nums)
        Solution.quicksort(nums, positions, len(nums) - 1)
        print(nums, positions)
        return positions
```
