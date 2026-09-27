str1 = "Hello"
name =input("Enter your Name: ")
str2 =str1 +" " + name
print(str2)
str3 =",Welcome to Python Programming" 
str2 =str2 + str3
print(str2)

# Question 2  String Slicing And Indexing
###############################################

str1 = "Hello Farsana welcome to Python programming"

# a. First character
print("First character:", str1[0])

# b. Last character
print("Last character:", str1[-1])

# c. First 5 characters
print("First 5 characters:", str1[:5])

# d. Last 11 characters
print("Last 11 characters:", str1[-11:])

# e. Reverse the string
print("Reverse:", str1[::-1])

# f. Print Python using slicing
print("Python:", str1[25:31])

# Question 3 string methods
###################################

strM = "Python beginner tutorial"

# a. Convert to uppercase
print("Uppercase:", strM.upper())

# b. Convert to lowercase
print("Lowercase:", strM.lower())

# c. Capitalize
print("Capitalize:", strM.capitalize())

# d. Count character 't'
print("Number of 't':", strM.count("t"))

# e. Replace Python with Machine Learning
print("Replace:", strM.replace("Python", "Machine Learning"))

#  Question 4 TUPLES 
#########################

t1 = (10, 20, 30)
t2 = (40, 50, 60)

# a. Concatenate the two tuples
t_combine = t1 + t2
print("Combined tuple:", t_combine)

# b. Repeat t_combine 3 times
t_repeat = t_combine * 3
print("Repeated tuple:", t_repeat)

# c. Access the 3rd element
print("3rd element:", t_combine[2])

# d. Access first three elements
print("First three elements:", t_combine[:3])

# e. Access last three elements
print("Last three elements:", t_combine[-3:])


