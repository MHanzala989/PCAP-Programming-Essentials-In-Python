#using while loop
#can be done using for loop
def is_prime(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False 
        i += 1
    return True

for i in range(1, 30):
    if is_prime(i + 1):
        print(i + 1, end=" ")
###############################################################################
#uing for loop
def is_Prime(x):
    if x < 2: return False
    for i in range(2, x):
        if x%i==0:
            return False
    return True

#print("Enter a Number: ", end="")
#n = int(input())
for n in range(20):
    if is_Prime(n):
        print(n)
