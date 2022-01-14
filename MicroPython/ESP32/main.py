import machine
import time


# Declaración de variables   
val_eeprom = 64
datos_eeprom = [val_eeprom]
temp=[val_eeprom]
datoTAG=[val_eeprom]


# ----- SALIDAS ---------
Led_Verde_grande = machine.Pin(15, machine.Pin.OUT)
Led_Verde_chico = machine.Pin(16, machine.Pin.OUT)
Led_senal_rojo = machine.Pin(2, machine.Pin.OUT)
Led_senal_verde = machine.Pin(10)
Buzzer = machine.Pin(23, machine.Pin.OUT)

# ------ SPI / I2C ----------
Pin_MISO = machine.Pin(12)
Pin_MOSI = machine.Pin(13)
Pin_SCLK = machine.Pin(14)
Pin_SDA  = machine.Pin(4)

# Definición de funciones
#------ toggle ----------
def toggle(p):
   p.value(not p.value())
# ------- tagOK ------
def tagOK():
    Led_Verde_chico.on()
    Buzzer.on()
    time.sleep_ms(200)
    Buzzer.off()
    Led_Verde_chico.off()

# ------- tagERROR ------
def tagERROR():
    Led_senal_rojo.on() # led rojo apagado
    Buzzer.off() # Buzzer apagado
    for i in range(6): # hacer titilar 3 veces rapido
        toggle(Led_senal_rojo)
        toggle(Buzzer)
        time.sleep_ms(150)

# ------ initBuffer -----
def initBuffer():
    for i in range(val_eeprom): # val_eeprom = 64
        datos_eeprom[i] = 0
        temp[i] = 0
        datoTAG[i]=0
# ------ clearBuffData----
def clearBuffData():
    for i in range(val_eeprom):
        datoTAG[i]=0        


# Main
for i in range (0,100,5):
    if i==35:
        tagERROR()
    if i==90:
        tagOK
    print(i)
    time.sleep_ms(100)
