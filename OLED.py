import time
import curses
import atexit

def cleanup():
   curses.nocbreak()
   curses.echo()
   curses.endwin()


class State(object):
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self):
        print('Processing current state:', str(self))
        self.order = ["SystemStatus","Sensor1","Sensor2","Sensor3","Sensor4"]

    def next(self):
        index = self.order.index(self.__class__.__name__)
        index = index + 1 if len(self.order) > index+1 else 0
        fnName = self.order[index]
        return globals()[fnName]()

    def prev(self):
        index = self.order.index(self.__class__.__name__)
        index = index - 1 if len(self.order) > 0 else len(self.order)-1
        fnName = self.order[index]
        return globals()[fnName]()

    def on_event(self, event):
        if not hasattr(self, 'order'):
            return self
        if event == 'buttonNext':
            return self.next()
        if event == 'buttonPrev':
            return self.prev()
        return self

    def __repr__(self):
        """globals()[fnName]()globals()[fnName]()
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.__class__.__name__
# Start of our states

class SystemStatus(State):
    pass

class Sensor1(State):
    pass

class Sensor2(State):
    pass

class Sensor3(State):
    pass

class Sensor4(State):
    pass

# End of our states.

class Screen(object):

    def __init__(self):
        """ Initialize the components. """
        # Start with a default state.
        self.state = SystemStatus()

    def on_event(self, event):
        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event)

if __name__ == "__main__":
    screen = Screen()
    screen.on_event("buttonNext")
    screen.on_event("buttonNext")
    screen.on_event("buttonPrev")
    screen.on_event("buttonPrev")
    screen.on_event("buttonPrev")
    screen.on_event("buttonNext")
