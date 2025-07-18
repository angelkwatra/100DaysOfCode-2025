from collections import Counter

def k_frequency_sum(nums, k):
    freq = Counter(nums)
    return sum(num for num, count in freq.items() if count == k)

# Example
print(k_frequency_sum([2, 3, 9, 9], 1))  
print(k_frequency_sum([1, 8, 8, 8, 5, 6, 2], 3))  
