from MotorModule import Motor
import keyboard as kb


motor = Motor(13, 19, 26, 16, 20, 21)

kb.init()


def main():
    if kb.getKey("UP"):
        motor.move(10.0, 0, 0.1)
    elif kb.getKey("DOWN"):
        motor.move(-10, 0, 0.1)
    elif kb.getKey("LEFT"):
        motor.move(0.5, 0.3, 0.1)
    elif kb.getKey("RIGHT"):
        motor.move(0.5, -0.3, 0.1)
    else:
        motor.stop(0.1)


if __name__ == "__main__":
    while True:
        main()

