# A powerful number is one with at least 2 distinct prime factors and
# for every prime factor p  the number also divides p^2
def nthPowerfulNumber(n):
  found = 0
  guess = 2
  while found < n:
    guess += 1
    if isPowerfulNumber(guess):
      found += 1
  return guess

def isPowerfulNumber(n):
  count = 2
  powerC = 0
  while count**2<=n:
    if isPrime(count) and n%count==0:
      if n%(count**2) != 0:
        return False
      else:
        powerC+=1
    count+=1
  if powerC<2:
    return False
  return True

def isPrime(p):
  if p==2 or p == 3:
    return True
  if p%2==0 or p%3==0:
    return False

  n = 5
  w = 4

  while n**2 <= p:
    if p%n == 0:
      return False
    w = 6-w
    n+=w

  return True

#Sieve of Eratosthenes
def sieve(n):
  isPrime = [ True ] * (n+1) # assume all are prime to start
  if( n > 0):
    isPrime[1] = False
    
  isPrime[0] = False # except 0 and 1, of course
  primes = [ ]
  for prime in range(n+1):
    if (isPrime[prime] == True):
      # we found a prime, so add it to our result
      primes.append(prime)
      # and mark all its multiples as not prime
      for multiple in range(2*prime, n+1, prime):
        isPrime[multiple] = False
  return primes

def isPrimeWithSieve(n):
	if n in sieve(n):
		return True
	return False

for i in range(1,11):
  print nthPowerfulNumber(i)

