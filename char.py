'''uppercase character'''
# ch=input("enter a characters:")
# if 'A'<=ch<='Z':
#     print("upper case",ch)
# else:
#     print("not a uppercase",ch)
    
'''lowercase characters'''
# ch=input("enter a characters:")
# if 'a'<=ch<='z':
#     print("lowercase",ch)
# else:
#     print("not a lowercase",ch)
    
'''digits'''
# ch=input("enter a characters:")
# if '0'<=ch<='9':
#     print("digits",ch)
# else:
#     print("not a digits",ch)
    

    
'''all characters'''
# ch=input("enter a characters:")
# if 'A'<=ch<='Z' or 'a'<=ch<='z' or '0'<=ch<='9':
#     print("special characters",ch)
# else:
#     print("not a special characters",ch)
    
'''check whether the given character is digit or not if digit then print ASCII values'''
# ch=input("enter a character:")
# if '0'<=ch<='9':
#     print(ord(ch),ch)
    
# ch=input("enter a character:")
# if 'A'<=ch<='Z':
#     print(ord(ch),ch)
    
# ch=input("enter a character:")
# if 'a'<=ch<='z':
#     print(ord(ch),ch)

'''check whether the given input character is alphabet.
if alphabet then print ASCII value.
if digit then display next character 
if special character store it in list'''

# ch=input("enter a character:")
# if 'A'<=ch<='Z' or 'a'<=ch<='z':
#     print(ord(ch),ch)
# elif '0'<=ch<='9':
#     a=chr(ord(ch)+1)
#     print(ch,a)
# else:
#     l=[]
#     l.append(ch)
#     print(l)
    
'''coverting uppercase to lowercase'''   
# ch=input("enter a character:")
# if 'A'<=ch<='Z':
#     print(chr(ord(ch)+32))
# elif 'a'<=ch<='z':
#     print(chr(ord(ch)-32))
# else:
#     print("character is not an alphabet")

'''Guess the number'''
# import random
# secret=random.randint(1,20)
# Guess=56
# count=0
# print("Welcome to number Guessing Game")
# while Guess!=secret:
#     Guess=int(input("Guess a number:"))
#     count+=1
#     if Guess==secret:
#         print("Hurry!! You won the game in",count,"chances")
#         break
#     elif Guess<secret:
#         print("Too low")
#     else:
#         print("Too high")


'''Create a Password '''
password="Prathu"
user_password="prathyusha"
while user_password!=password:
    user_password=input("enter your password:")
    if user_password==password:
        print("Login successfully")
        break
