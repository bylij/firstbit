# sub_main.py

import sys
sys.path.append('..')

from utils.class_utils import *

encoder = Encoder()
print(encoder.encode('abcde'))

decoder = Decoder()
print(decoder.decode('edcba'))