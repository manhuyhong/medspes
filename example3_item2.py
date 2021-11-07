from medspes.item2 import Patients

# create an object
p = Patients(8)

# print the current state
print('--- Initialize ---')
print(p)
# print the marking
print(p.get_marking())
# check if any patient is waiting
print('Is there anyone waiting?', p.is_waiting())
# check if any patient is inside
print('Is there anyone inside?', p.is_inside())

# next states
p.next()
print('--- Next state ---')
print(p)
print(p.get_marking())
print('Anyone inside now?', p.is_inside())

# next 5 states
p.advance(5)
print('--- Next 5 states ---')
print(p)
print(p.get_marking())
