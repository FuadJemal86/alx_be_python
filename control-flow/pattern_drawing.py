pattern = int(input("Enter the size of the pattern: "))

if pattern > 0:
    i = 1
    while i <= pattern:
        print("*" * i)
        i += 1
else:
    print("Please enter a positive number.")
