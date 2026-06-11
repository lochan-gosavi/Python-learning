total = 0
number = int(input("Enter the number here : "))
while(number != 0):
    total = total + number
    number = int(input("Enter the next number here : "))
    print("Total sum : ",total)