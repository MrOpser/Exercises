# Given an array of integers, return a new array with each value doubled.
#
# For example:
#
# [1, 2, 3] --> [2, 4, 6]

def duble_array(array: list[int]) -> list[int]:
    res_array = array
    count = 0
    for i in array:
        element = i * 2
        res_array[count] = element
        count += 1
    return print(res_array)


if __name__ == '__main__':
    duble_array([2, 3, 9, 234])




