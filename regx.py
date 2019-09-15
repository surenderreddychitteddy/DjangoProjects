import re

s="Python is a multi-paradigm programming language. Meaning, $ it || supports $ different programming approach One || of the popular approach to solve a programming problem is by creating objects. This is known as Object-Oriented Programming (OOP)"

s1=re.findall("\\$(.*?)\\|\\|",s)
for i in s1:
	print("$"+i+'||')

#s1=re.search("p",s,re.MULTILINE)

print(s1)

#The match function is used for finding matches at the beginning of a string only.

#The search() function searches the string for a match, and returns a Match object if there is a match.

#If there is more than one match, only the first occurrence of the match will be returned:

#it finds all occurrences of a pattern in a string
