import re
string = "I’m seven, or s"
regex=".*i'm.*"
if re.match(string,regex, flags=re.IGNORECASE):
    print("YES")
else:
    print("NO")