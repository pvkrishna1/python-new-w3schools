import re
txt = "the rain in spain"
x = re.sub("\s", "9", txt, 2)
print(x)