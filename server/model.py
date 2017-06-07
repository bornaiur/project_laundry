import random
import time

def temp_model(filename):
    labels = ['socks', 'panty', 'tshirt', 'hankerchif', 'bra', 'short pants']
    print('classfying.....', flush=True, end='\t')
    time.sleep(3)
    ans = labels[random.randint(0, 5)]
    print('[ {} ]'.format(ans), flush=True)
    return ans
