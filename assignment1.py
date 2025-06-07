rows = int(input("Enter the number of rows: "))

print("Lower Triangular Pattern")
for i in range(1, rows + 1):
    print('*' * i)

print("Upper Triangular Pattern")
for i in range(rows):
    print(' ' * i + '*' * (rows - i))

print("Pyramid Pattern")
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))
