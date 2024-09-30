#   Recursion means returning the function to the function again.

num=int(input("Enter the factorial: "))     # creating a num integer.

def factorial(num):                 # creating a new function with parameter num

    if num == 0 or num == 1:        # if the num is 0 or 1 then the output is 1 cuz factorial of 1 and 0 is 1
        return  1

    else:
        return num * factorial(num-1)   # if num is not equal to 0 and 1 then it does recursion process so the fucntion
                                        # use the same function to repeat steps




a=factorial(num)

print(a)


#Factorial examples:
#factorial 5 = 5*4*3*2*1
#factorial 7 =7*6*5*4*3*2*1