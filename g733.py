from g733_battery import G733Battery

class LogitechG733:
    usb_device = None

    def __init__(self, usb_device):
        self.usb_device = usb_device

    def set_led_color(self, red, green, blue):
        color_hex_sequence = self.__get_hex_sequence_for_led_state(red, green, blue)

        # top
        self.usb_device.ctrl_transfer(0x21, 0x09, 0x0211, 0x0003,
                                      [0x11, 0xff, 0x04, 0x3E, 0x01, color_hex_sequence, red, green, blue, 0x02,
                                       0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        self.__read_from_device()
        # bottom
        self.usb_device.ctrl_transfer(0x21, 0x09, 0x0211, 0x0003,
                                      [0x11, 0xff, 0x04, 0x3E, 0x00, color_hex_sequence, red, green, blue, 0x02,
                                       0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        self.__read_from_device()

    def set_sidetone(self, volume):
        self.usb_device.ctrl_transfer(0x21, 0x09, 0x0211, 0x0003,
                                      [0x11, 0xFF, 0x07, 0x1e, volume, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                       0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        self.__read_from_device()

    def is_connected(self):
        data = self.__read_charge_state()
        return data[6] == 1



    def get_charge_percentage(self):
        data = self.__read_charge_state()

        percentage = G733Battery.parse_response(data)
        return percentage

    def __read_charge_state(self):
        self.usb_device.ctrl_transfer(0x21, 0x09, 0x0211, 0x0003,
                                      [0x11, 0xFF, 0x08, 0x0b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                       0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        return self.__read_from_device()

    def __get_hex_sequence_for_led_state(self, red, green, blue):
        if red == 0 and green == 0 and blue == 0:
            return 0
        else:
            return 1

    def __read_from_device(self):
        interface = self.usb_device.get_active_configuration()[(3, 0)][0]
        data = self.usb_device.read(interface.bEndpointAddress, interface.wMaxPacketSize, 0)
        return data

    def __print_decimal_as_hex(self, data):
        str = ""
        for i in data:
            str += " " + hex(i)[2:].zfill(2)
        return str

