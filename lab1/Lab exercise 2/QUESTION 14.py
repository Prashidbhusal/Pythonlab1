#Give the three digit number. Find the sum of its digits
user_input=int(input('enter the three digit number '))
sum=0
while user_input>0:
    reminder=user_input
    sum=sum+reminder
    user_input=user_input//10
print('the sum of the given three number is',sum)
