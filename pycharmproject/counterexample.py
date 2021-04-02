from collections import Counter
c = Counter('abcdeabcdabcaba')
# most_common(n)
# This method returns the most common elements from the counter.
# If we don’t provide value of ‘n’ then sorted dictionary is returned from most common the least common elements.
# We can use slicing to get the least common elements on this sorted dictionary.

print(c.most_common())

# three most common elements
print(c.most_common(3))

# list all unique elements
print(sorted(c))

print(' '.join(sorted(c.elements())))  # list elements with repetitions

print("total of all counts")
print(sum(c.values()))

print("count of letter a")
print(c['a'])

#update counts from an iterable
for elem in 'sazam':
    c[elem]+=1

print(c['a'])

print("#remove all b")
del c['b']
print(c['b'])

print("#make another counter")
d=Counter('simsalabim')
c.update(d)
print(c['a'])

# elements()
# This method returns the list of elements in the counter. Only elements with positive counts are returned.

counter = Counter({'Dog': 2, 'Cat': -1, 'Horse': 0})

# elements()
elements = counter.elements()# doesn't return elements with count 0 or less

print(elements)
for value in elements:
    print(value)

print("clear counter")
c.clear()
print(c)

# Note:  If a count is set to zero or reduced to zero, it will remain
#     in the counter until the entry is deleted or the counter is cleared:

#output
# [('a', 5), ('b', 4), ('c', 3), ('d', 2), ('e', 1)]
# [('a', 5), ('b', 4), ('c', 3)]
# ['a', 'b', 'c', 'd', 'e']
# a a a a a b b b b c c c d d e
# total of all counts
# 15
# count of letter a
# 5
# 7
# #remove all b
# 0
# #make another counter
# 9
# <itertools.chain object at 0x0000016D85709608>
# Dog
# Dog
# clear counter
# Counter()
