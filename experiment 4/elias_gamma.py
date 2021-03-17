from math import log   
log2 = lambda x: log(x, 2) 

def Unary(x): 
    return (x-1)*'0'+'1'
  
def Binary(x, l = 1): 
    s = '{0:0%db}' % l 
    return s.format(x) 

def binaryToDecimal(binary):       
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal  
      
def Elias_Gamma(x): 
    if(x == 0):  
        return '0'
  
    n = 1 + int(log2(x)) 
    b = x - 2**(int(log2(x))) 
  
    l = int(log2(x)) 
  
    return Unary(n) + Binary(b, l) 
ec=[]      
even_num = [2,4,6,8,10,12,14,16,18,20]
for i in even_num:
  ec.append(Elias_Gamma(i))
  print('Elias Gamma of '+str(i)+' : '+(Elias_Gamma(i)))

for i in ec:
  binstr = (i[i.index('1'):])
  binstr = int(binstr)
  print('Original Value of '+str(i)+' : '+str(binaryToDecimal(binstr)))
