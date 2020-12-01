#declare a variable
a=100
print(a)
#redeclare variable
a='guru99'
print(a)
#different types cannot be combined
#print("guru"+99)
b="guru"
print(a+b)
print("##########################1 #declare a variable end###############################")



#global vs local variable in funtion
f=101
def somefunction():
#local variable f defined within a function
 f="I am learning Python"
 print(f)
somefunction()
print(f)
print("##########################2 #global vs local variable in funtion end###############################")


#keyword global
f=101
print(f)
def somefunction():
    global f
    f = "hi i'm kavuri"
    print(f)
  #  f="hi i'm kavuri"
somefunction()
print(f)
print("##########################3 keyword global end###############################")

#delete variable

f=1
print(f)
del(f)
print(f)
print("##########################4 #delete variable end###############################")


