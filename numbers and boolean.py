#numbers and boolean 
x=10     #int
y=12.36  #float
z=3+2j   #complex
is_valid=True #bool

#random number ex: OTP
import random #import random library
no=random.randrange(100,500)
print(no)

#casting
#used to change variable type 
# can change all int to str but not vise versa
x=50
y=str(x)
print(y) #50 (in type str)

x='hulk' # can't change to int
x='7'    #7 (in type int)
x=7
y=float(x)  #7.0
y=complex(x)#7+0j


