#regular expression assignment
import re
actual = open("actual.txt", "r")
summation = 0
for line in actual:
    list_of_int = re.findall('[0-9]+', line)
    list_of_int = list(map(int, list_of_int))
    for integer in list_of_int:
        summation += integer
print(summation)

