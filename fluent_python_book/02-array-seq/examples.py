#####
##### listcomp Списковое включение
#####
symbols = '$%^&*()!@'

codes = [ord(code) for code in symbols]
print(codes)

codes = [ord(code) for code in symbols if ord(code) > 38]
print(codes)

#Декартово произведение
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirs = [(color, size) for color in colors for size in sizes]
print(tshirs)

tshirs = [(color, size) for size in sizes for color in colors]
print(tshirs)


#####
##### genexp Списковое включение
#####

symbols = '$%^&*()!@'
generator = (ord(code) for code in symbols)
print(generator)
list_from_generator = [item for item in generator]
print(list_from_generator)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for thirst in ((c,s) for c in colors for s in sizes):
    print(tshirs)
