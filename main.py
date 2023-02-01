# print("Happy new Year")

a = int(input("wtite 1 num"))
b = int(input("write 2 num"))
c = input("write sign")

def calc( num1 , num2 , calcu):
  if calcu == "+":
    print(num1+ num2)
  elif calcu == "-":
    print(num1 - num2)
  elif calcu == "*":
    print(num1*num2)
  elif calcu == "/":
    print(num1/num2)
  elif calcu == "*":
    print(num1**num2)
  else:
    print("А давай ще раз , мені не сподобалось!")
a = int(input("введіть число "))
b = int(input("введіть число "))
c = input("введіть дію ")
calc(a , b , c)