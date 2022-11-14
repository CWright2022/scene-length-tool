import re
string="i’m"
regex=".*i'm.*"
if re.match(string,regex, flags=re.IGNORECASE):
    print("YES")
else:
    print("NO")