import re
string="Example [for] Me7@ta Characters 456 in Regular Expressions"
res1= re.findall("a",string)
print(res1)

res2= re.findall("[a]",string)
print(res2)

res3= re.findall("^Ex",string)
print(res3)

res4= re.findall("sions$",string)
print(res4)

res5= re.findall("Exam...",string)
print(res5)

res6= re.findall("...Exam",string)
print(res6)

res7= re.findall("r*",string)
print(res7)

res8= re.findall("r+",string)
print(res8)

res9= re.findall("r{2}",string)
print(res9)

res10= re.findall(r"\s",string)
print(res10)

res11= re.findall(r"\S",string)
print(res11)

res12= re.findall(r"\d",string)
print(res12)

res13= re.findall(r"\D",string)
print(res13)

res14= re.findall(r"\w",string)
print(res14)

res15= re.findall(r"\W",string)
print(res15)

res16= re.findall(r"[12345]",string)
print(res16)

res17= re.findall(r"[0-9][0-9][0-9]",string)
print(res17)

res18= re.findall(r"[^456]",string)
print(res18)


txt = "Hello hkdbcqidebman bjwkefhvk bcwkuch Nikita dcbwjfchi Nikita "
s= re.search("Nikita", txt)
print(s)

result = re.match(r"Hello", "world Hello")
print(result)
 # Matches only if "Hello" is at the start
