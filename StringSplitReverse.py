#Python Strings: Replace, Join, Split, Reverse, Uppercase & Lowercase

x="Hello world"

#[]-Slice- it gives the letter from the given index

#[:]-Range slice-it gives the characters from the given range

print(x[:6])
print(x[0:6] + "Guru99")
#in-Membership-returns true if a letter exist in the given string
print("u" in x)
#not in -	Membership-returns true if a letter exist is not in the given string
print("u" not in x)
#r/R-Raw string suppresses actual meaning of escape characters.
#adding
name = 'guru'
number = 99
print ('%s %d' % (name,number))
#adding
x="Guru"
y="99"
print (x+y)
#repeat
print(2*x)
#replace
oldstring = 'I like Guru99'
newstring = oldstring.replace('like', 'love')
print(newstring)
#UpperCase-upper
a="python at guru99"
print(a.upper())
#capitalize-capitalize
b="python at guru99"
print(b.capitalize())
#lowercase-lower
c="PYTHON AT GURU99"
print(c.lower())
#join function
print(":".join("Python"))
#reverse string
string="12345"
print(''.join(reversed(string)))
#split
word="guru99 career guru99"
print(word.split(' '))
print(word.split('r'))
x = "Guru99"
x.replace("Guru99","Python")
print(x)
x = x.replace("Guru99","Python")
print(x)