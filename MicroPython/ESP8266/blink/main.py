# Complete project details at https://RandomNerdTutorials.com
import machine
from machine import Pin
import time

def toggle(p):
       p.value(not p.value())
# Configurar GPIO
#RST_PIN = Pin(30, Pin.IN) # RST-PIN für RC522 - RFID - SPI - Modul GPIO5
#SS_PIN = Pin(4, Pin.OUT) # SDA-PIN für RC522 - RFID - SPI - Modul GPIO4  4

OFFSET_ZERO = 0
OFFSET_16 = 16 
OFFSET_32 = 32
OFFSET_48 = 48
#define MIFARECLASSIC 1
#define NTAG21x 2
#define KEY_A  1

BUZZER = Pin(5,Pin.OUT)
LEDVERDE = Pin(16,Pin.OUT) #Logica positiva
LEDSENALROJO = Pin(2,Pin.OUT) # lógica negativa
LEDSENALVERDE = Pin(10) #Logica negativa
LEDSENALVERDEGRANDE = Pin(15,Pin.OUT) #Logica positiva

i=0
while i<22:
  if i%2==0:
#    LEDSENALVERDE.off()
    LEDSENALROJO.off()
    LEDSENALVERDEGRANDE.on()
    LEDVERDE.on()
    BUZZER.off()
  if i%2!=0:
#    LEDSENALVERDE.off()
    LEDSENALROJO.on()
    LEDVERDE.off()
    LEDSENALVERDEGRANDE.off()
#    BUZZER.on()
  time.sleep_ms(500)
  i+=1
  if i==22:
    print(i)
    LEDSENALROJO.on()
    LEDSENALVERDE.on()
    time.sleep_ms(1000)
    LEDSENALVERDE.off()
    time.sleep_ms(1000)
    LEDSENALVERDE.on()