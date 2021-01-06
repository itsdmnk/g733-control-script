from simple_usb_controller import SimpleUsbController
from g733 import LogitechG733
import argparse
import sys

parser = argparse.ArgumentParser(description="G733 Headset")
parser.add_argument('--sidetone', nargs=1, type=int, help='Volume of sidetone (from 0 to 100)')
parser.add_argument('--colors', nargs='+', type=int, help='RGB Colors')

args = parser.parse_args()

VENDOR_ID = 0x046d # Logitech
PRODUCT_ID = 0x0ab5 # G733

usb_controller = SimpleUsbController(VENDOR_ID, PRODUCT_ID)
g733 = LogitechG733(usb_controller.device)

if not g733.is_connected():
    print("USB Device found, but charge state indicates that it's off?")

charge_percentage = g733.get_charge_percentage()
print("Battery: ", charge_percentage, "%")

if args.colors is not None and len(args.colors) == 1:
    print("Turning leds off")
    g733.set_led_color(0, 0, 0)
elif args.colors is not None and len(args.colors) > 1:
    print("Setting colors to", args.colors)
    g733.set_led_color(args.colors[0], args.colors[1], args.colors[2])

if args.sidetone is not None:
    print("Setting sidetone to", args.sidetone[0])
    g733.set_sidetone(args.sidetone[0])

usb_controller.reattach_drivers()
