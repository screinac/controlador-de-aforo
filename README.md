# Sistema Controlador de Aforo

Descripcion (Reemplazar por texto)

## Componentes
### Dispositivo - Base:
- ESP32-WROOM-32
- FT232RL o CP2102
### Dispositivo - Extras:


## Funcionalidades

### Funciones - Base:

### Funciones - Extras:

## **Como funciona?** 
El controlador de aforo se basa principalmente en el uso del chip **ESP32-WROOM** el cual ejecuta diferentes funciones en base a los requerimientos del proyecto, el esquema general de los modulos especificos que hacen posible su funcionamiento se puede ver en la imagen a continaucion.

![Esquema de funcionalidades - Controlador de Aforo](/Imagenes/Esquema-Controlador-de-Aforo.png)

## **Diseño de la PCB**

### **ESP32-WROOM:**

Para el proyecto se decidio implementar como SoC el chip ESP-WROOM-32 dada su gran variedad de aplicaciones dentro del IoT ya que es un chip de bajo consumo de modo que en su datasheet se especifica que en el modo activo tiene un consumo maximo de 260mA lo cual es ideal para alimentarlo a traves de baterias ademas que posee conectividad bluetooth y wifi, su esquema de conexiones es el siguiente:

![Esquema de conexiones ESP32-WROOM-32 - Controlador de Aforo](/Imagenes/ESP32-WROOM-32-pinout.png)

<br /> 

### **Alimentacion:**

En el sistema de alimentacion se ideo realizar multiples circuitos enfocados en ofrecer multiples opciones de alimentacion al tiempo para el circuito por lo cual se ideo implementar un modulo de carga por baterias recargables, que incluso pueda funcionar y cargar las baterias al tiempo de modo que el diseño se dividio por varias etapas.

#### **Alimentacion - Modulo de Carga:**

Para el modulo de carga se ideo extraer la energia necesaria a traves de un conector Tipo-C que se conectase a una fuente de alimentacion, de modo que utilizando el integrado TP4056 con una resistencia de ajuste con un valor de $1.2k\Omega$ se obtenga una etapa de corriente maxima a 1A aproximadamente y luego una etapa de tension constante para terminar de cargar la bateria, el estado de carga se indicara a traves de 2 LEDs distintos para saber en que proceso se encuentra el dispositivo. Luego se implemento directamente una etapa de proteccion utilizando el integrado DW01A-G el cual protege la bateria de Sobrecarga, Sobredescarga y Cortocircuitos utilizando el circuito de referencia que proporciona el fabricante, de modo que el esquema del Modulo de carga resultante se puede observar en la figura a continuacion:

<img src="./Imagenes/EasyEDA-Esquema-Alimentacion-Carga.png" alt='EasyEDA - Conexiones fisicas del modulo de carga de la bateria - Controlador de Aforo' width="1000px"/>

#### **Alimentacion - Multiplicador de Tension:**

Debido a que multiples dispositivos que se implementaran requieren una tension de 5v se realizo una etapa de multiplicacion de Tension realimentada utilizando el integrado MT3608 el cual independientemente de la tension de entrada siempre entregara 5v siguiendo una expresion lineal de realimentacion entre la resistencia 1 (R1=$7.5k\Omega$) y la resistencia 2 (R2=$1k\Omega$), su esquema respectivo se puede observar en la siguiente figura:

<img src="./Imagenes/EasyEDA-Esquema-Alimentacion-Elevacion.png" alt='EasyEDA - Conexiones fisicas del modulo de Elevacion de tension - Controlador de Aforo' width="700px"/>

#### **Alimentacion - Puente de Carga**

Algo importante a tener en cuenta es que aunque el circuito pueda seguir funcionando mientras esta cargando, en dado caso que el sistema consuma mas alla de 1 amperios, la bateria empezara a descargarse lentamente, de modo que se realizo un puente que cambia entre la conexion de la bateria y la fuente de alimentacion del USB-C a traves de un Mosfet y un diodo schottky lo cual permite que el circuito pueda cargar la bateria al mismo tiempo que seguir en funcionamiento, la unica implicacion a tener en cuenta es que la fuente de alimentacion debe ser capaz de suministrar la corriente de operacion del circuito y la corriente de carga de la bateria para poder funcionar correctamente, el esquema del puente realizado se puede observar en la figura a continuacion:

