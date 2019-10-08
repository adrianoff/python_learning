coords = (33.333, 444.222)
lat, _ = coords
print(lat)


print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))

a = 1
b = 2

b, a = a, b
print(a, b)



a, b, *rest = range(5)
print(a, b, rest)

a, *rest, b = range(5)
print(a, b, rest)


metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),  # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  # <2>
    if longitude <= 0:  # <3>
        print(fmt.format(name, latitude, longitude))



#####
##### Named tuple
#####

from collections import namedtuple
City = namedtuple('City', ['name', 'population', 'coords'])
tokyo = City('Tokyo', 36.933, (33.333, 112.22))
print(tokyo)
print(tokyo.population)

print(tokyo._fields)
kyiv_list = ['Kyiv', 36.933, (33.333, 112.22)]
kyiv = City._make(kyiv_list)
print(kyiv)
print(kyiv._asdict())