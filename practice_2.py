# DATA TYPES

# str - string
_str = 'test'
_str2 = "tst"
_str3 = f'{_str2} test'.format(_str2=_str2)

# bool - boolean
_bool = True
_bool_false = False

# int - integer
_int = 1
_int = -1
_int_negative = -1

# float
_float = 1.0
_float_neagtive = -1.0


# list

_list = ['alex', 'grande', 'sara', 'laura', 'danielle', 'jen']
_list2 = list()

for name in _list:
        print(name)
# CASTING

output = float('1.0') + 1
output2 = '1'+ str(1)


print(output)
print(output2)

print(bool(0))
print(bool(1))
print(bool(.1))
print(bool('false'))

print(len(''))
print(len('false'))

"""
    practice: print each letter in a given string
"""

# for [variable_name] in <collection<:
# <action>
name = 'name'
for character in name:
    print(character)