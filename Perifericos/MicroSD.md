# Almacenamiento - MicroSD


El modulo de almacenamiento se gestiono en mycropython a traves de la libreria de servicios basicos de "sistema operativo" **OS** integrada y una libreria personalizada para administrar la tarjeta microSD a traves del protocolo SPI pues los pines de la microSD no se conectaron a traves de los dedicados del bus SPI por ende no es posible el uso de la libreria **SDcard** integrada en **Machine**, en su lugar se utilizo una implementacion que hace uso del metodo **SOFTSPI** en la libreria **SPI** integrada en **Machine** para gestionar el protocolo SPI a traves de software.

Para poder implementar la libreria personalizada se debe crear una clase que inicialice la tarjeta microSD y cuente con los metodos **readblocks**, **writeblocks** y **ioctl** necesarios para su utilizacion con la libreria **OS**, adicionalmente se deben crear los metodos necesarios para que las funciones mencionadas anteriormente puedan interactuar con la tarjeta microSD a traves del protocolo SPI. La jerarquia de comunicacion y metodos implementados para la comunicacion entre **OS** y la microSD se puede observar en el esquema a continacion:

<img src="./Imagenes/SDlibreria.png" alt='Jerarquia de metodos y librerias del modulo de almacenamiento' width="1000px"/>

Como se puede observar en el esquema de funciones, el protocolo SPI es el nivel de comunicacion mas bajo en la jerarquia teniendo una conexion directa con la tarjeta microSD, su implementacion en codigo respectivamente se hace utilizando el metodo **SOFTSPI** y  declarando como argumento los pines respectivos donde se realizara su comunicacion (MOSI, MISMO, CLK)(CS se gestiona independientemente) por lo cual una vez declarados los puertos se configura la cantidad de baudios con la que se comunicara el protocolo. una vez configurado el protocolo se hace uso de los metodos **spi.write**, **spi.read**, **spi.readinto** y **spi.write_readinto** para enviar y recibir datos incluso al mismo tiempo.

Una vez teniendo las funciones basicas de comunicacion del protocolo SPI, se necesita un metodo que permita enviar comandos a la tarjeta MicroSD para que pueda realizar diferentes funciones tanto de lectura como de escritura, de modo que generalmente las tarjetas del tipo SD poseen la siguiente estructura en la linea de comandos:

| Byte1 | Byte1 | Byte1    | Byte2-5   | Byte6 | Byte6 |
|-------|-------|----------|-----------|-------|-------|
| 7     | 6     |   5-0    |   31-0    |   7   | 0     |
| 0     | 1     |  Comand  | Arguments | CRC   | 1     |

Teniendo la estructura de datos necesaria se declara un metodo que reciba los comandos y argumentos que se deseen enviar a traves de un buffer para luego utilizar el metodo spi.write y enviar dicha informacion a la tarjeta microSD de modo que luego se reciba una respuesta de un byte la cual sera retornada por el metodo, en caso de no recibir respuesta dentro de un tiempo determinado el metodo retorna -1.

Una vez determinada una funcion basica para el envio de comandos de la tarjeta microSD es necesario generar las funciones basicas para enviar y leer datos las cuales se reflejan en **readinto**, **write** y **write_token**. luego de definir las comunicaciones basicas es necesario inicializar la tarjeta microSD a traves de comandos que permitan iniciar la tarjeta microSD, obtener la version de la tarjeta, obtener el numero de sectores de la tarjeta y ajustar la longitud de los bloques a 512 bytes con el fin de que el sistema unicamente se encargue de escribir y recibir la informacion que necesita, por esto se declaran 3 funciones especificas de bloques necesarias para interactuar con los bloques de la tarjeta y almacenar/leer datos de la misma, estos bloques como se ha visto corresponden a **readblocks**, **writeblocks** y **ioctl** de modo que a traves de comandos de escritura/lecturas de uno o multiples bloques se envia/lee la informacion necesaria en la tarjeta microSD. 

con todos estos metodos definidos se puede controlar la tarjeta microSD a traves de la libreria **OS**, simplificando en modulos superiores el uso de comandos basicos de un sistema de archivos.