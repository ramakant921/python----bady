# f = open("file.txt")
# print(f.read())
# f.close()

# Same can be written using With statement like this:
with open("file.txt") as f:
    print(f.read())

# You don't have to explicitly close the file