def fibonacci(n):
  '''
  Calculates and returns nth value in Fibonacci series.
  Parameters:
    n (int): Index of Fibonacci series to return. (e.g fibonacci(4) = 3, fibonacci(5) = 5)
  Returns:
    int: nth value
  '''
  if n < 0:
    print("Invalid input: Negative index")
  
  elif n == 0:
    return 0
  
  elif n == 1 or n == 2:
    return 1
  
  else: 
    return fibonacci(n-1) + fibonacci(n-2)
  
def lucas(n):
  '''
  Calculates and returns nth value in Lucas series.
  Parameters:
    n (int): Index of Lucas series to return. (e.g lucas(4) = 4, lucas(5) = 7)
  Returns:
    int: nth value
  '''
  if n < 0:
    print("Invalid input: 0 or negative index")
  
  elif n == 0:
    return 2
  
  elif n == 1:
    return 1
  
  else: 
    return lucas(n-2) + lucas(n-1)
  
def sum_series(n, op=0, op1=1):
  '''
  Calculates and returns nth value in either lucas or fibonacci series.
  Parameters:
    n (int): Index of the series to return. (e.g lucas(4) = 4, fibonacci(5) = 5)
    op (int): Optional. Determines which series to run.
    op1 (int): Optional. Technically does nothing right now.
  Returns:
    int: nth value
  '''
  if op == 0:
    return fibonacci(n)
  elif op == 2:
    return lucas(n)
  else: 
    print("Other series")
    return None
  


