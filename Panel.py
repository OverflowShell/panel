#!/usr/bin/python3

#Colores xD
M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'

from requests.exceptions import ConnectionError
import requests
import time
import sys
import os

#Banner simple :v 
def main():
    print("""

    
    _      _       _                             _ 
   /_\  __| |_ __ (_)_ _ ___ _ __  __ _ _ _  ___| |
  / _ \/ _` | '  \| | ' \___| '_ \/ _` | ' \/ -_) |
 /_/ \_\__,_|_|_|_|_|_||_|  | .__/\__,_|_||_\___|_|
                            |_|                    


    """)

    print(''+C+'Uso de la herramienta; '+C+'')
    print(''+C+'[+]python3 Panel.py www.sitio.com'+C+'')
if __name__ == '__main__':
    main()
    time.sleep(5)


#Proceso!!

def main():
	found = []
	os.system('clear')
	web = sys.argv[1]
	if not web.startswith('http'):
		web = 'http://' + web
        
		web = web + '/'
	print(''+C+'SITIO WEB'+A+' : '+W+'{}'.format(sys.argv[1]))
	print(''+C+'-------------- '+W+'Iniciando'+C+' --------------')
	
	list = ['admin', 'administrator', 'webadmin', 'wp-login.php', 'wp-admin.php', 'admin1', 'admin2', 'admin3', 'admin4', 'admin5', 'admin/login.php', 'admin/login',
	'adminarea', 'admin/index.php', 'memberadmin', 'admin.aspx', 'admin.asp', 'admin.php', 'administrator.php', 'administrator.aspx', 'administrator.asp', 'login.html', 'cpanel',
	'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
	'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
	'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
	'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
	'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
	'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','administration','pages/admin/admin-login.html','admin/admin-login.html',
	'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
	'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
	'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
	'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
	'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php']
	
	for i in list:
		try:
			url = web + i
			w = requests.get(url)
			f = web.replace('http://','')
			s = f + i
			if w.status_code < 200 or w.status_code <= 201:
				print(''+ W +'Probando ' + C + s + K + ' : ' + H + 'Encontrado !')
				found.append(s)
			else:
				print(''+ W +'Probando ' + C + s + K + ' : ' + A + 'No encontrado !')
		except ConnectionError:
			break
			
	print(''+C+'----------- '+W+'Páginas encontradas'+C+' -----------')
	c = (len(found))
	print(''+C+'Resultados : '+W+str(c))
	print('\n'.join(found))
        
if __name__ == '__main__':
    main()

