def fact(n):
    if (n <= 1):  
     return 1
    else:
     return n*fact(n-1); 
print(fact(5))



def sumton(n):
  total = 0
  for x in range(n+1):
    total += x
  return total
print(sumton(5))

def recursive_sumton(n):
  total = 0
  if n == 1:
    return 1
  else:
    return n + recursive_sumton(n-1)
  
print(recursive_sumton(5))


import time
start_time = time.perf_counter()

def fibonacci(n):
  if n == 1:
    return 0
  elif n ==2:
    return 1
  else:
    a = [0,1]
    while len(a) !=n:
      b = list_sum(a)
      a.append(b)
      return(a[n-1])
 
  
def list_sum(lst):
  c = 0
  for item in lst:
    c += item
  return c

print(fibonacci(5))  
  

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")


        
        