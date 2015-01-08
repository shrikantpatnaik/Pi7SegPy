Raspberry Pi 7 Segment Display Library
======================================

This is a simple library to use M 7 segment displays connected to N
\*595 Shift registers. All pin numbers are based on the GPIO.BCM
numbering scheme. You will need the RPi.GPIO module available.

This module also requires my
`PiShiftPy <http://github.com/shrikantpatnaik/PiShiftPy>`__ library.

Basic Usage
-----------

Defaults
~~~~~~~~

| 595 Data: 18
| 595 Clock: 23
| 595 Latch: 24
| No of 595's: 1
| No of Displays on each 595: 1
| Displays are Common Cathode: False

Code
~~~~

.. code:: python

    import Pi7SegPy as Pi7Seg

    Pi7Seg.init()
    while True:
        Pi7Seg.show([1]) # Display 1 on a single 7 segment display connected to 1 Shift register

Advanced Usage
--------------

.. code:: python

    import Pi7SegPy as Pi7Seg

    Pi7Seg.init(17,27,22,2,4) # Initialize with Data:GPIO17, Clock:GPIO27, Latch:GPIO22, with 2 shift registers and 4 7 segment displays on each register

    while True:
        Pi7Seg.show([1,2,3,4,5,6,7,8], [1,2,5]) # Display 12345678 on 8 displays connected to 2 registers with dots enabled on the 1st, 2nd and 5th Digit

Available Characters
--------------------

0,1,2,3,4,5,6,7,8,A,b,C,c,d,E,F,H,h,L,n,I,O,o,P,S, (space)
