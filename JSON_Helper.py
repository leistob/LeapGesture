import json

METHOD = "method"
MODULE = "module"
JSON_PROTOCOL = "json_rpc"
PARAMS = "params"
POSITION = "position"
POS_X = "pos_x"
POS_Y = "pos_y"
POS_Z = "pos_z"
SPEED = "speed"
STATUS = "status"
HAND = "hand"
DEFLECTION = "deflection"
DEF_X = "def_x"
DEF_Y = "def_y"
DEF_Z = "def_z"

CURRENT_MODULE = "gesture"
CURRENT_METHOD = "move"
STATUS_ACTIVE = "active"
STATUS_INACTIVE = "inactive"
JSON_VERSION = "2.0"

HAND_LEFT = "hand_left"
HAND_RIGHT = "hand_right"

ORIENTATION = "orientation"
PITCH = "pitch"
YAW = "yaw"
ROLL = "roll"
IS_FIST = "is_fist"


def build_json(speed=0.0, pos_x=0.0, pos_y=0.0, pos_z=0.0,
               def_x=0.0, def_y=0.0, def_z=0.0,
               pitch=0.0, yaw=0.0, roll=0.0, is_fist=5, status=STATUS_ACTIVE, hand=""):

    data = {JSON_PROTOCOL: JSON_VERSION,
            MODULE: CURRENT_MODULE,
            METHOD: CURRENT_METHOD,
            PARAMS: {POSITION: {POS_X: str(pos_x),
                                POS_Y: str(pos_y),
                                POS_Z: str(pos_z)},
                     DEFLECTION: {DEF_X: str(def_x),
                                  DEF_Y: str(def_y),
                                  DEF_Z: str(def_z)},
                     ORIENTATION: {PITCH: str(pitch),
                                   YAW: str(yaw),
                                   ROLL: str(roll)},
                     IS_FIST: is_fist,
                     SPEED: speed,
                     STATUS: status,
                     HAND: hand}}

    json_data = json.dumps(data)
    return json_data


def build_json_inactive():
    return build_json(status=STATUS_INACTIVE)
