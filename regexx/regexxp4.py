import re

txt = "the rain in spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
