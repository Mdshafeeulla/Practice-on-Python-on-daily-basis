def sec_lar_correct(nums):
    if len(nums) < 2:
        return None  # Handle small lists
    largest = float('-inf')
    second_largest = float('-inf')

    for i in nums:
        if i > largest:
            second_largest = largest  # The old largest becomes the new second largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i

    return second_largest


print(f"Correct [1, 2, 3, 4, 5]: {sec_lar_correct([1, 2, 3, 4, 5])}")  # 4
print(f"Correct [10, 50, 20, 100]: {sec_lar_correct([10, 50, 20, 100])}")  # 50