from machine import Pin, I2C
import ssd1306

def connect_to(ssid: str, passwd: str) -> str:

    
    import network
    from time import sleep
    
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(ssid, passwd)
        while not sta_if.isconnected():
            sleep(.05)
    
    return sta_if.ifconfig()[0]  


ip_address = connect_to("Cooperadora Alumnos", "")
print("IP:", ip_address)


i2c = I2C(0, scl=Pin(22), sda=Pin(21))


oled = ssd1306.SSD1306_I2C(128, 32, i2c)

oled.fill(0)

oled.text("IP:", 0, 0)
oled.text(ip_address, 0, 10)

oled.show()