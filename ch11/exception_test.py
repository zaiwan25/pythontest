class UppercaseException(Exception):
    pass

words = ['e', 'a', 'b', 'D']
for word in words:
    print(word)
    if word.isupper():
        raise UppercaseException(word)