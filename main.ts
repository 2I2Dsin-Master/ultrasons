let Td = 0
let mes = 0
function pulse_TRIG () {
    pins.digitalWritePin(DigitalPin.P0, 1)
    control.waitMicros(10)
    pins.digitalWritePin(DigitalPin.P0, 0)
}
pins.onPulsed(DigitalPin.P1, PulseValue.High, function () {
    // durée de la dernière pulse reçue
    Td = pins.pulseDuration()
})
basic.forever(function () {
    pulse_TRIG()
    basic.pause(25)
    mes = Td / 58
    led.plotBarGraph(
    mes,
    10
    )
})
