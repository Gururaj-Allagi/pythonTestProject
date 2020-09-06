import re

str = "gsa943@gmail.com"

r = re.search(r'.com\b', str)

print(r.group())