try:
    f = open("README.md")
    for line in f:
        print(line)
finally:
    close(f)
