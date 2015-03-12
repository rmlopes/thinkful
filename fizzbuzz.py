import sys

try:
  n = int(sys.argv[1])
except:
  print 'Please provide an integer as input (eg.: python fizzbuzz.py 100)' 
  sys.exit(0)

for i in range(1, n):
  if i % 3 == 0 and i % 5 == 0:
    print 'Fizz Buzz'
  elif i % 3 == 0:
    print 'Fizz'
  elif i % 5 == 0:
    print 'Buzz'
  else:  
    print i  