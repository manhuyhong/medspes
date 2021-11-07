"""Item 1 - Specialist"""
from snakes.nets import PetriNet, Place, Transition, Expression, Value

VALUE = Value('token')


def print_model():
    """Print the model"""
    print('Model:                 ')
    print('[free]  ←  end ← [docu]')
    print('  ↓                ↑   ')
    print('start → [busy] → change')


class Specialist:
    def __init__(self):
        """The initial state of the specialist is 'free'"""
        # create the model
        self._net = PetriNet('Specialist')
        # add places
        self._P = []
        for p in ['free', 'busy', 'docu']:
            tokens = ['token'] if p == 'free' else []
            self._net.add_place(Place(p, tokens))
            self._P.append(self._net.place(p))
        # add transitions
        self._T = []
        for t in ['start', 'change', 'end']:
            self._net.add_transition(Transition(t, Expression('True')))
            self._T.append(self._net.transition(t))
        # add inputs
        self._net.add_input('free', 'start', VALUE)
        self._net.add_input('busy', 'change', VALUE)
        self._net.add_input('docu', 'end', VALUE)
        # add outputs
        self._net.add_output('free', 'end', VALUE)
        self._net.add_output('busy', 'start', VALUE)
        self._net.add_output('docu', 'change', VALUE)

    def __repr__(self):
        """Represent the current state"""
        return self.get_state()

    def next(self):
        """Next state"""
        for t in self._T:
            if t.modes():
                t.fire(VALUE)
                break

    def advance(self, num):
        """Next n states"""
        for i in range(num):
            self.next()

    def get_marking(self):
        """
        Return a tuple of the current marking (free, busy, docu)
        - e.g. (1, 0, 0)
        """
        return tuple(len(p.tokens) for p in self._P)

    def get_state(self):
        """Return the current state"""
        for p in self._P:
            if p.tokens:
                return str(p)

    def run(self):
        """Run the model in terminal"""
        print('-------------------------------------------')
        print('            Item 1 - Specialist            ')
        print('-------------------------------------------')
        print_model()
        print('-------------------------------------------')
        print('Press enter to next, or "stop" to stop     ')
        print('-------------------------------------------')
        print('[current state]                            ')
        while True:
            print(self)
            option = input().lower()
            if option == 'stop':
                print('Stopped')
                return
            elif option in ['', 'next']:
                self.next()
            else:
                print('Invalid option. Please try again.\n')

    def reset(self):
        """Reset to the initial marking"""
        self.__init__()
