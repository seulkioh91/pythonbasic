def search4vowels(word:str) -> set :
    ''' Return a boolean based on any vowels found'''
    vowels = set('aeiou')
    return vowels.intersection(set(word))
    '''결과값으로 셋이 나올수도 있어요!!!'''

help(search4vowels)

search4vowels('hitch-hiker')
search4vowels('galaxy')
search4vowels('life, the universe and everything')
search4vowels('sky')

l = list()
l

d = dict()
d

s = set()
s

t = tuple()
t
