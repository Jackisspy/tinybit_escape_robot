def on_received_value(name, value):
    if name == "run":
        wuKong.set_motor_speed(wuKong.MotorList.M1, value)
    else:
        wuKong.stop_all_motor()
radio.on_received_value(on_received_value)

radio.set_group(1)
basic.show_icon(IconNames.YES)

def on_forever():
    if pins.digital_read_pin(DigitalPin.P0) == 1:
        wuKong.set_motor_speed(wuKong.MotorList.M1, -100)
        radio.send_number(-100)
    elif pins.digital_read_pin(DigitalPin.P1) == 1:
        wuKong.set_motor_speed(wuKong.MotorList.M1, 100)
        radio.send_number(100)
basic.forever(on_forever)
