def merge(nums1, nums2):
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


def mergesort(lt, rt, lst):
    if lt < rt:
        m = (lt + rt) // 2
        return merge(mergesort(lt, m, lst), mergesort(m + 1, rt, lst))
    return [lst[lt]]


class Solution:

    def mergeSort(self, nums: list) -> list:
        return mergesort(0, len(nums) - 1, nums)