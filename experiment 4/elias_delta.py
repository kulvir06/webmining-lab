import math

def gamma(t):
    x=[];
    y=[];
    while(t>0):
        x.append(t%2);
        t=int(t/2);
    for i in range(len(x)-1):
        y.append(0);
    for i in range(len(x)):
        y.append(x.pop());
    return y;
 
even_num = [2,4,6,8,10,12,14,16,18,20]
ed = []
for x in even_num:
 temp = str(x)  
 t=math.floor(1+math.log(x,2));
 p=gamma(t);
 y=[];
 while(x>0):
     y.append(x%2);
     x=int(x/2);
 y.pop();
 for i in range(len(y)):
     p.append(y.pop());
 a=''.join(map(str,p));
 ed.append(a)
 print('Elias Delta Code of '+temp+' : '+a)

 def decode(x):
    num=0;
    for i in range(len(x)):
        num+=(int(x[len(x)-1-i])*(math.pow(2,i)));
    return num;

for x in ed:
 if(x=='1'):
     print('1');
     exit;
 else:
     x=list(x);
     t=0;    
     v=[];
     b=0;
     w=[];
     c=0;
     for i in x:
         if(b!=1):
             if(i=='0'):
                 t+=1;
             else:
                 v.append(i);
                 b=1;
         elif(c!=1):
             if(t==0):
                 c=1;
                 w.append('1');
                 w.append(i);
             else:
                 v.append(i);
                 t-=1;
         else:
             num=decode(v);
             if(num==0):
                 break;
             else:
                 w.append(i);
                 num-=1;
     ans=decode(w);
     print('Original Number: ',int(ans));
