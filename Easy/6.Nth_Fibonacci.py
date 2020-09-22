#Navie Way of solving
# O(2^n) time || O(n) space
class Solution:
    def fib(self, N: int) -> int:
        if N==2:
            return 1
        elif N==1:
            return 1
        elif N==0:
            return 0
        else:
            return self.fib(N-1) + self.fib(N-2)
        
#Using recursive but by using Dictonary we can elimnate repetion of function calls. 
# O(n) time || O(n) space
    def fib(self, N: int,memoize={0 :0,1:1,2:1}) -> int:
        if N in memoize:
            return memoize[N]
        else:
            memoize[N]=self.fib(N-1,memoize)+self.fib(N-2,memoize)
            return memoize[N]

# using Just an two digit array to save space
# O(n) time || O(1) space
def fib(self, N: int) -> int:
        if N==0:
            return 0
        elif N==1:
            return 1
        elif N==2:
            return 1
        lastTwo=[1,1]
        counter=3
        nextFib=0
        while counter <= N:
            nextFib=lastTwo[0]+lastTwo[1]
            lastTwo[0]=lastTwo[1]
            lastTwo[1]=nextFib
            counter+=1
        return nextFib
        