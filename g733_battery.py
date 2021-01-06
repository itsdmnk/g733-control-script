class G733Battery:
    CHARGE_MAX = 4200
    CHARGE_MIN = 3600

    @staticmethod
    def parse_response(response):
        voltage = G733Battery.__get_voltage(response)
        percentage = G733Battery.__calculate_percentage_from_voltage(voltage)
        return percentage

    @staticmethod
    def __get_voltage(response):
        raw = [hex(response[4]), hex(response[5])]
        voltage = int(raw[0][2:] + raw[1][2:].zfill(2), 16)
        return voltage

    @staticmethod
    def __calculate_percentage_from_voltage(voltage):
        percentage = (voltage - G733Battery.CHARGE_MIN) / (
                G733Battery.CHARGE_MAX - G733Battery.CHARGE_MIN)
        return round(percentage * 100, 2)
