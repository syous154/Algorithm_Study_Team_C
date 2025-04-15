n = int(input())

if n == 3:
    answer = 1
elif n == 4:
    answer = -1
else:    # n >= 5
    a = n//5
    b = (n-5*a)
    if b%3==0:
        answer = a+b/3
    else:
        while a > 0:
            a -= 1
            if (n-5*a)%3==0:
                answer = a+(n-5*a)/3
                break
            else:
                answer = -1    
print(int(answer))  