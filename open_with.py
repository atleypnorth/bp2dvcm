with open("README.md") as f2:
    # automatically closed by context manager once the code exits the with block
    for line in f2:
        print(line)


f2.read()
