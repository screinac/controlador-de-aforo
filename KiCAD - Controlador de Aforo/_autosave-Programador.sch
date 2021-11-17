EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 2
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text HLabel 5250 3200 0    50   Input ~ 0
RXDu0
Text HLabel 5250 3500 0    50   Output ~ 0
TXDu0
Wire Wire Line
	5350 3200 5250 3200
Wire Wire Line
	5350 3500 5250 3500
Text HLabel 5250 4350 0    50   Output ~ 0
Boot-Flash
Text HLabel 5250 4500 0    50   Input ~ 0
Ground
Wire Wire Line
	5250 4350 5550 4350
Wire Wire Line
	5950 4350 6050 4350
Wire Wire Line
	6050 4350 6050 4500
Wire Wire Line
	6050 4500 5250 4500
$Comp
L Connector:Conn_01x01_Female RXDu0
U 1 1 6196EA06
P 5550 3200
F 0 "RXDu0" H 5578 3226 50  0000 L CNN
F 1 "Conn_01x01_Female" H 5578 3135 50  0000 L CNN
F 2 "Connector_Wire:SolderWirePad_1x01_SMD_1x2mm" H 5550 3200 50  0001 C CNN
F 3 "~" H 5550 3200 50  0001 C CNN
	1    5550 3200
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x01_Female TXDu0
U 1 1 6196F61A
P 5550 3500
F 0 "TXDu0" H 5578 3526 50  0000 L CNN
F 1 "Conn_01x01_Female" H 5578 3435 50  0000 L CNN
F 2 "Connector_Wire:SolderWirePad_1x01_SMD_1x2mm" H 5550 3500 50  0001 C CNN
F 3 "~" H 5550 3500 50  0001 C CNN
	1    5550 3500
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push Boot-Flash
U 1 1 6196FF55
P 5750 4350
F 0 "Boot-Flash" H 5750 4635 50  0000 C CNN
F 1 "SW_Push" H 5750 4544 50  0000 C CNN
F 2 "Button_Switch_SMD:SW_SPST_B3U-1000P" H 5750 4550 50  0001 C CNN
F 3 "~" H 5750 4550 50  0001 C CNN
	1    5750 4350
	1    0    0    -1  
$EndComp
$EndSCHEMATC
