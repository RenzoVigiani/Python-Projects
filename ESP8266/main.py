import machine
import time

# ----- SALIDAS ---------
Led_Verde_grande = machine.Pin(15, machine.Pin.OUT)
Led_Verde_chico = machine.Pin(16, machine.Pin.OUT)
Led_senal_rojo = machine.Pin(2, machine.Pin.OUT)
#Led_senal_verde = machine.Pin(9, machine.Pin.OUT)
Buzzer = machine.Pin(5, machine.Pin.OUT)

# ------ SPI / I2C ----------
Pin_MISO = machine.Pin(12, machine.Pin.IN)
Pin_MOSI = machine.Pin(13, machine.Pin.OUT)
Pin_SCLK = machine.Pin(14, machine.Pin.OUT)
Pin_SDA  = machine.Pin(4, machine.Pin.OUT)

# -------- SERIAL --------------
Pin_Flash = machine.Pin(0, machine.Pin.IN)
Pin_TXD0 = machine.Pin(1, machine.Pin.OUT)
Pin_RXD0 = machine.Pin(3, machine.Pin.IN)


for i in range(0,100):
    if i%2==0:
        Led_Verde_chico.off()
        Led_Verde_grande.on()
        Led_senal_rojo.off()
    if i%2!=0:
        Led_Verde_chico.on()
        Led_Verde_grande.off()
        Led_senal_rojo.on()
    time.sleep_ms(500)    
    
#Led_senal_verde.on()

