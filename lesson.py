# #variable unpacking
# colors=["white","black","blue","red","yellow"]
# a,b,c,d,e = colors

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# #output variables
# x="Ebru"
# y="Sena"
# z="Özsöğüt"
# print(x,y,z)

# a=1
# b=2
# print(a+b)

#global variiables
text = "marvellous"

def myFunction():
    global x
    x="ebru"
    print("python is : " + text)

myFunction()
print(x)