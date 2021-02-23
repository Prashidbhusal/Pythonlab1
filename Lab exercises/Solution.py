#3 N students take K apple and distribute them among each other evenly. The remaining (the undivisible) part remains in
#the basket . How many apples will each single student get? How many apples remain in the basket? The program reads the
#number N and K. It should print the two answers for the question above.

N=int(input("enter the number of students in class:"))
A=int(input("enter the number of apple:"))
D=(A//N)
R=(A%N)
print(f"each student got {D} ")
print(f"the remaining apples are {R} ")