# Raspberry Pi 3 GPIO

## Note
This document is written in markdown. You can read a rendered version visiting
the SIMON GitHub repository <https://github.com/rzbrk/simon>. Alternatively,
you can render the markdown by using a tool like [Grip -- GitHub Readme Instant Preview](https://github.com/joeyespo/grip).

## Raspberry Pi 3 GPIO Assignment
| Usage | Pin ID | Pin No | Pin No | Pin ID | Usage |
|-------|:------:|:------:|:------:|:------:|-------|
| IMU VCC | 3.3V PWR | 1 | 2 | 5V PWR | NC |
| IMU SDA | GPIO2 (SDA1, I2C) | 3 | 4 | 5V PWR | VRM VCC |
| IMU SCL | GPIO3 (SCL1, I2C) | 5 | 6 | GND | VRM GND |
| NC | GPIO4 (GPIO_GCLK) | 7 | 8 | GPIO14 (UART_TXD0) | VRM RX |
| IMU GND | GND | 9 | 10 | GPIO15 (UART_RXD0) | VRM TX |
| NC | GPIO17 (GPIO_GEN0) | 11 | 12 | GPIO18 (GPIO_GEN1) | NC |
| NC | GPIO27 (GPIO_GEN2) | 13 | 14 | GND | NC |
| NC | GPIO22 (GPIO_GEN3) | 15 | 16 | GPIO23 (GPIO_GEN4) | Display CS (Chip Select) |
| Display VCC + Display LED | 3.3V PWR | 17 | 18 | GPIO24 (GPIO_GEN5) | Display CD (Command/Data) |
| Display MOSI | GPIO10 (SPI0_MOSI) | 19 | 20 | GND | NC |
| Display MISO | GPIO9 (SPI0_MISO) | 21 | 22 | GPIO25 (GPIO_GEN6) | NC |
| Display SCLK | GPIO11 (SPI0_CLK) | 23 | 24 | GPIO8 (SPI_CE0_N) | NC |
| Display GND | GND | 25 | 26 | GPIO7 (SPI_CE1_N) | NC |
| NC | IS_SD (I2C_EEPROM) | 27 | 28 | IS_SC (I2C_EEPROM) | NC |
| NC | GPIO5 | 29 | 30 | GND | NC |
| NC | GPIO6 | 31 | 32 | GPIO12 | NC |
| NC | GPIO13 | 33 | 34 | GND | NC |
| NC | GPIO19 | 35 | 36 | GPIO16 | NC |
| NC | GPIO26 | 37 | 38 | GPIO20 | NC |
| NC | GND | 39 | 40 | GPIO21 | NC |


