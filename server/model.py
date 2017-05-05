import random
import time

def temp_model(filename):
    labels = ['socks', 'panty', 'tshirt', 'hankerchif', 'bra', 'short pants']
    print('classfying.....', flush=True)
    time.sleep(3)
    return labels[random.randint(0, 5)]