<img src="./Imagenes/EasyEDA-Esquema-Alimentacion-Puente.png" alt='EasyEDA - Conexiones fisicas del Puente de carga - Controlador de Aforo' width="700px"/>

#### **Alimentacion - Regulador de Tension**
Por ultimo se implemento una etapa de regulacion de tension para los dispositivos que lo requieren tales como el ESP32, la tarjeta Micro-SD y los LEDs respectivamente los cuales no requieren de mucha corriente, por lo cual se hizo uso del integrado AMS1117-3.3 que viene previamente calibrado para regular la tension a 3.3v respectivamente facilitando enormemente su esquema de conexion el cual se puede observar en la siguiente figura:

<img src="./Imagenes/EasyEDA-Esquema-Alimentacion-Regulador.png" alt='EasyEDA - Conexiones fisicas del modulo regulador de tension - Controlador de Aforo' width="500px"/>

<br />

### **Programacion:**

La programacion del dispositivo se realizara a traves de los pines <sub>U0</sub>TXD (41) y <sub>U0</sub>RXD (40) a traves de la interfaz UART, de modo que se requiere de un dispositivo con el cual se pueda realizar la conversion de Serial(USB) a Uart, en este caso se hara uso del modulo **FT232RL** o **CP2102** de manera externa debido a que no se requiere activamente en el funcionamiento del dispositivo, por ende unicamente se crearan sus conexiones hembra para cuando se desee unicamente programar el dispositivo.

Para poder implementar el proyecto dentro del microcontrolador se hara uso de la herramienta **ESPTOOL** la cual nos permite flashear(Reescribir) la memoria flash con la aplicacion que se ha programado para el chip, esto haciendo uso de los pines <sub>CLK</sub>OUT1 (23) para reescribir los datos de la memoria y <sub>Chip</sub>PU (9) para reiniciar el microcontrolador.

Arbitrariamente se implemento un led Azul haciendo uso del pin <sub>GPIO</sub>2 de modo que este indique si el dispositivo esta en funcionamiento.

Teniendo en cuenta lo anterior se realizaron las conexiones correspondientes al bloque de la programacion, en el caso de los pines <sub>U0</sub>TXD (41) y <sub>U0</sub>RXD (40) se realizaron conexiones basicas con pines Hembra dejando las conexiones abiertas para cuando se requiera programar el dispositivo, para el pin <sub>CLK</sub>OUT1 (23) se conecto directamente a un boton a tierra de modo que al pulsarlo se entre al Bootloader cuando se requiera, luego para el pin <sub>Chip</sub>PU (9) se realizo una conexion de resistencia Pull-Up con la fuente y tierra usando una resistencia de 10k de modo que cuando se realize una pulsacion se reinicie el dispositivo, por ultimo el LED se conecto al pin <sub>GPIO</sub>2 (22) y a una resistencia de 180 $\Omega$ que va a tierra de modo que se tiene un consumo promedio de 3.3mA, el esquema resultante se puede observar en la siguiente figura:

<img src="./Imagenes/EasyEDA-Esquema-Programador.png" alt='EasyEDA - Conexiones fisicas del programador - Controlador de Aforo' width="400px"/>

<br /> 

### **Sistema de Deteccion**

Para el sistema de deteccion se buscaron multiples alternativas que hiciesen posible medir la distancia de un objeto respecto al sensor de modo que finalmente se decidio utilizar el sensor HC-SR04 (Sensor de distancias por Ultrasonido), el sensor HC-SR04 consta de 4 pines siendo estos: Alimentacion(5v), Tierra(GND), Trigger(TTL)-Input y Echo(TTL)-Output de modo que aunque la alimentacion del sensor sea de 5v, la salida de Echo se entrega respecto al nivel TTL de Trigger, por ende se puede implementar directamente sin utilizar conversores logicos 5v-3.3v en el ESP32, adicionalmente se especifica que el sensor consume aproximadamente 15mA de corriente.

