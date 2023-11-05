from board import SCL, SDA
import busio
import time
import digitalio
import board

# Import the SSD1306 module.
import adafruit_ssd1306

WIDTH = 128
HEIGHT = 64

led_aa = digitalio.DigitalInOut(board.C6)
led_aa.direction = digitalio.Direction.OUTPUT
led_bb = digitalio.DigitalInOut(board.C7)
led_bb.direction = digitalio.Direction.OUTPUT


# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
# Alternatively you can change the I2C address of the device with an addr parameter:
#display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x31)

# Clear the display.  Always call show after changing pixels to make the display
# update visible!
x = 0

while True:

	display.fill(0)

# Set a pixel in the origin 0,0 position.
	display.pixel(0, 0, 1)
# Set a pixel in the middle position.
	display.pixel(WIDTH//2, HEIGHT//2, 1)
# Set a pixel in the opposite far end corner position.
	display.pixel(WIDTH - 1, HEIGHT - 1, 1)

	display.text("HELLO", x, 10,1)
	x = x + 7

	display.circle(32,32,10,1)
	led_aa.value = (x % 2 == 0)
	led_bb.value = (x % 2 != 0)
	x %= WIDTH
	display.show()
	time.sleep(0.005)


