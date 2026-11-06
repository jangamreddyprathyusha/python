#Implicit conversion
a=10.2
b=8
c=(2)
print(type(c))
c=a+b
print(type(c))

#Explicit conversion
a=10
print(type(a))
b=str(a)
print(type(a))

#All 24 combinations of type conversion
#int to float
a=float(10)
print(type(a))

#int to str
a=str(10)
print(type(a))

#int to bool
a=bool(10)
print(type(a))

#int to complex
a=complex(10)
print(type(a))

#float to int
a=int(10.5)
print(type(a))

#int to int
a=int(70)
print(type(a))

# float to str
a=str(10.5)
print(type(a))

#float to bool
a=bool(10.5)
print(type(a))

#float to complex
a=complex(10.5)
print(type(a))

#float to float
a=float(10.5)
print(type(a))

#str to int
a=int("10")
print(type(a))

#str to float
a=float("10.5")
print(type(a))

#str to bool
a=bool("")
print(type(a))

#str to complex
a=complex("3+6j")
print(type(a))

#bool to int
a=int(True)
print(type(a))

#bool to float
a=float(True)
print(type(a))

#bool to str
a=str(True)
print(type(a))

#bool to complex
a=complex(True)
print(type(a))


