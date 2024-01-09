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
    n (int): Index of Fibonacci series to return. (e.g lucas(4) = 3, lucas(5) = 5)
  Returns:
    int: nth value
  '''
  if n < 1:
    print("Invalid input: 0 or negative index")
  
  elif n == 1:
    return 2
  
  elif n == 2:
    return 1
  
  else: 
    return lucas(n-1) + lucas(n-2)