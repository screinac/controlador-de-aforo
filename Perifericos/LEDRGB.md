# LED RGB - WS2812B


Para implementar un modulo que utilice el protocolo definido para el LED RGB WS2812, el esp32 posee una libreria nativa dentro de micropython que se llama Neopixel de modo que unicamente se declara la clase **NeoPixel** en una variable inicializandola con el pin de datos y el numero de pixeles a controlar, seguido a esto se seleccionan los valores de color RGB (8 por bits cada canal de color) y el numero del Led al cual se le cambien sus valores de color, por ejemplo np[0]=(255,255,255) y con este metodo se modifican directamente los colores del pixel seleccionado.