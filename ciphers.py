from random import shuffle
from string import ascii_lowercase

class Cipher(dict):
    def __init__(self, letters=None, do_shuffle=False):
        super().__init__()
        self.letters = letters
        if self.letters is None:
            self.letters = list(ascii_lowercase)
        elif not isinstance(letters, dict):
            self.letters = list(self.letters)
            if do_shuffle:
                shuffle(self.letters)
            self.generate_symatric()
        else:
            self.update(letters)

    def generate_symatric(self):
        '''
        generate a symetric cipher based on the original key
        :return:
        '''
        for k, v in zip(self.letters, reversed(self.letters)):
            self.setdefault(k, v)
        return self.copy()

