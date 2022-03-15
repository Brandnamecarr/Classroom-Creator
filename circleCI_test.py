# this file is testing to ensure that circleCI is configured properly.


def main():

    countdown = 10

    while countdown > 0:
        print("{}...".format(countdown))
        countdown = countdown - 1
    
    if countdown == 0:
        print("Countdown reached 0!")


main()