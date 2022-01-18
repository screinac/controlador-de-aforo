EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 6
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Sheet
S 7950 2700 950  650 
U 61955D17
F0 "Programador" 50
F1 "Programador.sch" 50
F2 "RXDu0" I L 7950 3050 50 
F3 "TXDu0" O L 7950 2950 50 
F4 "Boot-Flash" O L 7950 3250 50 
F5 "Ground" I L 7950 2800 50 
$EndSheet
Wire Wire Line
	7850 2650 7850 2800
Wire Wire Line
	7850 2800 7950 2800
Wire Wire Line
	7950 3250 7850 3250
Wire Wire Line
	7850 3250 7850 3950
$Sheet
S 2450 2200 1200 650 
U 61965519
F0 "alimentacion" 50
F1 "alimentacion.sch" 50
$EndSheet
$Sheet
S 1150 3500 1050 650 
U 61965726
F0 "sistema_deteccion" 50
F1 "sistema_deteccion.sch" 50
$EndSheet
$Sheet
S 2250 4850 1150 650 
U 6196608F
F0 "indicadores" 50
F1 "indicadores.sch" 50
$EndSheet
$Sheet
S 8450 4800 1050 600 
U 6196613C
F0 "sistema_de_uso" 50
F1 "sistema_de_uso.sch" 50
$EndSheet
Wire Wire Line
	7850 3950 6100 3950
Wire Wire Line
	6100 2650 7850 2650
Wire Wire Line
	6100 3050 7950 3050
Wire Wire Line
	6100 2950 7950 2950
$Comp
L ESP32-footprints-Shem-Lib:ESP-32S U1
U 1 1 619515E6
P 5200 3300
F 0 "U1" H 5175 4687 60  0000 C CNN
F 1 "ESP-32S" H 5175 4581 60  0000 C CNN
F 2 "ESP32-footprints-Lib:ESP-32S" H 5550 4650 60  0001 C CNN
F 3 "" H 4750 3750 60  0001 C CNN
	1    5200 3300
	1    0    0    -1  
$EndComp
$EndSCHEMATC