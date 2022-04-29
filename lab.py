print("Dheeraj Theegela")
print("E19CSE393 \n")
no = int(input("Enter a Number: "))
if no > 1:
    for i in range(2, int(no/2)+1):
        if (no % i) == 0:
            print(no, "is not a prime number")
            break
    else:
        print(no, "is a prime number")
  
else:
    print(no, "is not a prime number")
