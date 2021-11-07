from medspes.item1 import Specialist

# create an object
s = Specialist()

# print the current state
print('--- Initialize ---')
print(s)
# print the marking
print(s.get_marking())

# next state
print('--- Next state ---')
s.next()
print(s)
print(s.get_marking())

# next 2 states
print('--- Next 2 states ---')
s.advance(2)
print(s)
print(s.get_marking())
