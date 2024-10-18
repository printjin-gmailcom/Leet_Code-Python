def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    next_greater = {}
    stack = []
    
    for num in reversed(nums2):
        while stack and stack[-1] <= num:
            stack.pop()
        next_greater[num] = stack[-1] if stack else -1
        stack.append(num)
    
    return [next_greater[num] for num in nums1]
