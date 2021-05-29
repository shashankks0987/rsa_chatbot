import random
def rsa1():
    lowPrimes =   [3,7,13,17,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
                   ,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,
                   181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
                   ,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367
                   ,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461
                   ,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571
                   ,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661
                   ,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773
                   ,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883
                   ,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
    
    p=random.choice(lowPrimes)
    q=random.choice(lowPrimes)
    while(q==p):
        #p=random.choice(lowPrimes)
        q=random.choice(lowPrimes)
    public_key1=p*q

    phi=(p-1)*(q-1)
    
    e=3
    while(e<phi):
      if(gcd(e,phi)==1):
          break
      else:
        e+=1
    
   # k=random.randint(2,10)
    #k=2
    
    private= modinv(e,phi)
    
   # private_key= (k*phi + 1) / e
    return [private, public_key1 , e]

def encrypt(publickey ,data):
  pu= publickey.find('0')
  e=int(publickey[:pu])
  publickey1=int(publickey[pu+1:])
  numbers = [ord(letter) for letter in data]  #converting alphabets to numbers
 
  encypted_data = ""
  for mes in numbers:
    encypted_data= encypted_data + " " +str((pow(mes,e) %  (publickey1)))
  return encypted_data
def decrypt(private, publickey,ciphertext ):
  s= str()
  for i in ciphertext:
      k = int(i)
      decrypt = pow(k,private) % publickey
      s= s + chr(decrypt)
  return s
def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a)
def lcm(a,b):
   return (a*b) / gcd(a,b) 
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


#lis = rsa1()
#print(lis)
#f= encrypt(lis[1] , lis[2] , "n hello hi , how are toy im finw")
#d= f.strip()
#d= f.split(" ")
#print(d)
#for i in f:
#print(decrypt(lis[0],lis[1],d))
    