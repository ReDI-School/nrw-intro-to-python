from baseencoder import BaseEncoder

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': ''}


class MorseEncoder(BaseEncoder):
    code_dict = MORSE_CODE_DICT
    
    def encode(self, text_in: str) -> str:
        return ''.join([
            f'{self.code_dict[c]} '
            for c in text_in
        ]).rstrip()
    
    def decode(self, text_in: str) -> str:
        # Invert code_dict
        inverse_code_dict = {
            value: key
            for key, value in self.code_dict.items()
        }
        return ''.join([
            inverse_code_dict[c] for c in text_in.split(' ')
        ]).rstrip()