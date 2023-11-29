import sys
def findMaxLength(nums):
    count = 0
    max_length = 0
    count_dict = {0: -1}

    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1

        if count in count_dict:
            max_length = max(max_length, i - count_dict[count])
        else:
            count_dict[count] = i

    return max_length
    
nums_input = input()
nums = list(map(int, nums_input.split()))
output = findMaxLength(nums)
print(output)


# # Example 1
# nums1 = [0, 0, 0, 1, 1, 1, 1, 0]
# output1 = findMaxLength(nums1)
# print(output1)

# # Example 2
# nums2 = [1, 0, 0, 1, 1, 1, 1, 0]
# output2 = findMaxLength(nums2)
# print(output2)