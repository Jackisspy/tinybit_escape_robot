let distance = 0
basic.showString("Hello Tinn")
basic.forever(function () {
    distance = Tinybit.Ultrasonic_Car()
    if (distance < 20 && distance > 2) {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_SpinLeft, 50)
        basic.pause(randint(100, 200))
    } else {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 150)
    }
})
