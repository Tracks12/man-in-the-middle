#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2009 - Copyright by 4N4RCHY. All rights is reserved.

# ----------------------------------
#  Program >>> man-in-the-middle.py
# ----------------------------------

import os, sys
import warnings
from Tkinter import *

""" Variable de séléction d'interface réseau """
op = 0 # [ 0. eth0 | 1. wlan0 ]

if(op): op = " -i wlan0"
else: op = ""

""" Définition de valeur pour les couleur """
class color:
	""" Define plain colors """
	GRAY     = '\033[30m'
	RED      = '\033[31m'
	GREEN    = '\033[32m'
	YELLOW   = '\033[33m'
	BLUE     = '\033[34m'
	MAGENTA  = '\033[35m'
	CYAN     = '\033[36m'
	WHITE    = '\033[37m'
	CRIMSON  = '\033[38m'
	
	""" Define highlighted colors """
	RED_HL     = '\033[41m'
	GREEN_HL   = '\033[42m'
	BROWN_HL   = '\033[43m'
	BLUE_HL    = '\033[44m'
	MAGENTA_HL = '\033[45m'
	CYAN_HL    = '\033[46m'
	GRAY_HL    = '\033[47m'
	WHITE_HL   = '\033[48m'
	
	""" Define bold colors """
	B_GRAY     = '\033[1;30m'
	B_RED      = '\033[1;31m'
	B_GREEN    = '\033[1;32m'
	B_YELLOW   = '\033[1;33m'
	B_BLUE     = '\033[1;34m'
	B_MAGENTA  = '\033[1;35m'
	B_CYAN     = '\033[1;36m'
	B_WHITE    = '\033[1;37m'
	B_CRIMSON  = '\033[1;38m'
	
	""" Define bold highlighted colors """
	B_RED_HL     = '\033[1;41m'
	B_GREEN_HL   = '\033[1;42m'
	B_BROWN_HL   = '\033[1;43m'
	B_BLUE_HL    = '\033[1;44m'
	B_MAGENTA_HL = '\033[1;45m'
	B_CYAN_HL    = '\033[1;46m'
	B_GRAY_HL    = '\033[1;47m'
	B_WHITE_HL   = '\033[1;48m'
	
	""" Define end variable to cancel colors """
	END = '\033[0m'

""" Mode Terminal du program """
def console():
	print("> " + color.GREEN + "Initiate TERM mod_" + color.END)
	print("TCP Dump - by DHS Team {DevilHatSec}\nProgramed by 4N4RCHY and z3r0.")
	
	while(1):
		print("\n\t\tTCP Dump Command PORT\n")
		print(color.GREEN + "\t1. SAMPLE\n\t2. ALL\n" + color.END + color.YELLOW + "\t3. FTP\n\t4. HTTP\n\t5. HTTPS\n\t6. SMTP\n\t7. POP3\n\t8. HELP\n\t9. MORE\n\t10. INTERFACE\n" + color.END + color.RED + "\t0. QUIT\n" + color.END)
		choice = input("> Select Dump mod: ")
		
		if(choice == 1): dump_list()
		elif(choice == 2): dump_all()
		elif(choice == 3): dump_ftp()
		elif(choice == 4): dump_http()
		elif(choice == 5): dump_https()
		elif(choice == 6): dump_smtp()
		elif(choice == 7): dump_pop3()
		elif(choice == 8):
			print("> " + color.B_YELLOW + "Get Help_" + color.END)
			print("Aide:\t\t\t\t\n[SAMPLE], lance tout simplement tcpdump\n[ALL], lance la commande traduit en ascii sur tout les ports\n[FTP], lance la commande que sur le port FTP\n[HTTP], lance la commande que sur le port HTTP\n[HTTPS], lance la commande que sur le port HTTPS\n[SMTP], lance la commande que sur le port SMTP\n[POP3], lance la commande que sur le port POP3\n[INTERFACE], permet de sélectionner l'interface réseau à utiliser\n\nATTENTION: Il se peut que le scan HTTPS soit illisible à cause de la clé de cryptage.\nCe Software est compatible uniquement sous linux.")
		
		elif(choice == 9):
			print("> " + color.B_YELLOW + "Get More Info_" + color.END)
			print("More:\n\n\tProgram Created by 4N4RCHY and z3r0.\n\tVersion_1.0-b\n\n\tProgramer:\n\t\t4N4RCHY <anarchy.dar97@gmail.com>;\n\t\tz3r0 <mail>;")
		
		elif(choice == 10):
			print("> " + color.B_YELLOW + "Choose interface_" + color.END)
			print("Interface: \n\n" + color.GREEN + "\t0. eth0\n\t1. wlan0\n" + color.END)
			interface = input("> Select interface: ")
			
			if(interface == 0):
				print("> " + color.YELLOW + "Interface: eth0_" + color.END)
				op = ""
			elif(interface == 1):
				print("> " + color.YELLOW + "Interface: wlan0_" + color.END)
				op = " -i wlan0"
			elif(interface < 0): print("> " + color.RED + "Interface: Not Defined_" + color.END)
			elif(interface > 1): print("> " + color.RED + "Interface: Not Defined_" + color.END)
		
		elif(choice == 0):
			print("> " + color.B_RED + "Quitting_" + color.END)
			exit(1)

