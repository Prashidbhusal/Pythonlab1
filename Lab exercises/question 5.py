#4 Given the integer N- the number of minutes that is the past since midnight - how many hours and minutes displayed
#on the 24th digital clock.
N= int(input("Enter the minutes passed since midnight"))
hours=(N/60)
minutes=(N%60)
print(f"the hours is {hours} ")
print(f"the minutes is {minutes}")
print(f"Its {hours}:{minutes} now")