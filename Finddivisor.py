
def sumDivisor(num):
    answer = 0

    for i in range(1,num+1):
        if num%i==0:
            answer += i
    return answer        

n = int(input())
print(sumDivisor(n))   