""" Mode Fenêtre graphique du program """
def window():
	print("> " + color.B_GREEN + "Initiate GRAPH mod_" + color.END)
	tcpdump = Tk()
	tcpdump.title('TCP Dump - by DHS Team {DevilHatSec}')
	tcpdump.resizable(width=FALSE, height=FALSE)
	
	""" Menu de l'app """
	menubar = Menu(tcpdump)
	
	""" Menu "Fichier" """
	menu0 = Menu(menubar, tearoff=0)
	menu0.add_command(label="Quitter", command=quit)
	menubar.add_cascade(label="Fichier", menu=menu0)
	
	""" Menu "À propos" """
	menu1 = Menu(menubar, tearoff=0)
	menu1.add_command(label="Aide", command=help_window)
	menu1.add_command(label="À propos du software", command=info_window)
	menubar.add_cascade(label="À propos", menu=menu1)
	
	""" Panneau de Commande """
	panel = Frame(tcpdump, borderwidth=1, relief=GROOVE)
	panel.pack(side=TOP, padx=8, pady=8)
	Label(panel, text="TCP Dump Command PORT").pack(padx=5, pady=2)
	
	""" Bouttons de commandes contenu dans le Panneau de Commande """
	Button(panel, text="SAMPLE", command=dump_list).pack(side=LEFT, padx=2, pady=2)
	Button(panel, text="ALL", command=dump_all).pack(side=LEFT, padx=2, pady=2)
	Button(panel, text="FTP", command=dump_ftp).pack(side=LEFT, padx=2, pady=2)
	Button(panel, text="HTTP", command=dump_http).pack(side=LEFT, padx=2, pady=2)
	Button(panel, text="HTTPS", command=dump_https).pack(side=LEFT, padx=2, pady=2)
	Button(panel, text="SMTP", command=dump_smtp).pack(side=LEFT, padx=2, pady=2)
	Button(panel, text="POP3", command=dump_pop3).pack(side=LEFT, padx=2, pady=2)
	
	""" Panneau pied de fenêtre """
	bot_panel = Frame(tcpdump, borderwidth=1, relief=GROOVE)
	bot_panel.pack(side=TOP, padx=8, pady=8)
	Label(bot_panel, text="Quit TCP Dump").pack(padx=5, pady=2)
	
	""" Bouttons de commandes contenu dans le Panneau pied """
	Button(bot_panel, text="HELP", command=help_window).pack(side=LEFT, padx=2, pady=2)
	Button(bot_panel, text="MORE", command=info_window).pack(side=LEFT, padx=2, pady=2)
	Button(bot_panel, text="QUIT", command=quit).pack(side=LEFT, padx=2, pady=2)
	
	tcpdump.config(menu=menubar)
	tcpdump.mainloop()
	quit()

