from main import Pet

garfield = Pet('Garfield', 3)
x = 1
print(f'{x}:{garfield}')
x = 2
print(f'{x}:{garfield.owner}')

garfield.set_owner('Jon')
x = 3
print(f'{x}:{garfield.owner}')

garfield.train()
x = 4
print(f'{x}:{garfield}')

# create a list with about 4 pets
pets = [garfield, Pet('Beethoven', 2), Pet('Jake', 5), Pet('Stuart', 7)]
for p in pets:
    x += 1
    print(f'\n{x}:{p}')
