import Leap
import JSON_Helper as jH
from Event import *


class LeapSensorListener(Leap.Listener):
    max_position_x = 300
    max_position_y = 150
    max_position_z = 200

    def on_init(self, controller):
        print "Initialized"
        self.status = ""

    def on_connect(self, controller):
        print "Connected"
        self.status = jH.STATUS_ACTIVE

    def on_disconnect(self, controller):
        print "Disconnected"
        self.status = jH.STATUS_INACTIVE

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        frame = controller.frame()

        if frame.hands.is_empty and self.status == jH.STATUS_ACTIVE:
            self.status = jH.STATUS_INACTIVE
            Event(LEAP_INACTIVE, jH.STATUS_INACTIVE)
            return
        if frame.hands.is_empty:
            return

        self.status = jH.STATUS_ACTIVE
        current_hand = frame.hands[0]
        palm_position = current_hand.palm_position
        deflection_x = calculate_speed(self.max_position_x, palm_position.x)
        deflection_y = calculate_speed(self.max_position_y, palm_position.y)
        deflection_z = calculate_speed(self.max_position_z, palm_position.z)

        pitch = current_hand.direction.pitch
        yaw = current_hand.direction.yaw
        roll = current_hand.palm_normal.roll

        print pitch

        data_arr = []
        data_arr.append(round(palm_position.x, 1))
        data_arr.append(round(palm_position.y, 1))
        data_arr.append(round(palm_position.z, 1))
        data_arr.append(deflection_x)
        data_arr.append(deflection_y)
        data_arr.append(deflection_z)
        data_arr.append(pitch)
        data_arr.append(yaw)
        data_arr.append(roll)

        Event(LEAP_VAL_CHANGED, data_arr)


def calculate_speed(max_pos, pos_x):
    max_pos = float(max_pos)
    max_speed = 1.0
    signum = pos_x
    signum = abs(signum)
    if signum > max_pos:
        if pos_x > 0:
            return max_speed
        else:
            return -max_speed

    percent_pos = pos_x / max_pos
    speed = percent_pos * max_speed
    # Round result
    return round(speed, 3)


def check_fist(hand):
    min_value = 0.1
    finger_sum = 0
    for finger in hand.fingers:
        meta = finger.bone(0).direction
        proxi = finger.bone(1).direction
        inter = finger.bone(2).direction
        dMetaProxi = meta.dot(proxi)
        dProxiInter = proxi.dot(inter)
        finger_sum += dMetaProxi
        finger_sum += dProxiInter
        finger_sum /= 10.0

    if finger_sum <= min_value:
        return True
    else:
        return False
