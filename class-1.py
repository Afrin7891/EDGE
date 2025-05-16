
n = int(input("Enter an odd number n: "))

sum = 0


for i in range(1, n+1, 2):  
    sum += i**2

print("Sum of squares of odd numbers up to", n, "is:", sum)
