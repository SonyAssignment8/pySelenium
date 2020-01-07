#Given 2 strings, write regular expression to match those strings
import re
s1="Bangalore"
s2="Bangalore"
result=re.match(s1,s2)
if result:
    print("The string matches")
else:
    print("The string doesnot match")
