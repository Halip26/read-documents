# Refactored code
with open("check.txt", "r") as f:
    print(f.read())

with open("check2.txt", "w") as f:
    f.write("Now the new file is there. With information")

with open("check2.txt", "r") as f:
    print(f.read())

with open("check2.txt", "a") as f:
    f.write("Now the new file is there. We are appending text in file.")

with open("check2.txt", "r") as f:
    print(f.read())

with open("check.txt", "r") as f:
    print(f.readline())
    print(f.readline())

with open("check.txt", "r") as f:
    print(f.readlines())

with open("the results.txt", "x"):
    pass
