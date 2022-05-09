from ciphers import Cipher
from components import Component
from string import ascii_lowercase

class Machine:
    machines = []

    def __init__(self, rotors: list, machine_id = None, plugboard_cipher=None, reflector_cipher=None, quite=True):
        self.machine_id = machine_id
        if self.machine_id is None:
            self.machine_id = len(Machine.machines)
        Machine.machines.append(self)

        self.keyboard = Component('keyboard', static=True, index=0, machine_id=self.machine_id)
        self.plugboard = Component('plugboard', static=True, cipher=plugboard_cipher,machine_id=self.machine_id)
        self.rotors = []
        for i, (cipher, slot) in enumerate(rotors):
            setattr(self, f'rotor{i}',Component(f'rotor{i}', cipher=cipher, slot=slot, machine_id=self.machine_id))
        if reflector_cipher is None:
            reflector_cipher = Cipher(ascii_lowercase)
        self.reflector = Component('reflector', cipher=reflector_cipher, static=True,machine_id=self.machine_id)
        if not quite:
            self.print_components()
        self.lamp_board = ''
        self.machine = Component.components[self.machine_id]
        # for k,v in self.__dict__.items():
        #     print(k)


    def translate(self, text):
        '''
        :param str text: text to encrypt decrypt
        :return str: encrypted/decrypted text
        '''
        output = ''
        for letter in text:
            self.rotor0.tick()
            # print(self.rotor0.slot, self.rotor0.position)
            output = output + self.keyboard.forward_letter(letter.lower())
        return output

    def print_components(self):
        for i in range(len(self.machine)):
            print(i, self.machine[i].index, self.machine[i].name)

    def set_rotors_position(self, position):
        '''
        :param dict position: ROTOR_NAME : LETTER POSITION (order[0])
        :return:
        '''
        rotors_dict = {i.name:i for i in self.machine if not i.static}
        for name, letter in position.items():
            rotors_dict[name].set_position(letter)

    def get_rotors_position(self):
        rotors_dict = {i.name: i for i in self.machine if not i.static}
        rotors_position = dict()
        for rotor in rotors_dict.values():
            rotors_position[rotor.name] = (rotor.position, rotor.order[rotor.position], rotor.order[0])
        return rotors_position