def fib(a = 0, b = 1): 
  print(a)
  c = a + b
  if c > 100:
    return

  return fib(b, c)

fib()

