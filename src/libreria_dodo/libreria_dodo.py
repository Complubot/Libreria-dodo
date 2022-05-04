from machine import Pin, PWM, I2C
from utime import sleep_us, ticks_us, sleep
from micropython import const
import array, time
import rp2
import framebuf

# register definitions
SET_CONTRAST = const(0x81)
SET_ENTIRE_ON = const(0xA4)
SET_NORM_INV = const(0xA6)
SET_DISP = const(0xAE)
SET_MEM_ADDR = const(0x20)
SET_COL_ADDR = const(0x21)
SET_PAGE_ADDR = const(0x22)
SET_DISP_START_LINE = const(0x40)
SET_SEG_REMAP = const(0xA0)
SET_MUX_RATIO = const(0xA8)
SET_COM_OUT_DIR = const(0xC0)
SET_DISP_OFFSET = const(0xD3)
SET_COM_PIN_CFG = const(0xDA)
SET_DISP_CLK_DIV = const(0xD5)
SET_PRECHARGE = const(0xD9)
SET_VCOM_DESEL = const(0xDB)
SET_CHARGE_PUMP = const(0x8D)

class dodo:
    def __init__(self, tipo='dodo'):
        self.tipo = tipo
        self.rgb = Neopixel(5,0,2,'GRB')
        i2c = I2C(0, sda=Pin(0), scl=Pin(1)) #configuramos el I2C
        self.oled = SSD1306_I2C(128,64,i2c)       #configuramos la pantalla oled
        self.rojo = (255,0,0)
        self.verde = (0,255,0)
        self.azul = (0,0,255)
        self.amarillo = (255,255,0)
        self.cian = (0,255,255)
        self.magenta = (255,0,255)
        self.blanco = (255,255,255)
        self.apagado = (0,0,0)
        
        self.logo(self.tipo)
        
    #####################################################################
    # Función que muestra el logo en pantalla en funcion del tipo de placa
    #####################################################################
    def logo(self, tipo):
        
        #mostramos logo
        logo = bytearray(b'\x00\x00x\x00\x00\x00\x00\x00\x01\xfe\x00\x00\x00\x00\x00\x07\xff\x80\x00\x00\x00\x00\t\xff\x80\x00\x00\x00\x00\x0e\xc7\xc0\x00\x00\x00\x00\x08\xd3\xc0\x00\x00\x00\x00\x0f\xc7\xc0\x00\x00\x00?\x8f\xef\xc0\x00\x00\x00\x7f\xff\xff\xc0\x00\x00\x00\xff\xff\xff\x80\x00\x00\x00\xff\xff\xff\x80\x00\x00\x00\xff\xff\xfe\x00\x00\x00\x00\xff\xff\xfc\x00\x00\x00\x00?\xfex\x00\x00\x00\x00\x1f\xf1\xe0\x00\x00\x00\x00\x07\x83\xc0\x00\x00\x00\x00\x00\x07\x80\x00\x00\x00\x00\x00\x1f\x00\x00\x00\x00\x00\x00?\x0f\x80\x00\x00\x00\x00~\x7f\xfe\x01\x9c\x00\x00\xfe\xff\xff\x01\xb8\x00\x01\xff\xff\xff\xc1\xf7\x00\x01\xff\xff\xff\xf1\xff\x80\x03\xff\xff\xff\xfd\xff\x00\x03\xff\xff\xff\xff\xf0\x00\x07\xff\xff\xff\xff\xce\x00\x03\xff\xff\xff\xff\xff\x00\x03\xff\xff\xff\xff\xe7\x80\x01\xff\xff\xff\xff\xfc\x00\x00\x7f\xff\xff\xff\xdc\x00\x00\x7f\xff\xff\xffn\x00\x00?\xff\xff\xfef\x00\x00?\xff\xff\xfc \x00\x00\x0f\xff\xff\xf8\x00\x00\x00\x07\xff\xff\xf0\x00\x00\x00\x01\xff\xff\xf0\x00\x00\x00@\xff\xff\xe0\x00\x00\x00\xf8\x7f\xff\xc0\x00\x00\x01\xfe<\x7f\xe0\x00\x00\x03\x93\x9c\x03\xe0\x00\x00\x03\x90\xcc\x03\xf0\x00\x00\x03\x80t\x01\xf0\x00\x00\x01\x80\x1c\x00\xf0\x00\x00\x00\x00\x04\x008\x00\x00\x00\x00\x00\x00\x1c\x00\x00\x00\x00\x00\x00\x06 \x00\x00\x00\x00\x00\x03\xa0\x00\x00\x00\x00\x00\x01\xf0\x00\x00\x00\x00\x00\x008\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x00\x00\x00\x0f\x80\x00\x00\x00\x00\x00\x03\xc0\x00\x00\x00\x00\x00\x01\x80')
        fb = framebuf.FrameBuffer(logo,50,53, framebuf.MONO_HLSB)
        self.oled.fill(0)
        self.oled.blit(fb,32,0)
        
        #Mostramos texto en función del tipo de placa
        if tipo == 'lite':
            self.oled.text('DODO LITE',28,56,1)
        elif tipo == 'dodo':
            self.oled.text('DODO BOARD',20,56,1)
        self.oled.show()
        
        #juego de luces
        self.rgb.brightness(80)
        self.rgb.set_pixel(0,self.magenta)
        for x in range(0,4):
            sleep(0.1)
            self.rgb.rotate_right(1)
            self.rgb.show()
        
        for x in range(0,4):
            sleep(0.1)
            self.rgb.rotate_left(1)
            self.rgb.show()
        
        sleep(0.1)
        self.rgb.fill(self.apagado)
        self.rgb.show()
        self.oled.fill(0)
        self.oled.show()
    
    ###########################################################################
    # Función que espera a que se pulse el pulsador seleccionado por el usuario
    ###########################################################################
    def espera_pulsado(self, pulsador):
        pul = Pin(pulsador,Pin.IN)
    
        while pul.value() == 0:  #espera a que se pulse
            pass
        while pul.value() == 1:  #espera a que se suelte
            pass
    
    #Funcion convierte rangos
    def convert (self,x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min ) + out_min
    
    ###########################################################################
    # Funciones para controlar los motores en velocidad y dirección
    # La Dodo puede controlar hasta 4 motores y la Dodo Lite hasta 2
    # La velocidad va de -100 a 100
    ###########################################################################
    
    def mueve_motor(self,motor, vel):
        
        motor_1a = PWM(Pin(8))
        motor_1b = PWM(Pin(9))
        motor_2a = PWM(Pin(6))
        motor_2b = PWM(Pin(7))
        motor_1a.freq(1000)
        motor_1b.freq(1000)
        motor_2a.freq(1000)
        motor_2b.freq(1000)
        
        if vel > 100:
            vel = 100
        elif vel < -100:
            vel = -100
        
        if motor == 1:
            if vel == 0:
                motor_1a.duty_u16(65535)
                motor_1b.duty_u16(65535)
            elif vel > 0:
                motor_1a.duty_u16(self.convert(vel,1,100,1,65535))
                motor_1b.duty_u16(0)
            else:
                motor_1a.duty_u16(0)
                motor_1b.duty_u16(self.convert(vel,-1,-100,1,65535))
                
        if motor == 2:
            if vel == 0:
                motor_2a.duty_u16(65535)
                motor_2b.duty_u16(65535)
            elif vel > 0:
                motor_2a.duty_u16(self.convert(vel,1,100,1,65535))
                motor_2b.duty_u16(0)
            else:
                motor_2a.duty_u16(0)
                motor_2b.duty_u16(self.convert(vel,-1,-100,1,65535))
                
        if self.tipo == 'dodo':
            motor_3a = PWM(Pin(18))
            motor_3b = PWM(Pin(19))
            motor_4a = PWM(Pin(16))
            motor_4b = PWM(Pin(17))
            motor_3a.freq(1000)
            motor_3b.freq(1000)
            motor_4a.freq(1000)
            motor_4b.freq(1000)
            
            if motor == 3:
                if vel == 0:
                    motor_3a.duty_u16(65535)
                    motor_3b.duty_u16(65535)
                elif vel > 0:
                    motor_3a.duty_u16(self.convert(vel,1,100,1,65535))
                    motor_3b.duty_u16(0)
                else:
                    motor_3a.duty_u16(0)
                    motor_3b.duty_u16(self.convert(vel,-1,-100,1,65535))
                    
            if motor == 4:
                if vel == 0:
                    motor_4a.duty_u16(65535)
                    motor_4b.duty_u16(65535)
                elif vel > 0:
                    motor_4a.duty_u16(self.convert(vel,1,100,1,65535))
                    motor_4b.duty_u16(0)
                else:
                    motor_4a.duty_u16(0)
                    motor_4b.duty_u16(self.convert(vel,-1,-100,1,65535))
    
    def para_motor(self,motor):
        self.mueve_motor(motor,0)
        
    ###################################################################
    #Funciones para el control de los RGB
    ###################################################################
    def enciende_rgb(self,n_rgb,color):
        self.rgb.set_pixel(n_rgb,color)
        self.rgb.show()
    
    def fila_rgb(self,color):
        self.rgb.fill(color)
        self.rgb.show()
        
    def apaga_rgb(self,n_rgb):
        self.rgb.set_pixel(n_rgb,self.apagado)
        self.rgb.show()
    
    def degradado_rgb(self,color1,color2):
        self.rgb.set_pixel_line_gradient(0,4,color1,color2)
        self.rgb.show()
    
    ###################################################################
    #Funciones para el control de la pantalla
    ###################################################################
    
    def escribe_pantalla(self,texto,x,y):
        self.oled.fill_rect(x,y,127,y+8,0)
        self.oled.text(texto,x,y,1)
        self.oled.show()
        
    def borra_pantalla(self):
        self.oled.fill(0)
        self.oled.show()
        

    ###################################################################
    #Funcion para leer el ultrasonidos en cm en el pin seleccionado
    ###################################################################
                    
    def lee_us(self,pin):
        #enviamos un echo
        trig = Pin(pin,Pin.OUT)
        trig.off()        #esperamos a estibilizar el pin
        sleep_us(10)
        
        #mandamos un pulso
        trig.on()
        sleep_us(5)
        trig.off()
        
        echo = Pin(pin,Pin.IN)
        while echo.value() == 0:
            tiempo_inicial = ticks_us()
        while echo.value() == 1:
            tiempo_final = ticks_us()
        
        tiempo = tiempo_final-tiempo_inicial
        return round((0.03432*tiempo)/2,1)
    
