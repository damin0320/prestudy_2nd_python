example = [2, 3, 5, 7, 1]
def plus(x):
    example.append(x)
    return example

def deleting():
    example.pop()
    return example

def sorting():
    example.sort()
    return example

print(deleting())
print(plus(6))
print(sorting())