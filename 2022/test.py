test = {'a'}

try:
    test.remove('b')
except:
    try:
        test.remove('a')
    except:
        pass

print(test)