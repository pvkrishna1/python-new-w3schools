import re
txt = "the rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
