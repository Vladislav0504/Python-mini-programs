class Solution:
    
    def merge(self, nums1: list, nums2: list) -> list:
        lst = []
        i1, i2 = 0, 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] <= nums2[i2]:
                lst.append(nums1[i1])
                i1 += 1
            else:
                lst.append(nums2[i2])
                i2 += 1
        lst.extend(nums1[i1:])
        lst.extend(nums2[i2:])
        return lst
