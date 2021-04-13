#Given positive real number , print its fractional part.
import math
user_input=float(input('enter the number'))
fractional_part=math.modf(user_input)
print(fractional_part)
