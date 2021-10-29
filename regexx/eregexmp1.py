import re
txt = "the rain in spain"
x = re.search("^the.*spain$", txt)
print(x)