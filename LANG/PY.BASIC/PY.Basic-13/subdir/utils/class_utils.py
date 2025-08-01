# class_utils.py

class Encoder:
    def encode(self, s):
        return s[::-1]

class Decoder:
    def decode(self, s):
        return ''.join(reversed(list(s)))