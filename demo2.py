import re

email1= "zuck26@facebook.com"   "page33@google.com"  "jeff42@amazon.com"
p=re.compile(r"([a-zA-Z0-9._]+)@([a-zA_Z]+).([com)]+)")
result1=p.findall(email1)

print(result1)