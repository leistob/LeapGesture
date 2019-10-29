import socket
from LeapSensorListener import *
from Socket_Client import Client
import Window as wD
import JSON_Helper as jH
import configparser

LEFT_IN = "left_in"
RIGHT_IN = "right_in"

INI_PATH = "config.ini"


class Controller(Observer):

    def __init__(self, s_client, ui, mode):
        Observer.__init__(self)
        self.c = s_client
        self.ui = ui
        self.mode_in = mode

    def show_view(self):
        self.ui.start_ui()

    def add_listener(self):
        self.observe(LEAP_VAL_CHANGED, self.leap_data_received)
        self.observe(LEAP_INACTIVE, self.leap_inactive_received)
        self.observe(UI_VAL_CHANGED, self.ui_data_received)

    def leap_inactive_received(self, who):
        self.c.send_string(jH.build_json_inactive())
        self.ui.reset_slider()

    def ui_data_received(self, speed):
        # print "test"
        return
        # self.c.send_string(str(speed))

    def leap_data_received(self, data):
        json_data = jH.build_json(pos_x=data[0],
                                  pos_y=data[1],
                                  pos_z=data[2],
                                  def_x=data[3],
                                  def_y=data[4],
                                  def_z=data[5],
                                  pitch=data[6],
                                  yaw=data[7],
                                  roll=data[8])
        # print json_data
        self.c.send_string(json_data)
        # self.ui.set_slider_val(who)

    def close_socket_conn(self):
        try:
            self.c.close_socket_conn()
        except socket.error:
            print "Could not close socket connection"


def main():
    # Default values in case config.ini is compromised
    max_pos_leap_x = 250
    max_pos_leap_y = 200
    max_pos_leap_z = 150
    mode_in = LEFT_IN
    server_addr = '127.0.0.1'
    server_port = 5555

    # Try to read config.ini values
    try:
        config = configparser.ConfigParser()
        config.read(INI_PATH)
        max_pos_leap_x = config["DEFAULT"]["MAX_POS_X"]
        max_pos_leap_y = config["DEFAULT"]["MAX_POS_Y"]
        max_pos_leap_z = config["DEFAULT"]["MAX_POS_Z"]
        mode_in = config["DEFAULT"]["MODE_IN"]
        server_port = config["DEFAULT"]["SERVER_PORT"]
        server_addr = config["DEFAULT"]["SERVER_ADDRESS"]
    except:
        print "Could not read .ini files, using default values"

    client = Client(server_addr, int(server_port))
    client.connect()
    window = wD.Window()

    main_controller = Controller(client, window, mode_in)
    main_controller.add_listener()

    leap_listener = LeapSensorListener()
    leap_listener.max_position_x = max_pos_leap_x
    leap_listener.max_position_y = max_pos_leap_y
    leap_listener.max_position_z = max_pos_leap_z
    leap_controller = Leap.Controller()
    leap_controller.add_listener(leap_listener)

    window.start_ui()

    leap_controller.remove_listener(leap_listener)
    main_controller.close_socket_conn()


if __name__ == "__main__":
    main()
