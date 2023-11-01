import os
import struct
import pandas as pd


file_path = os.path.expanduser("~/Desktop/regulation.bin")


with open(file_path, "rb") as fp:
    binary_data = fp.read()

floats = struct.unpack('f' * (len(binary_data) // 4), binary_data)
data = np.array(floats)
df = pd.read_fwf(data)
print(df.shape)