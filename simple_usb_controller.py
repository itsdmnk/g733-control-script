import usb.core

class SimpleUsbController:
    device = None

    def __init__(self, vendor_id, product_id):
        self.find_device(vendor_id, product_id)
        self.__detach_drivers_from_device()

    def find_device(self, vendor_id, product_id):
        self.device = usb.core.find(idVendor=vendor_id, idProduct=product_id)

    def reattach_drivers(self):
        self.device.attach_kernel_driver(0)

    def __detach_drivers_from_device(self):
        for cfg in self.device:
            for interface in cfg:
                self.__detach_kernel_driver_from_interface(interface)

    def __detach_kernel_driver_from_interface(self, interface):
        if self.__is_kernel_driver_active(interface):
            try:
                self.device.detach_kernel_driver(interface.bInterfaceNumber)
            except usb.core.USBError as e:
                sys.exit("Could not detach kernel driver from interface", intf.bInterfaceNumber, )

    def __is_kernel_driver_active(self, interface):
        return self.device.is_kernel_driver_active(interface.bInterfaceNumber)



