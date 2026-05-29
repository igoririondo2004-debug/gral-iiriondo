import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/tknika/gral-iiriondo/unitree_ws/install/standing_mode'
