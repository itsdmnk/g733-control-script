# Logitech G733 Sidetone, LED + Battery control

### Usage

Make sure to install `pyusb` (on arch install the package `python-pyusb`).

```bash
# turn sidetone and led off: 
sudo python main.py --sidetone 0 --colors 0

# turn sidetone on and led to white
sudo python main.py --sidetone 60 --colors 255 255 255
```

### Filters for USBLyzer

If you wan't to find other functions of the headset (such as the breathing mode for leds),
you can use the following filters for USBLyzer.

`URB Functions`
- `Class`
    - ALL
- `Transfer`
    - ALL but `..._ISOCH_TRANSFER`
  