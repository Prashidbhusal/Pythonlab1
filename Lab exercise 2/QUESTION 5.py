#IF NAME IS LESS THEN  3 CHARACTERS OTHERWISE IF IT'S MORE THEN 50 CHARACTERS - NAME MUST BE MAXIMUM OF 50
#OTHERWISE - NAME LOOKS GOOD!

name=str(input('Enter the name:'))
if (len(name))<=3:
    print('name must be 3 character')
elif len(name)>=50:
    print('name must be less then 50')
else:
    print('hamre chutiya banawe')