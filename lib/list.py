# list
sopranos = ['Tony', 'Carmella', 'Meadow', 'AJ']

print(sopranos)
print(sopranos[0])

sopranos[3] = 'Anthony Jr'
print(sopranos[3])

for member in sopranos:
    print('Member: ', member)

if 'Tony' in sopranos:
    print('Tony is still with us!')

print('There are ' + str(len(sopranos)) + ' members in the Soprano family')

sopranos.append('Kelly')

if 'Kelly' in sopranos:
    print("Where's Tony B?")

sopranos.remove('Kelly')

print(sopranos)

# Man in members only jacket
del sopranos[0]

print(sopranos)

print("You probably don't even hear it when it happens, right?")

sopranos.clear()
