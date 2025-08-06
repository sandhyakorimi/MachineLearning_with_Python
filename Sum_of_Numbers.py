def findSum(n, k):
    val = (k//(n-1))*n
    rem = k%(n-1)
    if(rem==0):
        val = val-1
    else:
        val=val+rem
    sum = (val*(val+1)) //2 
    x=k//(n-1)
    sum_of_multiples = (x*(x+1)*n)//2
    sum-=sum_of_multiples
    return sum
n=7
k=13
print(findSum(n,k)) 