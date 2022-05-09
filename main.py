from enigma import Machine
from ciphers import Cipher

from random import choice
from itertools import permutations


# TODO: ADD INTENSITY LEVEL FOR PRINTS
# TODO: ADD GUI ?!
# TODO ADD fixed ciphers configurations



if __name__ == '__main__':
    MESSAGE = 'heil hitler'

    letters1 = 'nstudogbpqrvaefwxyzhijklmc'
    letters2 = 'rstxyzfghiabcuvwedjklmnopq'
    letters3 = 'jabwxyzmnopqrcdefghiklstuv'
    cipher1 = Cipher(letters1)
    cipher2 = Cipher(letters2)
    cipher3 = Cipher(letters3)

    enigma_german = Machine(
        rotors=[(cipher1, 'a'), (cipher2, 'z'), (cipher3, 'a')])
    x,y,z = choice(letters1), choice(letters1), choice(letters1)
    # print(x,y,z)
    enigma_german.set_rotors_position(
                                    {'rotor0': x,
                                    'rotor1': y,
                                    'rotor2':z})
    print('ORIGINAL SETTING:', enigma_german.get_rotors_position())
    ciphered_german_message = enigma_german.translate(MESSAGE)
    print('ORIGINAL MESSAGE:', ciphered_german_message)
    # print(enigma_german.get_rotors_position())
    # print()
    enigma1 = Machine(rotors=[(cipher1, 'a'), (cipher2, 'z'), (cipher3, 'a')])
    print('looking for configuration according to: \n\t"', MESSAGE, '/', ciphered_german_message,'"')
    for combination in permutations(letters1,3):
        enigma1.set_rotors_position({'rotor0': combination[0],
                                    'rotor1': combination[1],
                                    'rotor2': combination[2]})
        if enigma1.translate(MESSAGE) == ciphered_german_message:
            print('COMBINATION FOUND', combination)
            # print(enigma1.get_rotors_position())
            break
