
Instalation
===========

If you are using raspbian with desktop you dont need to install anything

If you are using raspbian lite then you will need to install RPi.GPIO python module

> sudo apt-get update

>sudo apt-get install rpi.gpio

using the program
=================

Select color you want

Select style you want

To stop blinking press CTRL+C if led is still truned on run program again and select color that is truned on and select style Off

If led is truned on run program select color that is truned on and select style Off

Circuit
=======

RGB led is recomended becose if you use seperate leds for every color, color combinations wont work

Connect red LED to pin 14, green to pin 15 and blue to pin 18

You may notice that the red LED is glowing while system is booting, if you dont want that replace pins and replace output pins in code

You ALWAYS need resistor conected between raspberry pi and positive LED leg, i used 220 ohm resistor in this project

Ground leg connect to GND pin on raspberry pi
