rows = int(input("Enter the number of rows:"))
columns = int(input("Enter the number of columns:"))

print("Indexes of matrix:")
for i in range(rows):
    for j in range(columns):
        print(i, j, sep=",", end=" ")
    print()
