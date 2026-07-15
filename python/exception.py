try:
    print("enter a number to divide 10 by:")
    num = int(input())
    result = 10 / num
except ZeroDivisionError as e:
    # print("please enter a number other than zero")
    print(e)
else:
     print(f"the result is: {result}")
finally:
    print("execution completed")