"""Generic formatting for python strings."""
a = 2 / 3
print("{}".format(a))
print("{:.2f}".format(a))
# If need to print multiple variables
formatter = "{:.5f}"
print(formatter.format(a))
