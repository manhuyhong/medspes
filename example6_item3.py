from medspes.item3 import MergedModel


while True:
    try:
        n = int(input('How many patients today? '))
        break
    except ValueError:
        print('Integer only!')

try:
    m = MergedModel(n)
    m.run()
except ValueError:
    print('Uh oh! The number of patients cannot be negative,')
    print('or larger than 10, as our clinic is not big enough.')
