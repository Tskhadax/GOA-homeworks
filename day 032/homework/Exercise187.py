#Code Wars
def sum_two_smallest_numbers(numbers):
    small = []
    num = numbers[0]
    num1 = numbers[0]
    for i in numbers:
        if i < num:
            num = i
    numbers.remove(num)
    small.append(num)
    num1 = min(numbers)
    small.append(num1)
    sum = 0
    