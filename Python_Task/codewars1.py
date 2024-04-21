def sum_two_smallest_numbers(numbers:list):
    numbers.sort()
    return numbers[0]+numbers[1]

print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))