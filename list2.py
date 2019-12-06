import talib
import numpy as np

list1 = [1, 2, 4, 5, 6, 8, 10, 12, 14, 16, 19, 24, 29]  # 13个
# print(list1[:-3])
# print(list1[-3:])
output = talib.SMA(np.array(list1, dtype='d'), 3)
print(output)