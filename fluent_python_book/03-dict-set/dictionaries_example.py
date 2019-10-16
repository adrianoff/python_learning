a = {'one': 1, 'two': 2}
print(a)

DIAL_CODES = [
    (86, 'China'),
    (91, 'India')
]

country_codes = {country: code for code, country in DIAL_CODES}
print(country_codes)

###
# Update
###
country_codes.update([('key', 1)])
print(country_codes)
country_codes.update({'key': 20, 'Ukraine': 380})
print(country_codes)

country_codes.setdefault('USA', [])
print(country_codes)
country_codes.setdefault('USA', []).append('test_append')
print(country_codes)


class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()




ll = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(ll[2])

dd = {'2': 'test'}
lll = StrKeyDict0(dd)


import collections
class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.keys()

    def __setitem__(self, key, value):
        self.data[str(key)] = value

