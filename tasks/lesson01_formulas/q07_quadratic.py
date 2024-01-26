# solve quadratic equation
# inputs
import math

a = 1
b = 5
c = 2

sqrt_result = math.sqrt(math.pow(b, 2) - 4 * a * c)
result = (-b + sqrt_result ) / (2 * a)

print('result = ', result)