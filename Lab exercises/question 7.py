#Solve each of the following problems using pythone script . Makes sure you use appropriate variable names and comments.
#When there is final answer , have python is to the screen.
#  A person's body mass index(BMI) is defined as:
#  BMI=(mass in kg) / (height in m)^2

mass=float(input('enter the mass of person in kg'))
height=float(input('entr the height of a person in meter'))
BMI=mass/(height ** 2)
print(f"The BMI index of the person is {BMI}")
