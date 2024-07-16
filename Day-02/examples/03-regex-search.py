import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

import re
text2 = "Nature is beautiful"
x = r"beautiful"
search2 = re.search(x, text2)
if search2:
    print("Pattern found:", search2.group())
else:
    print("Patter not found")


