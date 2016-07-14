#!/usr/bin/python
import os
from commands import getstatusoutput as loc
opt,aloc,mloc,adown,mdown, = '','','','',''
# Enter your default Tomcat BIN Directory
Default='NULL' #TomcatDefault
def search():
	global aloc, mloc, adown, mdown
	os.system('sudo updatedb')
	aloc=loc('locate tomcat | grep /opt | grep startup.sh')
	adown=loc('locate tomcat | grep /opt | grep shutdown.sh')
	mloc=loc('locate tomcat | grep /usr | grep startup.sh')
	mdown=loc('locate tomcat | grep /usr | grep shutdown.sh')
	


def restart(op):
	
	global aloc, mloc, adown, mdown, Default
	if op == 'aloc':
		try:
			print("Shuting Down Tomcat")
			os.system('sudo {0}'.format(adown[1]))
        	except OSError as err:
			print("Error Shutting : {0}".format(err))
			os.system("sudo kill -9 `ps aux |grep tomcat | awk '{print $2}'`")
			print("Killing Tomcat....")
			os.system('sleep 2')
		try:
			print("Starting Tomcat")
		        os.system('sudo {0}'.format(aloc[1]))
		except OSError as err:
			print("Error Starting : {0}".format(err))

	elif op == 'mloc':
		try:
                        print("Shuting Down Tomcat")
                        os.system('sudo {0}'.format(mdown[1]))
                except OSError as err:
                        print("Error Shutting : {0}".format(err))
			os.system("sudo kill -9 `ps aux |grep tomcat | awk '{print $2}'`")
			print("Killing Tomcat....")
			os.system('sleep 2')
                try:    
                        print("Starting Tomcat")
                        os.system('sudo {0}'.format(mloc[1]))
                except OSError as err:
                        print("Error Starting : {0}".format(err))

	elif op == 'Default':
		try:
                        print("Shuting Down Tomcat")
                        os.system('sudo {0}shutdown.sh'.format(Default))
                except OSError as err:
                        print("Error Shutting : {0}".format(err))
			os.system("sudo kill -9 `ps aux |grep tomcat | awk '{print $2}'`")
			print("Killing Tomcat....")
			os.system('sleep 2')
                try:    
                        print("Starting Tomcat")
                        os.system('sudo {0}startup.sh'.format(Default))
                except OSError as err:
                        print("Error Starting : {0}".format(err))


	

def choice():
	global opt, aloc, mloc
	if aloc[0] == 0 and mloc [0] == 0:
		opt=raw_input("Choose Tomcat version :\n1.\t{0}\n2.\t{1}\n\t".format(aloc,mloc))

def main():
	global Default, aloc,mloc,opt
	if Default == 'NULL':
			search()
			choice()
			if opt == '1' or mloc[0] != 0:
				restart('aloc')
				exit(0)
			elif opt == '2' or aloc[0] != 0:
				restart('mloc')
				exit(0)
			else:
				print("Invalid Choice\nEnter Again")
				main()
	else:
		restart('Default')
		exit(0)

main()
