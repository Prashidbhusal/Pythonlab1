#2 Write a program that reads the length of the base and the height of a right-angled tringle and prints the area.
# Every number is given on a separete line.

length=int(input("enter the value of length: "))
height=int(input("enter the height: "))

area=(length * height)//2

#the floor division // rounds that result down to the nearest whole number

print(f"The area of right angled triangle is {area} ")
