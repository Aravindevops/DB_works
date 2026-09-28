l=["red","green","orange","yellow","blue"]

def word_length(a):
    length = []
    for i in a:
        length.append(len(i))
    return length

print(word_length(l))

def square(a):
    return a**2

print(square(5))