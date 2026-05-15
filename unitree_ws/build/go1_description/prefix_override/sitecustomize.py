import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/igor/gral-iiriondo/unitree_ws/install/go1_description'
