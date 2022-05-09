import string


class Component:
    components = [[]]

    def __init__(self,name: str, machine_id: int = None, index: int = None,
                 cipher: dict = None, order: list = None,
                 slot: int = None, position: int = None, static: bool = None,
                 quite = True):
        '''
        :param name: component name,
                special names: reflector,
        :param index: the index used to determinate when each component taking an action
        :param cipher: dictionary with a cipher, has to be symatric
        :param order: the order of the letters in the rotor, self.order[i] is where the rottors are conneted
        :param slot: when should the index+1 rotor to tick
        :param position: when position == slot the nex rotor will tick
        :param static: static means' disable ticking for that cipher
        :param quite: control prints
        '''
        self.name = name
        self.machine_id = machine_id
        self.index = index
        self.cipher = cipher
        self.slot = slot
        self.order = order
        self.position = position
        self.static = True

        if machine_id is None:
            self.machine_id = 0
        if self.machine_id >= len(Component.components):
            Component.components.append([])
        self.machine = Component.components[self.machine_id]
        if index is None:
            self.index = len(self.machine)
        if cipher is None:
            self.cipher = {i: i for i in string.ascii_lowercase}
        if self.order is None:
            self.order = list(sorted(self.cipher.keys()))
        if self.position is None:
            self.position = 0
        if self.slot is None:
            self.slot = 25
        self.set_slot()
        if not static:  # a rotor..
            self.static = False
        self.quite = quite
        Component.components[self.machine_id].insert(self.index, self)

    def tick(self):
        '''
        should be called every time before a letter is passed through the keyboard
        :return:
        '''
        self.position += 1
        self.print(self.name, 'ticked')
        last_letter = self.order.pop(0)
        self.order.append(last_letter)
        if self.position >= len(self.cipher.keys()):
            self.position = 0
        if self.slot == self.position:
            self.machine[self.index + 1].tick()


    def cipher_letter(self, letter):
        return self.cipher[letter]

    def find_index(self, letter):
        return self.order.index(letter)

    def forward_letter(self, letter):
        '''
        this is the main function to cipher a letter, including calling the backwards function
        that allows symmetric output of the enigma
        :param str letter: letter
        :return str: ciphered letter
        '''
        self.print(self.name, self.index,':')
        if letter not in self.order:
            self.print(f"MISSING CHARACTER: '{letter}'")
            return letter
        letter_index = self.find_index(self.cipher_letter(letter))
        self.print('\tletter_index:', letter_index, '\n\tinput_letter:', letter, '\n\tcipherd:', self.order[letter_index])
        # print(self.index)
        if self.name == 'reflector':
            return self.backward(self.cipher[letter])
        # if self.name == 'monitor':  # if self.index == len(Component.components):
        #     return letter
        next_letter = self.machine[self.index + 1].order[letter_index]
        self.print('next_letter_input_letter', next_letter)
        return self.machine[self.index + 1].forward_letter(
            self.machine[self.index + 1].order[letter_index])

    def backward(self, letter):
        '''
        during encryption proccess
        :param letter:
        :return:
        '''
        self.print(self.name, letter, '>>', self.cipher_letter(letter))
        letter_index = self.find_index(self.cipher_letter(letter))
        if self.name == 'reflector':
            letter_index = self.find_index(letter)
        if self.index == 1:  # assuming first element in the list is the keyboard
            return letter
        return self.machine[self.index - 1].backward(
            self.machine[self.index - 1].order[letter_index])

    def print(self, *args):
        '''
        :param args: builtin print
        :return:
        '''
        if not self.quite:
            print(*args)

    def set_position(self, letter):
        letter_position = letter
        if not isinstance(letter,int):
            letter_position = self.find_index(letter)
        self.order = self.order[letter_position:] + self.order[:letter_position]
        self.position = 0#letter_position #0

    def set_slot(self, letter=None):
        if letter is None:
            if isinstance(self.slot, str):
                self.slot = self.find_index(self.slot)
        else:
            self.slot = self.find_index(letter)
        return self.slot
