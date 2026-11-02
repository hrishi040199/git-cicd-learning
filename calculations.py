def calculate_total(numbers):
    return sum(numbers)


def calculate_average(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)

def find_maximum(numbers):
    if not numbers:
        return None

    return max(numbers)

def find_duplicates(numbers):
    duplicates = []

    for number in numbers:
        if numbers.count(number) > 1 and number not in duplicates:
            duplicates.append(number)

    return duplicates

def calculate_minimum(numbers):
    if not numbers:
        return None

    return min(numbers)
