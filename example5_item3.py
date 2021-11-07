from medspes.item3 import MergedModel

# create an object
m = MergedModel(7)

# print the current state
print('--- Initialize ---')
print(m)
# print the marking
print(m.get_marking())

# next states
m.next()
print('--- Next states ---')
print(m)
print(m.get_marking())

# next 7 states
m.advance(7)
print(m)
print(m.get_marking())
