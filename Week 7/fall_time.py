
import math
from constants import earth_g, mars_g

# Get the height from the user
height = int(input('Height in meters: '))  # Meters from planet

# Calculate and print the time to fall from the given height on Earth and Mars
if __name__ == '__main__':
    earth_time = math.sqrt(2 * height / earth_g)
    mars_time = math.sqrt(2 * height / mars_g)
    print(f'Earth: {earth_time:.2f} seconds')
    print(f'Mars: {mars_time:.2f} seconds')

