#complete all methods of lists
a=[23,1,2,4,6,4,9,3,56,73]
b=[12,34,57]
a.append(7)
a
a.clear()
a
a.copy()
a
a.count(2)
a
a.extend(b)
print(a)
x=a.index(23)
print(x)
a.insert(2,6)
print(a)
a.pop(1)
print(a)
a.remove(73)
print(a)
a.reverse()
print(a)
b.sort()
print(b)


#complete all methods of strings
txt="i am beautiful"
x=txt.capitalize()
print(x)

x=txt.casefold()
print(x)

x=txt.center(30)
print(x)

x=txt.count("am")
print(x)

x=txt.encode()
print(x)

x=txt.endswith(".")
print(x)

b="h\te\tl\tl\to"
y=b.expandtabs(2)
print(y)

x=txt.find("i")
print(x)

c="my age is{age}"
print(c.format(age=" 20"))

x=txt.index("beautiful")
print(x)

x=txt.isalnum()
print(x)

x=txt.isalpha()
print(x)

x=txt.isdecimal()
print(x)

z="234453434"
d=z.isdigit()
print(d)

x=txt.isidentifier()
print(x)

x=txt.islower()
print(x)

x=txt.isnumeric()
print(x)

x=txt.isprintable()
print(x)

x=txt.isspace()
print(x)

x=txt.istitle()
print(x)

x=txt.isupper()
print(x)

l1=("u","go","outside")
l2=".".join(l1)
print(l2)

l3="drawing"
l4=l3.ljust(30)
print(l4,"is my hobby")

l5="FRIENDS"
l6=l5.lower()
print(l6)

l7=" jack "
l8=l7.lstrip()
print("hi my name is", l8, "see you tomorrow")

l10=l7.rstrip()
print("hi my name is", l10,"see you tomorrow")

l11=txt.strip()
print("hi my name is", l7,"see you tomorrow")
      
l9="hello"
mytable=l9.maketrans("h","c")
print(l9.translate(mytable))

l10=l9.upper()
print(l10)

m1="could you please go"
m2=m1.partition("please")
print(m2)

m3=m1.replace("go","come")
print(m3)

m4=m1.rfind("could")
print(m4)

m5=m1.rindex("you")
print(m5)

txt1="apple"
t1=txt1.rjust(10)
print(t1, "is in my pocket")

m6="i drink tea, tea is my favourite"
m7=m6.rpartition("tea")
print(m7)

m8="ford, BMW, kia"
m9=m8.rsplit(",")
print(m9)

m10=m6.split()
print(m10)

r1="hi,you coming home"
r2=r1.splitlines()
print(r2)

r3=r1.startswith("hi")
print(r3)

r4=t1.swapcase()
print(r4)

r5=r1.title()
print(r5)

r6="23"
r7=r6.zfill(5)
print(r7)

#3-usage of negative index
#we can use

#eg
a="welcome home"
print(a[-2:-1])