""" Fenêtre secondaire "Aide" """
def help_window():
	print("> " + color.B_YELLOW + "Get Help_" + color.END)
	help = Tk()
	help.title('Manuel du program')
	help.resizable(width=FALSE, height=FALSE)
	
	""" Texte qui affiche l'aide du program """
	Label(help, text="Programme utilisant la commande 'tcpdump'\n en mode administrateur.\n").pack(side=TOP, padx=10, pady=5)
	Label(help, text="Aide:\t\t\t\t\n[SAMPLE], lance tout simplement tcpdump\n[ALL], lance la commande traduit en ascii sur tout les ports\n[FTP], lance la commande que sur le port FTP\n[HTTP], lance la commande que sur le port HTTP\n[HTTPS], lance la commande que sur le port HTTPS\n[SMTP], lance la commande que sur le port SMTP\n[POP3], lance la commande que sur le port POP3\n\nATTENTION: Il se peut que le scan HTTPS soit illisible à cause de la clé de cryptage.\nCe Software est compatible uniquement sous linux.").pack(side=LEFT, padx=2, pady=2)
	
	help.mainloop()

""" Fenêtre secondaire "À propos du software" """
def info_window():
	print("> " + color.B_YELLOW + "Get More Info_" + color.END)
	info = Tk()
	info.title('À propos du software')
	info.resizable(width=FALSE, height=FALSE)
	
	""" Texte qui affiche les infos du software """
	Label(info, text="Program Created by 4N4RCHY and z3r0.\n Version_1.0-b").pack(side=TOP, padx=10, pady=5)
	Label(info, text="Programer:\n\n 4N4RCHY <anarchy.dar97@gmail.com>;\n z3r0 <mail>;").pack(side=TOP, padx=5, pady=5)
	Label(info, text="(c) 2009 - Copyright by DevilHatSec.").pack(side=BOTTOM, padx=10, pady=5)
	
	info.mainloop()

""" Command: dump_list """
def dump_list():
	print("> " + color.GREEN + "Analyse All Ports with tcpdump [SAMPLE MOD]_" + color.END)
	os.system('sudo tcpdump' + op)

""" Command: dump_all """
def dump_all():
	print("> " + color.GREEN + "Analyse All Ports with tcpdump_" + color.END)
	os.system('sudo tcpdump -s 0 -A' + op)

""" Command: dump_ftp """
def dump_ftp():
	print("> " + color.YELLOW + "Analyse FTP Port with tcpdump_" + color.END)
	os.system('sudo tcpdump -s 0 -A port ftp' + op)

""" Command: dump_http """
def dump_http():
	print("> " + color.YELLOW + "Analyse HTTP Port with tcpdump_" + color.END)
	os.system('sudo tcpdump -s 0 -A port http' + op)

""" Command: dump_https """
def dump_https():
	print("> " + color.YELLOW + "Analyse HTTPS Port with tcpdump_" + color.END)
	os.system('sudo tcpdump -s 0 -A port https' + op)

""" Command: dump_smtp """
def dump_smtp():
	print("> " + color.YELLOW + "Analyse SMTP Port with tcpdump_" + color.END)
	os.system('sudo tcpdump -s 0 -A port smtp' + op)

""" Command: dump_pop3 """
def dump_pop3():
	print("> " + color.YELLOW + "Analyse POP3 Port width tcpdump_" + color.END)
	os.system('sudo tcpdump -s 0 -A port pop3' + op)

""" Command: Quit """
def quit():
	print("> " + color.B_RED + "Quitting_" + color.END)
	exit(1)

""" Selection des mods de lancement """
def program():
	while(1):
		print("> Please, select start mod:\n\n\t1. console mod\n\t2. graphique mod\n\t0. quit\n")
		choice = input(">>> Mod: ")
		
		if(choice == 1): console()
		elif(choice == 2): window()
		elif(choice == 0):
			print("> " + color.B_RED + "Quitting_" + color.END)
			exit(1)
		
		else: print("> " + color.B_YELLOW + "Uknown Mod_" + color.END)

print("> " + color.B_GREEN + "Launching_\n" + color.END)
program()

# -----
#  END
# -----
