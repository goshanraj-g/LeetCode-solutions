class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            if numbers[r]+numbers[l] > target:
                r -= 1
            elif numbers[l]+numbers[l] < target:
                l +=1
