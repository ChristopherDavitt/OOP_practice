def intersection(nums1, nums2):
    return list(set(nums1).intersection(nums2))

intersection(nums1 = [4,9,5], nums2 = [9,4,9,5,2])

# or 

def intersections(nums1, nums2):
    return list(set(filter(lambda x: True if x in nums2 else False, nums1)))

intersection(nums1 = [4,9,5], nums2 = [9,4,9,5,2])