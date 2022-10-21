Td = 0
# on attend pin=1 (début écho)
# puis on attend pin=0 (fin écho)
# après on peut utiliser la valeur calculée par "on pin pulsed"
# 
# on pourrait aussi mettre une simple tempo
# 400cm x 58µs = 23,2ms
def mesureT1():
    while pins.digital_read_pin(DigitalPin.P1) == 0:
        pass
    while pins.digital_read_pin(DigitalPin.P1) == 1:
        pass
def pulse_TRIG():
    pins.digital_write_pin(DigitalPin.P0, 1)
    control.wait_micros(10)
    pins.digital_write_pin(DigitalPin.P0, 0)

def on_pulsed_p1_high():
    global Td
    # durée de la dernière pulse reçue
    Td = pins.pulse_duration()
pins.on_pulsed(DigitalPin.P1, PulseValue.HIGH, on_pulsed_p1_high)

def mesureT2():
    global Td
    # pas clair comment fonctionne
    # on attend la pulse et on revient après?
    # si pas de pulse?
    Td = pins.pulse_in(DigitalPin.P1, PulseValue.HIGH)

def on_forever():
    pulse_TRIG()
    basic.pause(25)
    basic.show_number(Td)
basic.forever(on_forever)
