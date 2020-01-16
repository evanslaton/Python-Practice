
def while_loop(n, increment_by):
  i = 0
  numbers = []

  while i < n:
    print(f"At the top i is {i}")
    numbers.append(i)
    i = i + increment_by
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
  
  return numbers

numbers = while_loop(6, 2)

print("The numbers: ")
for number in numbers:
  print(number)