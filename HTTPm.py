from os import system
from time import sleep

red="\033[1;31m"
gris="\033[1;30m"
transparent="\033[0m"
Fiuscha="\033[0;35m"
green="\033[1;32m"

def display():
	try:
		system('clear || cls')
		print("\n\n")

		print("""       oooooooooooo            .o    .oooo.                     .o8 			""")
		sleep(0.1)
		print("""       `888'     `8          o888  .dP""Y88b                   "888 			""")
		sleep(0.1)
		print("""        {0}888         oooo d8b  888        ]8P' ooo. .oo.    .oooo888 			{1}""".format(gris,transparent))
		sleep(0.1)
		print("""        {0}888oooo8    `888""8P  888      <88b.  `888P"Y88b  d88' `888 			{1}""".format(gris,transparent))
		sleep(0.1)
		print("""        {0}888    "     888      888       `88b.  888   888  888   888 			{1}""".format(gris,transparent))
		sleep(0.1)
		print("""        {0}888          888      888  o.   .88P   888   888  888   888 			{1}""".format(Fiuscha,transparent))
		sleep(0.1)
		print("""       {0}o888o        d888b    o888o `8bd88P'   o888o o888o `Y8bod88P"			{1}""".format(Fiuscha,transparent))
		sleep(0.1)
		print("\n                       {0}))){1}  HTTP METHOD {0}((({1}                           ".format(Fiuscha,transparent))
		sleep(0.1)
		print("\n                                                        {}by 54m{}               ".format(Fiuscha,transparent))
	except KeyboardInterrupt:pass
	
	

request = ['POST','GET','HEAD','DELETE','PUT','CONNECT','OPTIONS','OPTIONS','PATCH','TRACE','PATCH']


try:
	display()
	link = input('\n\n{0}Enter your url{1} : '.format(gris,transparent))
	for req in request :
		print('\n\n{0}<============================= {3}{1} {0}===========================>{2}\n\n'.format(Fiuscha,req,transparent,gris))
		if req == 'HEAD' :
			system('curl -I {}'.format(link))
			continue
		system('curl -X {} {} '.format(req,link))
	print('\n\n{}Goodbye Friend !{}\n'.format(green,transparent))
except KeyboardInterrupt:
	print('\n\n{}Goodbye Friend !{}\n'.format(Fiuscha,transparent))
	exit(0)
	
