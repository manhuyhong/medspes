from medspes.item2 import Patients

while True:
    try:
        n = int(input('How many patients today? '))
        break
    except ValueError:
        print('Integer only!')

try:
    p = Patients(n)
    p.run()
except ValueError:
    print('Uh oh! The number of patients cannot be negative,')
    print('or larger than 10, as our clinic is not big enough.')
