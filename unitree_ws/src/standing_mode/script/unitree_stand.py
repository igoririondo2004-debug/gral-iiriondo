#!/usr/bin/env python3.8
import time
import sys
import robot_interface as sdk

ROBOT_IP = "192.168.123.161"

udp = sdk.UDP(0xee, 8080, ROBOT_IP, 8082)

cmd = sdk.HighCmd()
state = sdk.HighState()

udp.InitCmdData(cmd)


def send(cmd_mode, body_height=0.0, duration=3.0):
    cmd.mode = cmd_mode
    cmd.gaitType = 0
    cmd.speedLevel = 0
    cmd.footRaiseHeight = 0.0
    cmd.bodyHeight = body_height
    cmd.euler = [0.0, 0.0, 0.0]
    cmd.velocity = [0.0, 0.0]
    cmd.yawSpeed = 0.0

    print(f"[INFO] mode={cmd_mode}, bodyHeight={body_height}")

    start = time.time()
    while time.time() - start < duration:
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(0.02)


def stand_down():
    print(">>> STAND DOWN (relaxed)")
    send(5, body_height=-0.2)


def stand_up():
    print(">>> STAND UP")
    send(6, body_height=0.0)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage:")
        print("  python3.8 unitree_control.py stand_up")
        print("  python3.8 unitree_control.py stand_down")
        sys.exit(1)

    cmd_arg = sys.argv[1]

    if cmd_arg == "stand_down":
        stand_down()

    elif cmd_arg == "stand_up":
        stand_up()

    else:
        print("Unknown command:", cmd_arg)
        print("Use: stand_up | stand_down")