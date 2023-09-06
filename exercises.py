# TASKS
## Task 1: Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

### Task 1: Option 1
import re
string1 = input("Enter the string 'Abcd1234': ", )
print(re.search("[a-z[A-Z][0-9]", string1))

### Task 1: Option 2
import re
string2 = input("Enter the string 'A*d%23#{': ", )
print(re.search("[a-z[A-Z][0-9]", string2)) # * % # } are not included in the string. 

## Task 2: Write a Python program that matches a string that has an a followed by zero or more b's.(*)
import re
string = input("Enter the text 'foobar': ", )
print(re.search("[b*]", string))

## Task 3:  Write a Python program that matches a string that has an a followed by one or more b's. (+)
import re
string = input("Enter the text 'my-foobar': ", )
print(re.search("[b+]", string))

## Task 4: Write a Python program that matches a string that has an a followed by zero or one 'b'. (?)

import re
string = input("Enter the text 'your-foobar': ", )
print(re.search("[b?]", string))

## Task 5: Write a Python program that matches a string that has an a followed by three 'b'. {}

import re
string = input("Enter the text 'abbbbcd': ", )
print(re.search("b{3}", string))

### Task 6: Write a Python program that matches a string that has an a followed by two to three 'b'.{}
import re
string = input("Enter the text 'bbc abbbbcd': ", )
print(re.search("b{2,3}", string))

### Task 7: Write a Python program to find sequences of lowercase letters joined by an underscore. []
import re
string = input("Enter the text 'bbc_abbbbcd': ", )
print(re.search("[a-z]+$", string))

### Task 8: Write a Python program to find the sequences of one upper case letter followed by lower case letters. []
import re
string = input("Enter the text 'Abbc_Abbbbcd': ", )
print(re.search("[A-Z]+[a-z]+$", string))

### Task 9: Write a Python program that matches a string that has an 'a' followed by anything ending in 'b'. []
import re
string = input("Enter the text 'abbbb': ", )
print(re.search("[a+][b$]", string))

### Task 10: Write a Python program that matches a word at the beginning of a string. ^
import re
string = input("Enter the text 'abc': ", )
print(re.search("^a", string))

### Task 11: Write a Python program that matches a word at the end of a string, with optional punctuation. $

import re
string = input("Enter the text 'The quick brown fox jumps over the lazy dog': ", )
print(re.search("\w+$", string))

### Task 12: Write a Python program that matches a word containing 'z'. 

import re
string = input("Enter the text 'The quick brown fox jumps over the lazy dog': ", )
print(re.search("z+\w*", string))

### Task 13: Write a Python program that matches a word containing 'z', not the start or end of the word.

import re
string = input("Enter the text 'The quick brown fox jumps over the lazy dog': ", )
print(re.search("z+\w^$", string))

### Task 14: Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re
string = input("Enter the text '3_college_boys_Tom_Bob_and_Peter_are_friends': ", )
print(re.search("^[a-zA-Z0-9_]*$", string))

### Task 15: Write a Python program that starts each string with a specific number.

import re
string1 = input("Enter the text '5 Apples': ", )
string2 = input("Enter the text '5 kg Grapes': ", )
print(re.search("^5", string1 and string2))

### Task: Write a Python program to remove leading zeros from an IP address.

import re
string = input("Enter IP address '216.08.094.196': ", )
print(re.sub("\.[0]*", ".", string ))