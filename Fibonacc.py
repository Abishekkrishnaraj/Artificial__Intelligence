# Artificial__Intelligence
# Artificial_Intelligence 
 #to print the fibonacci series 
 n=int(input("enter the number=")) 
 a=0 
 b=1 
 print(a,b,end=' ') 
 c=0 
 while(n>0): 
     c=a+b 
     print(c,end=' ') 
     a=b 
     b=c 
     n=n-1