##############################################################
# Clase para el control de los leds RGBs
##############################################################

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop().side(0)                       [T2 - 1]
    wrap()

class Neopixel:
    def __init__(self, num_leds, state_machine, pin, mode="RGB", delay=0.0001):
        self.pixels = array.array("I", [0 for _ in range(num_leds)])
        self.mode = set(mode)   # set for better performance
        
        self.sm = rp2.StateMachine(state_machine, ws2812, freq=8000000, sideset_base=Pin(pin))
        self.shift = {'R': ((mode.index('R') ^ 3) - 1) * 8, 'G': ((mode.index('G') ^ 3) - 1) * 8,
                      'B': ((mode.index('B') ^ 3) - 1) * 8, 'W': 0}
        self.sm.active(1)
        self.num_leds = num_leds
        self.delay = delay
        self.brightnessvalue = 255

    # Set the overal value to adjust brightness when updating leds
    def brightness(self, brightness=None):
        if brightness == None:
            return self.brightnessvalue
        else:
            if brightness < 1:
                brightness = 1
        if brightness > 255:
            brightness = 255
        self.brightnessvalue = brightness

    # Create a gradient with two RGB colors between "pixel1" and "pixel2" (inclusive)
    # Function accepts two (r, g, b) / (r, g, b, w) tuples
    def set_pixel_line_gradient(self, pixel1, pixel2, left_rgb_w, right_rgb_w):
        if pixel2 - pixel1 == 0:
            return
        right_pixel = max(pixel1, pixel2)
        left_pixel = min(pixel1, pixel2)

        for i in range(right_pixel - left_pixel + 1):
            fraction = i / (right_pixel - left_pixel)
            red = round((right_rgb_w[0] - left_rgb_w[0]) * fraction + left_rgb_w[0])
            green = round((right_rgb_w[1] - left_rgb_w[1]) * fraction + left_rgb_w[1])
            blue = round((right_rgb_w[2] - left_rgb_w[2]) * fraction + left_rgb_w[2])
            # if it's (r, g, b, w)
            if len(left_rgb_w) == 4 and 'W' in self.mode:
                white = round((right_rgb_w[3] - left_rgb_w[3]) * fraction + left_rgb_w[3])
                self.set_pixel(left_pixel + i, (red, green, blue, white))
            else:
                self.set_pixel(left_pixel + i, (red, green, blue))

    # Set an array of pixels starting from "pixel1" to "pixel2" (inclusive) to the desired color.
    # Function accepts (r, g, b) / (r, g, b, w) tuple
    def set_pixel_line(self, pixel1, pixel2, rgb_w):
        for i in range(pixel1, pixel2 + 1):
            self.set_pixel(i, rgb_w)

    # Set red, green and blue value of pixel on position <pixel_num>
    # Function accepts (r, g, b) / (r, g, b, w) tuple
    def set_pixel(self, pixel_num, rgb_w):
        pos = self.shift

        red = round(rgb_w[0] * (self.brightness() / 255))
        green = round(rgb_w[1] * (self.brightness() / 255))
        blue = round(rgb_w[2] * (self.brightness() / 255))
        white = 0
        # if it's (r, g, b, w)
        if len(rgb_w) == 4 and 'W' in self.mode:
            white = round(rgb_w[3] * (self.brightness() / 255))

        self.pixels[pixel_num] = white << pos['W'] | blue << pos['B'] | red << pos['R'] | green << pos['G']

    # Rotate <num_of_pixels> pixels to the left
    def rotate_left(self, num_of_pixels):
        if num_of_pixels == None:
            num_of_pixels = 1
        self.pixels = self.pixels[num_of_pixels:] + self.pixels[:num_of_pixels]

    # Rotate <num_of_pixels> pixels to the right
    def rotate_right(self, num_of_pixels):
        if num_of_pixels == None:
            num_of_pixels = 1
        num_of_pixels = -1 * num_of_pixels
        self.pixels = self.pixels[num_of_pixels:] + self.pixels[:num_of_pixels]

    # Update pixels
    def show(self):
        # If mode is RGB, we cut 8 bits of, otherwise we keep all 32
        cut = 8
        if 'W' in self.mode:
            cut = 0
        for i in range(self.num_leds):
            self.sm.put(self.pixels[i], cut)
        time.sleep(self.delay)

    # Set all pixels to given rgb values
    # Function accepts (r, g, b) / (r, g, b, w)
    def fill(self, rgb_w):
        for i in range(self.num_leds):
            self.set_pixel(i, rgb_w)
        time.sleep(self.delay)
        
