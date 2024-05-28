
import constants

# Import the math module here
import math

height = int(input('Height in meters: '))  # Meters from planet


if __name__ == '__main__':
    print('Earth:', math.sqrt(2 * height / constants.earth_g), 'seconds')
    print('Mars:', math.sqrt(2 * height / constants.mars_g), 'seconds')
