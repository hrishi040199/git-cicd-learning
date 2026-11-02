

from calculations import (
    calculate_total,
    calculate_average,
    calculate_minimum
)

numbers = [100, 200, 300, 400, 500]

total = calculate_total(numbers)
average = calculate_average(numbers)
minimum = calculate_minimum(numbers)

print("Total:", total)
print("Average:", average)
print("Minimum:", minimum)
