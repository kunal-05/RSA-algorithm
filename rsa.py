import random
import math
import sympy

while True:
    p=int(input("Enter value of 1st prime number"))
    if((sympy.isprime(p))):
        break
    else:
        print("Please enter prime number only")

while True:
    q=int(input("Enter value of 2nd prime number"))
    if((sympy.isprime(q))):
        break
    else:
        print("Please enter prime number only")
n=p*q
fn=(p-1)*(q-1)
print("Value of ϕ:",fn)

a=[]
value=[]
# e calculation
for i in range(2,fn):
    g=math.gcd(i,fn)
    if(g == 1):
        a.append(i)
print(a)
e = random.choice(a)
print("e:",e)

#d calculation
e=e%fn
d=0
for i in range(1,fn):
	if(((i*e)%fn)==1):
		d=i
print("d is:",d)
print("Public key(n,e):",n,e)

#encryption
messagetext=input("Enter your message")
    
for i in range(len(messagetext)):
    k=ord(messagetext[i])
    print(k)
    value.append((k**e)%n)
   
print("Ciphertext:",value)

#decryption
message=[]
messageori=[]
print("Private key:",n,d)
for i in range(len(value)):
    message.append((value[i]**d)%n)

print("Decrypted message is:",message)
for i in range(len(value)):
    z=chr(message[i])
    messageori.append(z)
print("Original message after decryption:",' '.join(messageori)) 