Para lograr el sistema de deteccion se penso en implementar hasta 4 sensores ultrasonido de modo que se pudieran implementar multiples configuraciones como se especificara en la programacion respectiva, la implementacion de 4 sensores maximo tiene como consecuencia un consumo maximo de 60mA y el uso de 8 pines logicos en el microcontrolador los cuales estan asignados de la siguiente manera (Trigger, Echo): Ultrasonido 1 (<sub>GPIO</sub>26, <sub>GPIO</sub>36), Ultrasonido 2 (<sub>GPIO</sub>25, <sub>GPIO</sub>39), Ultrasonido 3 (<sub>GPIO</sub>33, <sub>GPIO</sub>34), Ultrasonido 4 (<sub>GPIO</sub>32, <sub>GPIO</sub>35), esta de mas aclarar que estos pines estan conectados directamente a puertos hembra que saldran del empaquetado 3D debido a que el ultrasonido se debe instalar en alguna superficie externa a la placa, el esquema resultante de las conexiones se puede observar en la siguiente figura:

<img src="./Imagenes/EasyEDA-Esquema-Deteccion.png" alt='EasyEDA - Conexiones fisicas del sistema de Deteccion - Controlador de Aforo' width="600px"/>

<img src="./Imagenes/HC-SR04.jpg" alt='Modulo Ultrasonido HC-SR04' width="300px"/>

<br /> 

### **Control Manual:**

El sistema de control manual unicamente se basa en la interaccion fisica directa entre algun operario y el mismo sistema, de modo que se implementaron 3 sistemas de resistencias Pull-Up con la fuente y tierra usando resistencias de 10k, ademas de que las conexiones de los botones respectivos se dejo abierta por dos pines hembra debido a que se realizara un cableado para colocar estos botones en la carcasa de la caja, los pines utilizados en el microcontrolador son: <sub>GPIO</sub>27, <sub>GPIO</sub>14 y <sub>GPIO</sub>12, el esquema resultante del control manual se puede observar en la figura a continuacion:


<img src="./Imagenes/EasyEDA-Esquema-ControlManual.png" alt='EasyEDA - Conexiones fisicas del Control Manual - Controlador de Aforo' width="600px"/>

<br /> 

### **Sistema de Indicadores:**

En este apartado se implementaron distintos metodos para tener una interaccion mas directa desde el sistema con el usuario, por lo cual a continuacion se describiran los multiples sistemas implementados para dar indicaciones a los usuarios.

#### **Sistema de Indicadores - Audio:**

En el caso del Sistema Indicador de Audio se vieron diferentes formas de implementar un speaker, de modo que se opto por implementar el integrado MAX98357A el cual consiste en un decodificador del protocolo I2S seguido de un DAC interno con una etapa de amplificacion clase D. Para el proposito del proyecto aunque el protocolo soportase usar dos canales diferentes, unicamente se implemento un canal (Izquierdo) lo cual implica que el pin SD_MODE del integrado esta conectado directamente a 3.3v, adicionalmente se escogio de manera arbitraria obtener una amplificacion de 15dB por lo cual como se especifica en su datasheet se conecto el pin de ganancia a tierra mediante una resistencia de 100k $\Omega$, otras consideraciones que se realizaron es que las salidas del Speaker (R+ y R-) se conectaron en serie con una impedancia dinamica de altas frecuencias junto a condensadores para filtrar el ruido de alta frecuencia que se puede encontrar el altavoz. Con lo anterior en cuenta se utilizaron 3 pines del microcontrolador destinados al protocolo I2S siendo estos <sub>GPIO</sub>21 (Serial Clock), <sub>GPIO</sub>22 (LRCLK) y <sub>GPIO</sub>19 (Data In), es importante tener en cuenta que el integrado esta diseñado para altavoces entre 4 $\Omega$ y 8 $\Omega$ ademas de tener una entrada de alimentacion entre 2.5v y 5v, lo cual implica que la potencia maxima de la amplificacion es de 3.2w y por ende entrega una corriente maxima de 1.25A, el esquema resultante se puede ver en la figura a continuacion:


<img src="./Imagenes/EasyEDA-Esquema-Indicador-Audio-I2S.png" alt='EasyEDA - Conexiones fisicas del Indicador de Audio por I2S - Controlador de Aforo' width="820px"/>

<img src="./Imagenes/EasyEDA-Esquema-Indicador-Audio-Speaker.png" alt='EasyEDA - Conexiones fisicas del Altavoz - Controlador de Aforo' width="500px"/>

