import re
for line in open("a.txt"):
    if not re.match("abcd", line):
        print line[:-1]   