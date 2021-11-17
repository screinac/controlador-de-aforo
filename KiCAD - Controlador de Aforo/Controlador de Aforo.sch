EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 2
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L ESP32-footprints-Shem-Lib:ESP-32S U1
U 1 1 619515E6
P 5800 3850
F 0 "U1" H 5775 5237 60  0000 C CNN
F 1 "ESP-32S" H 5775 5131 60  0000 C CNN
F 2 "ESP32-footprints-Lib:ESP-32S" H 6150 5200 60  0001 C CNN
F 3 "" H 5350 4300 60  0001 C CNN
	1    5800 3850
	1    0    0    -1  
$EndComp
$Sheet
S 8550 3250 950  650 
U 61955D17
F0 "Programador" 50
F1 "Programador.sch" 50
F2 "RXDu0" I L 8550 3600 50 
F3 "TXDu0" O L 8550 3500 50 
F4 "Boot-Flash" O L 8550 3800 50 
F5 "Ground" I L 8550 3350 50 
$EndSheet
Wire Wire Line
	6700 3500 8550 3500
Wire Wire Line
	6700 3600 8550 3600
Wire Wire Line
	6700 3200 8450 3200
Wire Wire Line
	8450 3200 8450 3350
Wire Wire Line
	8450 3350 8550 3350
Wire Wire Line
	8550 3800 8450 3800
Wire Wire Line
	8450 3800 8450 4500
Wire Wire Line
	8450 4500 6700 4500
$EndSCHEMATC
