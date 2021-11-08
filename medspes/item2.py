"""Item 2 - Patients"""
from snakes.nets import PetriNet, Place, Transition, Expression, Value

VALUE = Value('token')


def print_model():
    print('Model:                                     ')
    print('[wait] → start → [inside] → change → [done]')


class InvalidEvent(Exception):
    def __init__(self, message='Invalid event.'):
        self.message = message


class Patients:
    def __init__(self, num_wait):
        """
        The initial state of the patients:
        wait=num_wait, inside=0, done=0

        :param num_wait: accepts an integer from 0 to 10
        """
        if type(num_wait) is not int:
            raise TypeError('num_wait must be an integer')
        elif not 0 <= num_wait <= 10:
            raise ValueError(f'Invalid number of waiting patients: {num_wait}\n'
                             f'Only accepting 0 to 10.')

        # create the model
        self._net = PetriNet('Patients')
        # add places
        self._P = []
        for p in ['wait', 'inside', 'done']:
            tokens = ['token'] * num_wait if p == 'wait' else []
            self._net.add_place(Place(p, tokens))
            self._P.append(self._net.place(p))
        # add transitions
        self._T = []
        for t in ['start', 'change']:
            self._net.add_transition(Transition(t, Expression('True')))
            self._T.append(self._net.transition(t))
        # add inputs
        self._net.add_input('wait', 'start', VALUE)
        self._net.add_input('inside', 'change', VALUE)
        # add outputs
        self._net.add_output('inside', 'start', VALUE)
        self._net.add_output('done', 'change', VALUE)

    def __repr__(self):
        """Represent the current state"""
        state = []
        for p, token_count in zip(self._P, self.get_marking()):
            state.append(str(p) + ': ' + str(token_count))
        return '   '.join(state)

    def is_waiting(self):
        """Check if any patient is waiting"""
        return bool(self._net.transition('start').modes())

    def is_inside(self):
        """Check if any patient is inside"""
        return bool(self._net.transition('change').modes())

    def next(self):
        """Next state"""
        if self.is_inside():
            self._net.transition('change').fire(VALUE)
        elif self.is_waiting():
            self._net.transition('start').fire(VALUE)
        else:
            raise InvalidEvent('All done. No patient left.')

    def advance(self, num):
        """Next n states"""
        for i in range(num):
            self.next()

    def get_marking(self):
        """
        Return a tuple of the current marking (wait, inside, done)
        - e.g. (5, 0, 1)
        """
        return tuple(len(p.tokens) for p in self._P)

    def run(self):
        """Run the model in terminal"""
        print('-------------------------------------------')
        print('             Item 2 - Patients             ')
        print('-------------------------------------------')
        print_model()
        print('-------------------------------------------')
        print('Press enter to next, or "stop" to stop     ')
        print('-------------------------------------------')
        print('[current state]                            ')

        while True:
            print(self)
            marking = self.get_marking()
            # finished if no patients are waiting nor inside
            if marking[0] + marking[1] == 0:
                break

            option = input().lower()
            if option == 'stop':
                print('Stopped')
                return
            if option in ['', 'next']:
                self.next()
            else:
                print('Invalid option. Please try again.\n')
        print('Finished')

    def reset(self, num_wait):
        """Reset to the initial marking"""
        self.__init__(num_wait)
