def factorial(x):
  for i in range(x-1,0,-1):
    product=x*i
    factorial(product)

  return product

num=int(input("Enter a number : "))
result=factorial(num)

print("Factorial of ",num,"is : ",result)