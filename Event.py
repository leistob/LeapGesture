LEAP_VAL_CHANGED = "val_changed"
LEAP_INACTIVE = "leap_inactive"
UI_VAL_CHANGED = "ui_val_changed"


class Observer:
    _observers = []

    def __init__(self):
        self._observers.append(self)
        self._observables = {}

    def observe(self, event_name, callback):
        self._observables[event_name] = callback


class Event:
    def __init__(self, name, data, auto_fire=True):
        self.name = name
        self.data = data
        if auto_fire:
            self.fire()

    def fire(self):
        for observer in Observer._observers:
            if self.name in observer._observables:
                observer._observables[self.name](self.data)
