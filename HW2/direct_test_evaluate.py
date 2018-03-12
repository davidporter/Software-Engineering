from evaluate import parse_integer
i = 100
print('\nTest #1')
print('supplied %d should print /"99 bottles to go/" and return 100' %i)
print(parse_integer(100))
parse_integer(100)
print('\nTest #2')
print("Parse integer 99 test (should simply return 99):")
print(parse_integer(99))