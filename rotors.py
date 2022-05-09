from components import Component

class Rotor(Component):
    def __init__(self, slot, cipher, *args):
        super().__init__(slot=slot, cipher=cipher, static=False, *args)
        self.set_slot(slot)