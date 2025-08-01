# main.py

from utils import get_sum
from class_utils import Encoder, Decoder

print(get_sum(1, 2))

encoder = Encoder()
print(encoder.encode('abcde'))

decoder = Decoder()
print(decoder.decode('edcba'))