#### **Sistema de Indicadores - LEDs:**
Para el sistema de Indicador visual de LEDs se planteo la utilizacion de los LEDs 
WS2812B que funcionan a traves de señales digitales y permiten el acople de multiples LEDs utilizando la misma linea de datos de modo que se utilizo el pin <sub>GPIO</sub>23 del microcontrolador para su respectivo control, originalmente se plantea implementar un unico LED RGB pero no se descarta la opcion de implementar LEDs adicionales, de modo que se crea una segunda conexion para realizar el acople con uno o mas LEDs adicionales ademas se debe tener en cuenta que el consumo maximo de cada LED es de 50mA (16mA por cada subLED), debido a que se planea montar los LEDs en la carcasa del dispositivo se realizaron conexiones hembra para todos los pines tanto del primer LED como el acople con los LEDs adicionales para cablearlos afuera de la placa, el esquema respectivo se puede observar en la siguiente figura:

<img src="./Imagenes/EasyEDA-Esquema-Indicador-Visual-LED.png" alt='EasyEDA - Conexiones fisicas de los LEDs - Controlador de Aforo' width="600px"/>

<br /> 

### **Sistema de Almacenamiento:**

En el sistema de almacenamiento se opto por la implementacion de una tarjeta Micro-SD a traves del protocolo de comunicacion SPI, de modo que se utilizan 4 pines del microcontrolador siento estos <sub>GPIO</sub>17 (SD_Clock), <sub>GPIO</sub>5 (SD_Input), <sub>GPIO</sub>16 (SD_Output) y <sub>GPIO</sub>18 (Chip Select), la tarjeta MicroSD se conecto a traves de su socket respectivo de modo que se ha de tener en cuenta que esta consume aproximadamente 50mA cuando opera a traves del protocolo SPI, adicionalmente se conecto un LED azul en el Socket de la tarjeta con una resistencia de 180 $\Omega$, el cual funciona como indicador de cuando esta conectada la tarjeta o desconectada de modo que genera un consumo adicional de 3.3mA, el diagrama de conexiones del sistema de almacenamiento se puede observar a continuacion:

<img src="./Imagenes/EasyEDA-Esquema-Almacenamiento.png" alt='EasyEDA - Conexiones fisicas del sistema de Almacenamiento - Controlador de Aforo' width="500px"/>

<br /> 

### **Puertos de Expansion - ${I^2C}$ y GPIO:** 

Debido a que unicamente sobran 3 pines del microcontrolador se decidio conectar 2 de ellos a traves del protocolo de comunicacion ${I^2C}$ de modo que se conectaron en un sistema resistor de Pull-Up con una resistencia de 5k $\Omega$ a la fuente y se dejaron sus conexiones libres a pines hembra para poder conectar dispositivos adicionales con este sistema, los pines implementados para el $I^2C$ Corresponden a <sub>GPIO</sub>15 (SCL) y <sub>GPIO</sub>13 (SDA). En el caso del ultimo pin libre el cual es <sub>GPIO</sub>4 se creo una conexion a un pin hembra de modo que en caso que se requiera por alguna funcionalidad adicional se pueda utilizar libremente en la placa, el esquema correspondiente de los puertos de expansion se pueden observar en la siguiente figura:

<img src="./Imagenes/EasyEDA-Esquema-Expansion.png" alt='EasyEDA - Conexiones fisicas de los Puertos de Expansion - Controlador de Aforo' width="500px"/>

<br /> 

### **Esquema General - ESP32:** 

El esquema general de las conexiones anteriormente mencionadas al microcontrolador se puede observar en la figura a continuacion:

<img src="./Imagenes/EasyEDA-Esquema-ESP32.png" alt='EasyEDA - Conexiones fisicas de los Puertos del microcontrolador - Controlador de Aforo' width="500px"/>

<br />

### **PCB y Modelo-3D**

Una vez descritas todas las conexiones planteadas y las funcionalidades de la placa se realizo el respectivo ruteo de las pistas en la PCB teniendo en cuenta las corrientes maximas que se deben soportar sobre cada pista cuando el dispositivo bajo maxima operacion y cargando la bateria respectivamente (Se estima que maximo se consuman hasta 2.6A en casos extremos por la pista VBus), adicionalmente se tomo el tiempo necesario para realizar todas las pistas sobre la capa superior de la placa dando como resultado los esquemas que se observaran a continuacion:

<img src="./Imagenes/EasyEDA-PCB-ControladorAforo.png" alt='EasyEDA - PCB diseñada - Controlador de Aforo' width="500px"/>

