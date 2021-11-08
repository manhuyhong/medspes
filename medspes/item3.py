"""Item 3 - Merged model"""
from medspes.item1 import Specialist
from medspes.item2 import Patients, InvalidEvent


def print_model():
    """Print the model"""
    print('Model:                                   ')
    print('           ―――→ [inside] ―――――           ')
    print('           |                 ↓           ')
    print('[wait] → start → [busy] → change → [done]')
    print('           ↑                 ↓           ')
    print('        [free] ←  end  ←  [docu]         ')


class MergedModel:
    def __init__(self, num_wait):
        """
        The initial state of the model:\n
        Specialist: free\n
        Patients: wait=num_wait, inside=0, done=0

        :param num_wait: accepts an integer from 0 to 10
        """
        self._specialist = Specialist()
        self._patients = Patients(num_wait)

    def __repr__(self):
        """Represent the current state"""
        return '\n'.join(['Specialist: ' + str(self._specialist),
                          'Patients: ' + str(self._patients)])

    def next(self):
        """Next state"""
        # fire start
        if self._specialist.get_state() == 'free' and self._patients.is_waiting():
            self._specialist.next()
            self._patients.next()
        # fire change
        elif self._specialist.get_state() == 'busy':
            self._specialist.next()
            self._patients.next()
        # fire end
        elif self._specialist.get_state() == 'docu':
            self._specialist.next()
        else:
            raise InvalidEvent('All done. No patient left.')

    def advance(self, num):
        """Next n states"""
        for i in range(num):
            self.next()

    def get_marking(self):
        """
        Return a tuple of the current marking (free, busy, docu, wait, inside, done)
        - e.g. (1, 0, 0, 5, 0, 1)
        """
        s = self._specialist.get_marking()
        p = self._patients.get_marking()
        return s + p

    def run(self):
        """Run the model in terminal"""
        print('------------------------------------------------')
        print('             Item 3 - Merged Model              ')
        print('------------------------------------------------')
        print_model()
        print('------------------------------------------------')
        print('Press enter to next, or "stop" to stop          ')
        print('------------------------------------------------')
        print('[current state]                                 ')

        while True:
            print(self)
            marking = self._patients.get_marking()
            # finished if no patients are waiting nor inside
            # and the specialist is free
            if marking[0] + marking[1] == 0 and self._specialist.get_state() == 'free':
                break

            option = input().lower()
            if option == 'stop':
                print('Stopped')
                return
            elif option in ['', 'next']:
                self.next()
            else:
                print('Invalid option. Please try again.\n')
        print('Finished')

    def reset(self, num_wait):
        """Reset to the initial marking"""
        self.__init__(num_wait)
