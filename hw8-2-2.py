# Author RTS 12/9/21

def sum_odds(nums):
    odd = 0
    for x in nums:
        if x % 2 != 0:
            odd += x
    return odd

print(sum_odds([1, 2, 3, 4, 5, 6]) == 9)
print(sum_odds([1, 3, 5, 7, 9]) == 25)
print(sum_odds([2, 4, 6, 8, 10]) == 0)
