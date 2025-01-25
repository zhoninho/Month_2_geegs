def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
    return nums

def binary_search(val, arr):
    n = len(arr)
    result_ok = False
    first = 0
    last = n - 1
    pos = -1

    while first <= last:
        middle = (first + last) // 2
        if val == arr[middle]:
            result_ok = True
            pos = middle
            break
        elif val > arr[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if result_ok:
        print(f"Элемент найден на позиции {pos}")
    else:
        print("Элемент не найден")

numbers = [4,5,3,1,2]
bubble_sort(numbers)
print(numbers)
binary_search(2,numbers)


