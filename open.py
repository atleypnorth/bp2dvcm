
f = open("README.md")
for line in f:
    print(line)
# oops didnt close it ...
print('Next line : %s' % f.read())

print()

with open("README.md") as f2:
    for line in f2:
        print(line)

# automatically close by context manager once the code exits the with block

f2.read()
