EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
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
L ESP32:ESP32 U?
U 1 1 618D2927
P 6000 3900
F 0 "U?" H 6000 5737 60  0000 C CNN
F 1 "ESP32" H 6000 5631 60  0000 C CNN
F 2 "ESP32-footprints-Lib:ESP32" H 6450 4800 60  0001 C CNN
F 3 "" H 6450 4800 60  0001 C CNN
	1    6000 3900
	1    0    0    -1  
$EndComp
Wire Wire Line
	3050 3050 3900 3050
Wire Wire Line
	3900 3050 3900 5000
Wire Wire Line
	3900 5000 5150 5000
Wire Wire Line
	3050 3150 3800 3150
Wire Wire Line
	3800 3150 3800 5100
Wire Wire Line
	3800 5100 5150 5100
Wire Wire Line
	3050 3350 3650 3350
Wire Wire Line
	3650 3350 3650 5750
Wire Wire Line
	3650 5750 7000 5750
Wire Wire Line
	7000 5750 7000 4050
Wire Wire Line
	7000 4050 6850 4050
Wire Wire Line
	3050 3250 3750 3250
Wire Wire Line
	3750 3250 3750 5600
Wire Wire Line
	3750 5600 6900 5600
Wire Wire Line
	6900 5600 6900 4250
Wire Wire Line
	6900 4250 6850 4250
$Comp
L Interface_USB:FT232RL U?
U 1 1 618D5DB8
P 2250 3750
F 0 "U?" H 2250 4931 50  0000 C CNN
F 1 "FT232RL" H 2250 4840 50  0000 C CNN
F 2 "Package_SO:SSOP-28_5.3x10.2mm_P0.65mm" H 3350 2850 50  0001 C CNN
F 3 "https://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT232R.pdf" H 2250 3750 50  0001 C CNN
	1    2250 3750
	1    0    0    -1  
$EndComp
$EndSCHEMATC
