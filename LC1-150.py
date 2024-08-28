def merge(nums1, m, nums2, n):
    for j in range(n):
        nums1[m + j] = nums2[j]
    nums1.sort()
a=[1,2,3,0,0,0]
b=[4,6,5]
merge(a,3,b,3)
print(a)