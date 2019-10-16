a = {'one': 1, 'two': 2}
print(a)

DIAL_CODES = [
    (86, 'China'),
    (91, 'India')
]

country_codes = {country: code for code, country in DIAL_CODES}
print(country_codes)

###
### Update
###
country_codes.update([('key', 1)])
print(country_codes)
country_codes.update({'key': 20, 'Ukraine': 380})
print(country_codes)

country_codes.setdefault('USA', [])
print(country_codes)
country_codes.setdefault('USA', []).append('test_append')
print(country_codes)
