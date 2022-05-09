import string

class BaseEncoder:
    code_dict: dict[str, str] = {
        c: c
        for c in string.ascii_uppercase
    }
    
    def encode(self, text_in: str) -> str:
        return ''.join([
            self.code_dict[c] for c in text_in
        ])
    
    def decode(self, text_in: str) -> str:
        # Invert code_dict
        inverse_code_dict = {
            value: key
            for key, value in self.code_dict.items()
        }
        return ''.join([
            inverse_code_dict[c] for c in text_in
        ])