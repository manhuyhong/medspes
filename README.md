# medspes
Medspes is a Python library for modeling the business of a clinic using Petri Net.


## Installation

Dependencies: [SNAKES](https://github.com/fpom/snakes)

Using pip

```bash
pip install .
```

## Usage

**Example 1**

```python
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

```
Output

```bash
--- Initialize ---
free
(1, 0, 0)
--- Next state ---
busy
(0, 1, 0)
--- Next 2 states ---
free
(1, 0, 0)

```

**Example 2**

```python
from medspes.item1 import Specialist

s = Specialist()
s.run()

```

Output

```bash
-------------------------------------------
            Item 1 - Specialist            
-------------------------------------------
Model:                 
[free]  ←  end ← [docu]
  ↓                ↑   
start → [busy] → change
-------------------------------------------
Press enter to next, or "stop" to stop     
-------------------------------------------
[current state]                            
free
busy
docu
free
busy
Stopped

```

## Uninstallation

```bash
pip uninstall medspes
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
