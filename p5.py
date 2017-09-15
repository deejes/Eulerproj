#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def is_prime(num):
    x = num - 1
    while x > 1:
        if num % x == 0:
            return False
            break
        else:
            x = x - 1
    return True

def factor(num):
    #returns a list with prime factors of the argument
    factors = []
    x = num - 1
    if is_prime(num):
        factors.append(num)
    else:
        while num != 1:
            if num % x == 0 and is_prime(x):
                num = num / x
                factors.append(x)
            else:
                x = x - 1
    return factors

def union(master,append):
    # takes two lists as input. modifies the first to include any elements in list 2 
    #but not list1. Also equalizes occurences of any elements in both lists, to the level of list 2
    for x in append:
        if x not in master:
            master.append(x)
        else:
            if append.count(x)>master.count(x):
                while append.count(x) > master.count(x):
                    master.append(x)
x = 20
result = []
while x > 2:
    union(result,factor(x))
    x = x - 1
    
answer = 1
for x in result:
    answer = answer * x

print (answer)
