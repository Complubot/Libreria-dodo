# Librería para las placas dodo y dodo lite
Esta librería creada por **[Complubot](https://complubot.com/)** ha sido desarrollada para programar las placas dodo y dodo lite basadas en una Raspberry Pi Pico en MicroPython. Es una librería en desarrollo y que cada vez incluirá más funcionalidades para estas placas. 
A continuación os dejamos un breve resumen de como la librería y de que funciones dispone.

## Incluir la librería y definir la placa
Después de instalar la librería para poder utilizarla debemos importar la clase **dodo** que nos permite usar las funciones para controlar la placa. El objeto `mi_robot` puede llamarse como queramos mientras no tenga espacios.

Así definiríamos una placa **dodo**: 

```python
from complubot.libreria_dodo import dodo #importamos el modulo dodo de la libreria

mi_robot = dodo() #definimos nuestra placa dodo
```
Así definiríamos una placa **dodo lite**: 

```python
from complubot.libreria_dodo import dodo #importamos el modulo dodo de la libreria

mi_robot = dodo('lite') #definimos nuestra placa dodo lite
```
## Controlar motores
Las placas dodo y dodo lite tienen drivers de motores para poder controlar motores de corriente continua de hasta 1A. La placa **dodo** puede controlar 4 motores y la placa **dodo lite** puede controlar 2 motores. Para poder controlar los motores se han desarrollado varias funciones:
### Función mueve_motor(motor,velocidad)
La función mueve_motor cuenta con 2 parámetros:

 - **motor**: Es el número del motor que queremos mover. Van del 1 al 4 en la **dodo** y del 1 al 2 en la **dodo lite**.

 - **velocidad**: Es la velocidad a la que queremos que vaya el motor porcentualmente. La velocidad tiene un rango de -100 a 100. El signo indica el sentido de giro de nuestro motor si es negativo retrocede y si es positivo avanza.
 
Ejemplo de programa donde dos motores avanzan 1 segundo al 80%, retroceden 1 segundo al 50% y se paran durante 1 segundo. 
```python
from complubot.libreria_dodo import dodo
from utime import sleep

mi_robot = dodo()

while True:
    mi_robot.mueve_motor(1,80)
    mi_robot.mueve_motor(2,80)
    sleep(1)
    mi_robot.mueve_motor(1,-50)
    mi_robot.mueve_motor(2,-50)
    sleep(1)
    mi_robot.mueve_motor(1,0)
    mi_robot.mueve_motor(2,0)
    sleep(1)
```
### Función para_motor(motor)
Para detener un motor tenemos la función para_motor, esta función detiene en seco nuestro motor. La función para_motor cuenta con 1 parámetro:

 - **motor**: Es el número del motor que queremos parar. Van del 1 al 4 en la **dodo** y del 1 al 2 en la **dodo lite**.

Ejemplo de programa donde dos motores avanzan 2 segundo al 100% y se detienen 3 segundos.
```python
from complubot.libreria_dodo import dodo
from utime import sleep

mi_robot = dodo()

while True:
    mi_robot.mueve_motor(1,100)
    mi_robot.mueve_motor(2,100)
    sleep(2)
    mi_robot.para_motor(1)
    mi_robot.para_motor(2)
    sleep(3)
```
## Controlar leds RGB
En lado izquierdo de la placa tenemos 5 leds RGB inteligentes conectados todos en serie a un único pin de nuestra placa. El color de estos leds se pueden controlar de manera independiente y los podemos dar mucha utilidad, por ejemplo: generar códigos de colores, estado del robot, mostrar información de los sensores, identificar nuestro robot,  etc.
Para controlar estos leds disponemos de 4 funciones:
### enciende_rgb(posición del led, color)
Esta función nos permite encender un led RGB del color que queramos, cuenta con dos parámetros de entrada:
- **posición del led**: Es la posición del led que queremos controlar, la placa dodo cuenta con 5 leds RGB numerados del 0 al 4. La posición 0 corresponde con el led superior mientras que la 4 corresponde al led inferior.

 - **color**: El color en un led RGB esta definido por la cantidad de luz de cada una de sus componentes (rojo, verde ,azul). La librería dispone de 8 colores predefinidos que son: rojo, verde, azul, amarillo, cian, magenta, blanco, apagado.

La función la podemos usar de la siguiente manera:
```python
from complubot.libreria_dodo import dodo

mi_robot = dodo()

mi_robot.enciende_rgb(0,mi_robot.rojo)
mi_robot.enciende_rgb(1,mi_robot.verde)
mi_robot.enciende_rgb(2,mi_robot.azul)
mi_robot.enciende_rgb(3,mi_robot.magenta)
mi_robot.enciende_rgb(4,mi_robot.amarillo)
```
Este programa enciende cada uno de los leds RGB de un color distinto. 

También podemos usar colores propios definiendo una tupla de 3 valores que vayan de 0 a 255, cada valor corresponde a una de las componentes del led RGB:
```python
from complubot.libreria_dodo import dodo

mi_robot = dodo()

naranja = (255,124,0)
morado = (158,0,255)

mi_robot.enciende_rgb(0,naranja)
mi_robot.enciende_rgb(1,morado)
```
En esta pagina web puedes seleccionar de forma sencilla el color que desees y te da los códigos RGB: https://htmlcolorcodes.com/es/

### fila_rgb( color)
Esta función enciende toda la fila de leds del mismo color, cuenta con un parámetro de entrada:

 - **color**: El color en un led RGB esta definido por la cantidad de luz de cada una de sus componentes (rojo, verde ,azul). La librería dispone de 8 colores predefinidos que son: rojo, verde, azul, amarillo, cian, magenta, blanco, apagado.
Se usa de la siguiente manera:
```python
from complubot.libreria_dodo import dodo

mi_robot = dodo()

mi_robot.fila_rgb(0,mi_robot.cian)
```
Enciende toda la fila de color cian.

### apaga_rgb( posición del led)
Esta función apaga el led indicado, cuenta con un parámetro de entrada:

- **posición del led**: Es la posición del led que queremos controlar, la placa dodo cuenta con 5 leds RGB numerados del 0 al 4. La posición 0 corresponde con el led superior mientras que la 4 corresponde al led inferior.

Se usa de la siguiente manera:
```python
from complubot.libreria_dodo import dodo
from utime import sleep

mi_robot = dodo()

while True:
    mi_robot.enciende_rgb(0,mi_robot.verde)
    sleep(1)
    mi_robot.apaga_rgb(0)
    sleep(1)
```
Hace parpadear el led en verde, esta 1 segundo encendido y 1 segundo apagado.

### degradado_rgb(color1, color2)
Esta función nos permite hacer un degrado entre el primer led y el ultimo, cuenta con dos parámetros de entrada:
 - **color1**: El color en un led RGB esta definido por la cantidad de luz de cada una de sus componentes (rojo, verde ,azul). La librería dispone de 8 colores predefinidos que son: rojo, verde, azul, amarillo, cian, magenta, blanco, apagado.

 - **color2**: El color en un led RGB esta definido por la cantidad de luz de cada una de sus componentes (rojo, verde ,azul). La librería dispone de 8 colores predefinidos que son: rojo, verde, azul, amarillo, cian, magenta, blanco, apagado.

La función la podemos usar de la siguiente manera:
```python
from complubot.libreria_dodo import dodo

mi_robot = dodo()

mi_robot.degradado_rgb(mi_robot.amarillo,mi_robot.magenta)
```
Este programa hace una transición de color entre el amarillo y el magenta y lo muestra en los leds RGB.

## Controlar pantalla oled
Nuestro robot cuenta con una pantalla oled monocroma de 128x64 pixeles. En esta pantalla podemos mostrar texto y variables de forma sencilla gracias a las siguientes funciones:

### escribe_pantalla(texto, x ,y)
Esta función nos permite escribir texto en cualquier punto de nuestra pantalla, cuenta con tres parámetros de entrada:
 - **texto**: Es el texto que queremos mostrar, tiene que ser de tipo **string** y como mucho podrá ser de 16 caracteres de largo. Cada línea de la pantalla cuenta con 128 pixeles y cada carácter ocupa 8 pixeles de alto y de ancho. Con lo cual podemos escribir 8 líneas de 16 caracteres como máximo en nuestra pantalla.

 - **x**: Es la posición horizontal en la que empieza nuestro texto a escribirse. Va de 0 a 127 y comienza en la esquina superior izquierda de la pantalla.

 - **y**: Es la posición vertical en la que empieza nuestro texto a escribirse. Va de 0 a 63 y comienza en la esquina superior izquierda de la pantalla.

La función la podemos usar de la siguiente manera:
```python
from complubot.libreria_dodo import dodo

mi_robot = dodo()

mi_robot.escribe_pantalla('Complubot',28,28)
mi_robot.escribe_pantalla('Placa Dodo',24,36)
```
Este programa escribe en una posición centrada la palabra *Complubot* y justo debajo *Placa Dodo*.
Para mostrar una variable numérica debemos convertirla en un **string**, de la siguiente manera:

```python
from complubot.libreria_dodo import dodo

mi_robot = dodo()

numero = 245

mi_robot.escribe_pantalla(str(numero),28,28)
```

### borra_pantalla()
Esta función nos permite borrar completamente la pantalla, no cuenta con parámetros de entrada.

La función la podemos usar de la siguiente manera:
```python
from complubot.libreria_dodo import dodo
from utime import sleep

mi_robot = dodo()

mi_robot.escribe_pantalla('Complubot',28,28)
sleep(2)
mi_robot.borra_pantalla()
mi_robot.escribe_pantalla('Placa Dodo',24,28)
```
Este programa escribe en una posición centrada la palabra *Complubot*  durante 2 segundos, luego borra la pantalla y justo en la misma línea escribe *Placa Dodo*.

## Leer sensores

### lee_us( Pin)
Esta función nos permite saber la distancia que marca el modulo de ultrasonidos en cm, cuenta con un parámetro de entrada:

 - **Pin**: Pin hace referencia al puerto en el que hemos conectado nuestro modulo ultrasonidos.
 - 
Se usa de la siguiente manera:
```python
from complubot.libreria_dodo import dodo
from utime import sleep

mi_robot = dodo()

while True:
    distancia = mi_robot.lee_us(10)
    mi_robot.escribe_pantalla(str(distancia),28,28)
    sleep(0.1)
```
Este programa lee el sensor de ultrasonidos conectado al puerto **GP10** y lo muestra en pantalla, hace esto cada 0,1 segundos .
