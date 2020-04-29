# 01-navyCalc.py
"""
Title: Cannon Operator
Author: Jackson Reid
Date Created: 2020-04-29
"""
from sys import exit  # for python 3.5 or less
import math


# --- Inputs --- #
def askNumbersScenario1():
    """
    Asks for two numbers from the user
    :return: height, speed
    """
    height = checkNumberFloat(input("Height of the cannon above the water: "))
    speed = checkNumberFloat(input("Speed of the cannonball immediately after leaving the cannon: "))
    return height, speed


def askNumbersScenario2():
    """
    Asks for two numbers from the user
    :return: angle, speed
    """
    angle = checkNumberFloat(input("Height of the cannon above the water: "))
    speed = checkNumberFloat(input("Angle of the cannon : "))
    return angle, speed


def askNumbersScenario3():
    """
    Asks for three numbers from the user
    :return: angle, speed, heightCannon
    """
    angle = checkNumberFloat(input("Angle of the cannon: "))
    speed = checkNumberFloat(input("Speed of the cannonball : "))
    heightCannon = checkNumberFloat(input("Height of the cannon above target: "))
    return angle, speed, heightCannon


def menu():
    """
    display program options
    :return: valid option within the menu (Integer)
    """
    print(
        """
1. Cannon is shooting horizontal
2. Cannon is shooting at an angle to hit a target level with it
3. Cannon is shooting at an angle to hit a target shorter/lower than it
4. EXIT
"""
    )
    answer = checkNumberInt(input("> "))
    if 0 < answer < 5:
        return answer
    else:
        print("Please enter a valid number")
        return menu()


# --- Process --- #


def checkInt(value):
    """
    Test if the value can be converted into an integer.
    :param value: float value
    :return: float or integer value
    """
    if int(value) == value:
        return int(value)
    else:
        return value




def checkNumberFloat(value):
    """
    Checks if the value is a float and will typecast to a float
    :param value: string value to check
    :return: float value
    """
    try:
        value = float(value)
        return value
    except ValueError:
        print("You did not enter a number")
        newNum = input("Please enter a number: ")
        return checkNumberFloat(newNum)


def scenario1(height, speed):
    """
    Runs calculations for scenario 1
    :param height: height of the cannon above the water
    :param speed: speed of the cannonball immediately after it leaves the cannon
    :return: result
    """
    time = math.sqrt((2 * height) / 9.81)
    result = speed * time
    return result


def scenario2(angle, speed):
    """
    Runs calculations for scenario 2
    :param angle: angle of the cannon when the cannonball leaves the cannon
    :param speed: speed of the cannonball immediately after it leaves the cannon
    :return: result
    """
    speedHorizontal = speed * math.cos(angle)
    speedVertical = speed * math.sin(angle)
    timePeak = speedVertical / 9.81
    time = timePeak * 2
    result = speedHorizontal * time
    return result


def scenario3(angle, speed, heightCannon):
    """
    Runs calculations for scenario 3
    :param angle: angle of the cannon when the cannonball leaves the cannon
    :param speed: speed of the cannonball immediately after it leaves the cannon
    :param heightCannon: height of the cannon relative to the target
    :return: result
    """
    speedHorizontal = speed * math.cos(angle)
    speedVertical = speed * math.sin(angle)
    distancePeak = (speedVertical ** 2) / (2 * 9.81)
    heightTotal = heightCannon + distancePeak
    timeTotal = math.sqrt((2 * heightTotal) / 9.81)
    result = speedHorizontal * timeTotal
    return result


def checkNumberInt(value):
    """
    Checks if the value is a number and will typecast to float.
    :param value: string value to check
    :return: float value
    """
    if value.isnumeric():
        return int(value)
    else:
        print("You did not enter the correct numbers!")
        newNum = input("Please enter a number: ")
        return checkNumberInt(newNum)


# --- MAIN --- #
while True:
    # -- inputs -- #
    choice = menu()
    choice = int(choice)
    if choice == 4:
        exit()
    elif choice == 1:
        height, speed = askNumbersScenario1()
    elif choice == 2:
        angle, speed = askNumbersScenario2()
    elif choice == 3:
        angle, speed, heightCannon = askNumbersScenario3()

    # -- Process -- #
    if choice == 1:
        answer = scenario1(height, speed)
    elif choice == 2:
        answer = scenario2(angle, speed)
    elif choice == 3:
        answer = scenario3(angle, speed, heightCannon)
    else:
        print("Something went wrong! Your menu choice doesn't exist!")

    answer = checkInt(answer)
    # -- Output -- #
    print(answer)