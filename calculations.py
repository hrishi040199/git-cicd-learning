def calculate_total(numbers):
    return sum(numbers)


def calculate_average(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)