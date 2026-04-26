# trim extra whitespace
import re

mystring = "The   fox jumped   over    the log."

print(re.sub(" +", " ", mystring))
