def factorial(n):
  if n==0 or n==1:
      return 1

  result = factorial(n-1) *n
  return result

print(factorial(3))
