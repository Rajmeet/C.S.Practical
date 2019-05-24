n = int(input("Enter a number: "))

def count(n):
    return len(str(n))

def reverse(n):
    m = str(n)
    return(m[::-1])

def hasdigit(n):
    s = str(n)
    return s.isdigit()

def show(n):
    length = len(str(n))
    l = length - 1 
    total = ""
    i = 0
    x = True
    m = str(n)
    while x:
        num = int(m[i])*10**l
        i += 1
        l -= 1
        total += str(num)
        if l>=0:
            total = total + '+'    
        if(l < 0):
            x = False
            break

    return(total)

print(count(n))
print(reverse(n))
print(hasdigit(n))
print(show(n))