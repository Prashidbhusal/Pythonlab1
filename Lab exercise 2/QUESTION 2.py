2#WAP which accepts marks of four subjects and display totalo marks, percentage and grade.
#Hint: more then 70% ->distinction, more then 60%->first, more then 40%-> pass, less then 40%-> fail.

science=int(input('enter marks of science'))
math=int(input('enter marks of math'))
nepali=int(input('enter marks of nepali'))
social=int(input('enter marks of social'))
total=(science+math+nepali+social)
percentage=(total/400)*100
print(f'total marks = {total}')
print(f'percentage is {percentage}%')
if percentage>= 70:
    print('distinction')
elif percentage<=70 and percentage>=60:
    print('first')
elif percentage<=60and percentage>=40:
    print('pass')
else:
    print('fail')