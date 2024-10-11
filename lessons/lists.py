"""test_list: list[str] = ["one", "two"]

print(test_list[2])"""

x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0
print(x)
