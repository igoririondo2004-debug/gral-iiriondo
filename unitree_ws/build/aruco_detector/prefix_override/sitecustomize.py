import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/tknika/gral-iiriondo-main/unitree_ws/install/aruco_detector'
