
#Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.#
import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
sum_of_a

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
min_of_a
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
max_of_a
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a) / len(a)
mean_of_a
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = (1*2*3*4*5*6*7*8*9*10)
 
product_of_a
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = []
for i in a:
    squares_of_a.append(i*i) 

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = []
for i in a:
    if i % 2 != 0:
        odds_in_a.append (i)
odds_in_a
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = []
for i in a:
    if i % 2 == 0:
        evens_in_a.append (i)
evens_in_a
## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
import numpy as np
b = [
    [3, 4, 5],
    [6, 7, 8] ]
np.array(b)
# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
sum_of_b

import numpy as np

b = np.array(b)
sum_of_b = np.sum(b)

sum_of_b
# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1]) 


b = np.array(b)
min_of_b = np.min(b[:2])
min_of_b
# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

max_of_b = np.max(b[:2])
max_of_b
# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number 

product_of_b = np.prod(b)
product_of_b
# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
b = np.array(b)
## squares_of_b = np.square(b).flatten().tolist()
## squares_of_b
b **2
# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
odds_in_b = b[b % 2!= 0].tolist()

odds_in_b
# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

b = np.array(b)
evens_in_b = b[b % 2 == 0].tolist()
evens_in_b

# Exercise 9 - print out the shape of the array b.
print(b.shape)

# Exercise 10 - transpose the array b.
b = np.array(b)
b_transpose = np.transpose(b)
print(b_transpose)

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b.flatten()
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b_reshape = b.reshape((6, 1)).tolist()
print(b_reshape)
## Setup 3
import numpy as np
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

np.array(c)
# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c = np.array(c)
c_min = np.min(c)
c_max = np.max(c)
c_sum = np.sum(c)
c_product = np.prod(c)
print("Minimum:", c_min)
print("Maximum:", c_max)
print("Sum:", c_sum)
print("Product:", c_product)
# Exercise 2 - Determine the standard deviation of c.
c.std()
# Exercise 3 - Determine the variance of c.
c = np.array(c)
c_variance = np.var(c)
print("Variance:", c_variance)
# Exercise 4 - Print out the shape of the array c
print(c.shape)
# Exercise 5 - Transpose c and print out transposed result.
c_transpose = np.transpose(c)
print(c_transpose)
# Exercise 6 - Get the dot product of the array c with c. 
c = np.array(c)
c_dot_product = np.dot(c, c)
print("Dot product:", c_dot_product)
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
c = np.array(c)
c_times_c_transposed = np.dot(c, c_transpose)
c_times_c_transposed_sum = np.sum(c_times_c_transposed)
print("Sum of c times c transposed:", c_times_c_transposed_sum)

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
c = np.array(c)
c_times_c_transposed = np.dot(c, c.T)
c_times_c_transposed_product = np.prod(c_times_c_transposed)
print("Product of c times c transposed:", c_times_c_transposed_product)

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d
d = np.array(d)
sine_of_d = np.sin(d)
print("Sine of d:")
print(sine_of_d)

# Exercise 2 - Find the cosine of all the numbers in d

d = np.array(d)
cosine_of_d = np.cos(d)
print("Cosine of d:")
print(cosine_of_d)

# Exercise 3 - Find the tangent of all the numbers in d
d = np.array(d)
tangent_of_d = np.tan(d)
print("Tangent of d:")
print(tangent_of_d)
# Exercise 4 - Find all the negative numbers in d
d = np.array(d)
negative_numbers_in_d = d[d < 0]
print("Negative numbers in d:")
print(negative_numbers_in_d)
# Exercise 5 - Find all the positive numbers in d

d = np.array(d)
positive_numbers_in_d = d[d > 0]
print("Positive numbers in d:")
print(positive_numbers_in_d)
# Exercise 6 - Return an array of only the unique numbers in d.
unique_numbers = np.unique(d)
unique_numbers
# Exercise 7 - Determine how many unique numbers there are in d.
num_unique_numbers = len(np.unique(d))
num_unique_numbers
# Exercise 8 - Print out the shape of d.
print(d.shape)
# Exercise 9 - Transpose and then print out the shape of d.
d_transpose = d.T
print(d_transpose.shape)
# Exercise 10 - Reshape d into an array of 9 x 2
d_reshape = d.reshape(9, 2)