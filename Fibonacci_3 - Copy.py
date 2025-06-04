from machine import Pin
import time

#led_pins = [10, 11, 12, 13, 18, 19, 20, 21]
led_pins = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

def fibonacci():
    """Generates Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def binary_to_led(number):
    
    for i in range(len(led_pins)):
        if (number >> i) & 1:  
            leds[i].value(1)  
        else:
            leds[i].value(0)  

fib_gen = fibonacci()
count = 0

while True:
    fib_num = next(fib_gen)
    print(f"Fibonacci number: {fib_num}")

    binary_to_led(fib_num)  
    time.sleep(2)  

    #Optionally, reset the LEDs after displaying
#     for led in leds:
#         led.value(0)
#     time.sleep(1)