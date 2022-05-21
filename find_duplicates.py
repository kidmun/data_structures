# this method works only for values < 0 and the max item is < length of the array
# it has O(N) time complexity

def find_duplicate(nums):

    for num in nums:

        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            print(f"Repetition fount: {abs(num)}")


if __name__ == '__main__':
    find_duplicate([2, 3, 4, 5, 3, 2])

