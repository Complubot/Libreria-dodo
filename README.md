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
## Mover nuestro robot
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
