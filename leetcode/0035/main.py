class Solution(object):
    def searchInsert(self, nums, target):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0 if nums[1] > target else 1

        l = 0
        r = len(nums)-1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] <  target:
                l = m + 1
            else:
                r = m - 1
        return l

def main(nums, target, want):
    s = Solution()
    r = s.searchInsert(nums, target)
    if want != r:
        print("mismatch wanted {} and got {}".format(want, r))

if __name__ == "__main__":
    tests = [
        [[1,3,5,6], 5, 2],
        [[1,3,5,6], 2, 1],
        [[1,3,5,6], 7, 4]
    ]
    for test in tests:
        main(test[0], test[1], test[2])
