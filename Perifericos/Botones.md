# Botones - Interrupciones


El control manual del dispositivo se planteo a traves de interrupciones de modo que cuando se detecte un flanco de subida/bajada (se configura mas adelante) se ejecute una funcion respectiva que se configurara en la programacion del codigo general, la declaracion de las interrupciones se implementa a traves del metodo **irq** de la libreria Pin correspondiente al modulo machine de micropython, los argumentos de la interrupcion corresponden a la accion que desencadena la interrupcion y la funcion que se debe ejecutar respectivamente, de modo que la estructura del metodo es: irq(handler,trigger).
