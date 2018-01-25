import sys

_message = sys.argv[0]

_str = 'this is a str'
_str_2 = 'this is a str'

message =('hello world')

print('hello world')

print (message)


"""
  print each letter in a given string
"""

message = "programming 101"

# brute force
print('p')
print('r')
print('o')
print('g')
print('r')
print('a')
print('m')
print('m')
print('i')
print('n')
print('g')
print(' ')
print('1')
print('0')
print('1')

print ('-----')

# for <variable_name> in <collection>:
#   <action>

for letter in message:
    print(letter)

counts = [1,2,3,4,5,6,7,8]

for count in counts:
    print(count)

"""
  practice: print true or false if a letter exists in a given str
"""

search_value = 'e'
message = 'hello world'

if search_value in message:
    print(True)
else:
    print(False)


find_l