"""Circuit Playground LED control module."""
# pylint: disable=import-error
from adafruit_circuitplayground import cp

print("Hello World!")
value = 255
while(1):

    cp.pixels[0] = (0, 0, value)
    cp.pixels[1] = (0, 0, value)
    cp.pixels[2] = (0, 0, value)
    cp.pixels[3] = (0, 0, value)
    cp.pixels[4] = (0, 0, value)
    cp.pixels[5] = (0, 0, value)
    cp.pixels[6] = (0, 0, value)
    cp.pixels[7] = (0, 0, value)
    cp.pixels[8] = (0, 0, value)
    cp.pixels[9] = (0, 0, value)
    value = value - 1
    if value < 0:
        value = 255
