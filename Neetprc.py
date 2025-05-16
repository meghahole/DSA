class Solution:
    def merge1(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n== 0: return
        len1 = len(nums1)

        end_nums1 = len1 - 1

        while n > 0 and m > 0:
            if nums2[m-1] >= nums1[n-1]:
                nums1[end_nums1] = nums2[m-1]
                n -= 1
                print(nums1)
            else:
                nums1[end_nums1] = nums1[m-1]
                m -= 1
            end_nums1 -= 1
            
        print(nums1)
    
s = Solution()
s.merge1([1,2,3,0,0,0], 3, [2,5,6], 3)