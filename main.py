n = int(input("Enter a number:"))

sumeven = 0
sumodd = 0

while n > 0:
    r = n % 10
    if r % 2 == 0:
        sumeven = sumeven + r
    else:
        sumodd = sumodd + r
    n = int(n / 10)

print("Sum of even digits:", sumeven)
print("Sum of odd digits:", sumodd)