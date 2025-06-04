# Write a Python function that takes a list of integers and returns the count of positive, negative, and zero values.


def count_pos_neg_zero(numbers):
  count_pos = 0
  count_neg = 0
  count_zero = 0

  for number in numbers:
    if number > 0:
        count_pos += 1
    elif number < 0:
        count_neg += 1
    else:
         count_zero += 1

  return count_pos, count_neg, count_zero

input_list = list(map(int, input("Enter list elements: ").split()))
pos, neg, zero = count_pos_neg_zero(input_list)

print(f"Positive integers: {pos}, Negative integers: {neg}, Zeros: {zero}")
