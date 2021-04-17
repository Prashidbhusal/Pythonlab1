#Write a program to convert seconds into day, hour & minutes.

time=int(input('enter the time in second'))
minute=time/60
hour=minute/60
day=hour/24
print(f'{hour}, hour')
print(f'{minute}, minute')
print(f'{day}, day')