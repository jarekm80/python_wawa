print()
print(1, 2, "23", sep="-", end="---")
print(1, 2, "23", sep="-",)
x = 10
print("-", f"{x:15}", "-")

print(list(range(10)))
print(range(10))

print("   ")
for i in range(1,9):
    print(f"{i:4}", end="")
#    for j in range(1,9):
#        print(i * j)


"""
    1  2  3  4  5

1   1  2  3  4  5
2   2  4  6  8  10
3   3  6  9  12 15 
...

"""