# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials UART Serial example"""
import board
import busio
import digitalio

# For most CircuitPython boards:

uart = busio.UART(board.C4, board.C3, baudrate=9600)

while True:
	uart.write('Hello World')

