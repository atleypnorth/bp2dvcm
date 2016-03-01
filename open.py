f = open("README.md")
for line in f:
    print(line)

# oops didnt close it ...
print('read', f.read())
