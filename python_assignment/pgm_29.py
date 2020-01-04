# 30. Given 2 strings, write regular expression to match those strings

import re
batRegex = re.compile(r'python')
m = batRegex.search('The Adventures of python')
print(m.group())