numbers=[1,5,2,6,3,7,4,8,]
print(sorted(numbers))

print(sorted(numbers, reverse=True))

names=['Max','Kate','Rom']
print(sorted(names))


cities=[('Москва', 1000), ('Лас-Вегас', 500), ('Зилаир', 2000)]
print(sorted(cities))


def by_count(city):
    return city[1]

print(sorted(cities, key=lambda city: city[1]))
