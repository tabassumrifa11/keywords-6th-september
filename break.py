a = input("enter a word:")

for i in a:
    if i == 'A' or i == 'a':
        print(f"A is found at {i}")
        break

    else:
        print(f"A not found at {i}")