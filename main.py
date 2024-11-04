# Ethan Lawrence
# Oct 4 2024
# Range Challenges

# Counting Up & Down
num = int(input('please enter an intiger:   '))

for x in range(1, num + 1):
    print(x)
print('')
for x in range(num, 0, -1):
    print(x)
else:
    print('We have liftoff!')

print('')
# Number cubes
for x in range(1, 11):
    print(x**2)

print('')
# Multiplication table
num2 = 7
for x in range(1, 11):
    print(x * num2)

print('')

# List Iteration
total = 0
tens = range(10, 101, 10)
num_elements = len(range(10, 101, 10))
for i in range(num_elements):
    total += tens[i]
    
print(total)
print(sum(tens))