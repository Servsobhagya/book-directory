#Extract the followings from given Problem
import re

email1= "zuck26@facebook.com"   "page33@google.com"  "jeff42@amazon.com"
p=re.compile(r"([a-zA-Z0-9._]+)@([a-zA_Z]+).([com)]+)")
result1=p.findall(email1)

print(result1)


#Extract the Words Starting from b And B
import re
text="Betty bought a bit of butter , but the butter was so better , so she bought some butter , To make the bitter butter bitter "
pe=re.compile(r"([bB][A-zA-Z]+)")
result=p.findall(text)
for x in result:
 print(x)
#Split the Following Irregular Sentence into Words
import re

sentence="A,very very; irregular_sentence"
p=re.sub(r"[^a-zA-Z]"," ",sentence)
print(p)
#Optional Question
import re

tweets=tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats''' 

p=re.compile(r"(.+) RT (.+): (.+) http(.+)")
res=p.findall(tweets)
print(res[0][0],res[0][2])
print("\n")


