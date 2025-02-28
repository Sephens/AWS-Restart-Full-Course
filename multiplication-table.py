tableSize = 9

# print(" ", end="")

for col in range(1, tableSize +1):
    print(f"{col:4}", end="")

print("\n" + "_" * (4 * (tableSize + 1)))

for row in range(1, tableSize +1):
    print(f"{row:2} | ", end="")
    for col in range(1, tableSize +1):
        print(f"{row * col:4}", end="")
    print()