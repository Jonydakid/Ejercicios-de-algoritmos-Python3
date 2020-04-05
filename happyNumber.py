def hSum (n:int)-> int:
        sum=0
        while n!=0:
            i=n%10 #Rescato el primer digito
            n = int(n / 10) #Lo saco del valor total
            sum+= i*i # Se suma los cuadrados del dígito
        print(sum)
        return sum
class Solution:
    def isHappy(self, n: int) -> bool:
        x=[]
        for i in range(10):
            if n==1:
                return True
            n=hSum(n)
            if x.count(n)==1:
                return False
            
            x.append(n)
                
      