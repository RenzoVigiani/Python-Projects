import machine
import time

def toggle(p):
   p.value(not p.value())
   
# ----- SALIDAS ---------
Led_Verde_grande = machine.Pin(15, machine.Pin.OUT)
Led_Verde_chico = machine.Pin(16, machine.Pin.OUT)
Led_senal_rojo = machine.Pin(2, machine.Pin.OUT)
Led_senal_verde = machine.Pin(10)
Buzzer = machine.Pin(5, machine.Pin.OUT)

# ------ SPI / I2C ----------
Pin_MISO = machine.Pin(12)
Pin_MOSI = machine.Pin(13)
Pin_SCLK = machine.Pin(14)
Pin_SDA  = machine.Pin(4)

# -------- SERIAL --------------
'''Pin_Flash = machine.Pin(0)
Pin_TXD0 = machine.Pin(1, machine.Pin.OUT)
Pin_RXD0 = machine.Pin(3, machine.Pin.IN)
'''
Led_Verde_chico.off()
Led_Verde_grande.off()
Led_senal_rojo.on()
time.sleep_ms(500)        
Led_senal_verde.off()
time.sleep_ms(500)        

for i in range(0,10):
    if i==10:
        break
    toggle(Led_senal_rojo)
    toggle(Led_Verde_chico)
    toggle(Led_Verde_grande)
    time.sleep_ms(500)        
Buzzer.on()
time.sleep_ms(100)        
Buzzer.off()
