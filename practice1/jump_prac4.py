def getTotalPage(m, n):
    
    result = int(m/n)
    if m%n !=0:
        result += 1

    return result

print(getTotalPage(107, 10))