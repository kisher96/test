numbers=[1,2,3,4,5,-1,-2,-3]

result=[]
for number in numbers:
    if number > 0:
        result.append(number)

print(result)

result=filter(lambda number:number>0, numbers)
print(list(result))

result=[number for number in numbers if number if number>0]
print(result)

