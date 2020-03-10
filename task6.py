def number():
    num = [1,2,3,4,5,6,7,8,9,10]
    odd = 0
    even = 0
    for i in num:
        if i%2 == 0 :
            even+=1
        else:
            odd+=1
    return('Четные числа %s , нечетные числа %s' % (odd,even))
print(number())