class SSD1306(framebuf.FrameBuffer):
    def __init__(self, width, height, external_vcc):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.pages = self.height // 8
        self.buffer = bytearray(self.pages * self.width)
        super().__init__(self.buffer, self.width, self.height, framebuf.MONO_VLSB)
        self.init_display()

    def init_display(self):
        for cmd in (
            SET_DISP | 0x00,  # off
            # address setting
            SET_MEM_ADDR,
            0x00,  # horizontal
            # resolution and layout
            SET_DISP_START_LINE | 0x00,
            SET_SEG_REMAP | 0x01,  # column addr 127 mapped to SEG0
            SET_MUX_RATIO,
            self.height - 1,
            SET_COM_OUT_DIR | 0x08,  # scan from COM[N] to COM0
            SET_DISP_OFFSET,
            0x00,
            SET_COM_PIN_CFG,
            0x02 if self.width > 2 * self.height else 0x12,
            # timing and driving scheme
            SET_DISP_CLK_DIV,
            0x80,
            SET_PRECHARGE,
            0x22 if self.external_vcc else 0xF1,
            SET_VCOM_DESEL,
            0x30,  # 0.83*Vcc
            # display
            SET_CONTRAST,
            0xFF,  # maximum
            SET_ENTIRE_ON,  # output follows RAM contents
            SET_NORM_INV,  # not inverted
            # charge pump
            SET_CHARGE_PUMP,
            0x10 if self.external_vcc else 0x14,
            SET_DISP | 0x01,
        ):  # on
            self.write_cmd(cmd)
        self.fill(0)
        self.show()

    def poweroff(self):
        self.write_cmd(SET_DISP | 0x00)

    def poweron(self):
        self.write_cmd(SET_DISP | 0x01)

    def contrast(self, contrast):
        self.write_cmd(SET_CONTRAST)
        self.write_cmd(contrast)

    def invert(self, invert):
        self.write_cmd(SET_NORM_INV | (invert & 1))

    def show(self):
        x0 = 0
        x1 = self.width - 1
        if self.width == 64:
            # displays with width of 64 pixels are shifted by 32
            x0 += 32
            x1 += 32
        self.write_cmd(SET_COL_ADDR)
        self.write_cmd(x0)
        self.write_cmd(x1)
        self.write_cmd(SET_PAGE_ADDR)
        self.write_cmd(0)
        self.write_cmd(self.pages - 1)
        self.write_data(self.buffer)


class SSD1306_I2C(SSD1306):
    def __init__(self, width, height, i2c, addr=0x3C, external_vcc=False):
        self.i2c = i2c
        self.addr = addr
        self.temp = bytearray(2)
        self.write_list = [b"\x40", None]  # Co=0, D/C#=1
        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        self.temp[0] = 0x80  # Co=1, D/C#=0
        self.temp[1] = cmd
        self.i2c.writeto(self.addr, self.temp)

    def write_data(self, buf):
        self.write_list[1] = buf
        self.i2c.writevto(self.addr, self.write_list)
    