<img src="./Imagenes/EasyEDA-3DTop-ControladorAforo.png" alt='EasyEDA - Vista superior Esquema 3D - Controlador de Aforo' width="500px"/>

## **Programacion del Dispositivo**

### **Modulo de Almacenamiento**

El modulo de almacenamiento se gestiono en mycropython a traves de la libreria de servicios basicos de "sistema operativo" **OS** integrada y una libreria personalizada para administrar la tarjeta microSD a traves del protocolo SPI pues los pines de la microSD no se conectaron a traves de los dedicados del bus SPI por ende no es posible el uso de la libreria **SDcard** integrada en **Machine**, en su lugar se utilizo una implementacion que hace uso del metodo **SOFTSPI** en la libreria **SPI** integrada en **Machine** para gestionar el protocolo SPI a traves de software.

Para poder implementar la libreria personalizada se debe crear una clase que inicialice la tarjeta microSD y cuente con los metodos **readblocks**, **writeblocks** y **ioctl** necesarios para su utilizacion con la libreria **OS**, adicionalmente se deben crear los metodos necesarios para que las funciones mencionadas anteriormente puedan interactuar con la tarjeta microSD a traves del protocolo SPI. La jerarquia de comunicacion y metodos implementados para la comunicacion entre **OS** y la microSD se puede observar en el esquema a continacion:

<img src="./Imagenes/SDlibreria.png" alt='EasyEDA - Vista superior Esquema 3D - Controlador de Aforo' width="1000px"/>

Como se puede observar en el esquema de funciones, el protocolo SPI es el nivel de comunicacion mas bajo en la jerarquia teniendo una conexion directa con la tarjeta microSD, su implementacion en codigo respectivamente se hace utilizando el metodo **SOFTSPI** y  declarando como argumento los pines respectivos donde se realizara su comunicacion (MOSI, MISMO, CLK)(CS se gestiona independientemente) por lo cual una vez declarados los puertos se configura la cantidad de baudios con la que se comunicara el protocolo. una vez configurado el protocolo se hace uso de los metodos **spi.write**, **spi.read**, **spi.readinto** y **spi.write_readinto** para enviar y recibir datos incluso al mismo tiempo.

Una vez teniendo las funciones basicas de comunicacion del protocolo SPI, se necesita un metodo que permita enviar comandos a la tarjeta MicroSD para que pueda realizar diferentes funciones tanto de lectura como de escritura, de modo que generalmente las tarjetas del tipo SD poseen la siguiente estructura en la linea de comandos:

| Byte1 | Byte1 | Byte1    | Byte2-5   | Byte6 | Byte6 |
|-------|-------|----------|-----------|-------|-------|
| 7     | 6     |   5-0    |   31-0    |   7   | 0     |
| 0     | 1     |  Comand  | Arguments | CRC   | 1     |

Teniendo la estructura de datos necesaria se declara un metodo que reciba los comandos y argumentos que se deseen enviar a traves de un buffer para luego utilizar el metodo spi.write y enviar dicha informacion a la tarjeta microSD de modo que luego se reciba una respuesta de un byte la cual sera retornada por el metodo, en caso de no recibir respuesta dentro de un tiempo determinado el metodo retorna -1.

Una vez determinada una funcion basica para el envio de comandos de la tarjeta microSD es necesario generar las funciones basicas para enviar y leer datos las cuales se reflejan en **readinto**, **write** y **write_token**. luego de definir las comunicaciones basicas es necesario inicializar la tarjeta microSD a traves de comandos que permitan iniciar la tarjeta microSD, obtener la version de la tarjeta, obtener el numero de sectores de la tarjeta y ajustar la longitud de los bloques a 512 bytes con el fin de que el sistema unicamente se encargue de escribir y recibir la informacion que necesita, por esto se declaran 3 funciones especificas de bloques necesarias para interactuar con los bloques de la tarjeta y almacenar/leer datos de la misma, estos bloques como se ha visto corresponden a **readblocks**, **writeblocks** y **ioctl** de modo que a traves de comandos de escritura/lecturas de uno o multiples bloques se envia/lee la informacion necesaria en la tarjeta microSD. 

con todos estos metodos definidos se puede controlar la tarjeta microSD a traves de la libreria **OS**, simplificando en modulos superiores el uso de comandos basicos de un sistema de archivos.

### **Modulo de Audio**