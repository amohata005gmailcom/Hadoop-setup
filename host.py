
		

def slave():
	import subprocess 
	f=open('/etc/hosts'  , 'a')
	b=[]
	i=0
	while True:
		i=i+1
		print('Enter ip of system you want to add as slave')
		ip=input('')
		a=subprocess.getstatusoutput("ping {} -c 2".format(ip))
		if a[0]!=0:
			print('this ip is not reachable . Do you still want to add it yes/no')
			ans=input()
			if ans=='no':
				break
			if ans=='yes':
				b.append(ip)
				c='{}       slave{}.avn\n'.format(ip,i)
				f.write(c)
				
				print('do you want to add more slave  yes/no')
				c=input()
				if c=='no':
					break

		else:

			c='{}          slave{}.avn\n'.format(ip,i)
			f.write(c)
			print('do you want to add more slave  yes/no')
			c=input()
			if c=='no':
				break
	return(b)		
def master():
	import subprocess 
	f=open('/etc/hosts'  , 'a')

	print('Enter ip of system you want to add as master')
	b=input('')
	a=subprocess.getstatusoutput("ping {} -c 2".format(b))
	if a[0]!=0:
		print('this ip is not reachable . Do you still want to add it yes/no')
		ans=input()
		if ans=='yes':
			c='{}          master.avn\n'.format(b)
			f.write(c)
	else:
		c='{}          master.avn\n'.format(b)
		f.write(c)
	return(c)




def tasktracker():
	import subprocess 
	f=open('/etc/hosts'  , 'a')
	b=[]
	i=0
	while True:
		i=i+1
		print('Enter ip of system you want to add as Tasktracker')
		ip=input('')
		a=subprocess.getstatusoutput("ping {} -c 2".format(ip))
		if a[0]!=0:
			print('this ip is not reachable . Do you still want to add it yes/no')
			ans=input()
			if ans=='no':
				break
			if ans=='yes':
				b.append(ip)
				c='{}       tt{}.avn\n'.format(ip,i)
				f.write(c)
				
				print('do you want to add more Task tracker  yes/no')
				c=input()
				if c=='no':
					break

		else:

			c='{}          tt{}.avn\n'.format(ip,i)
			f.write(c)
			print('do you want to add more Task tracker  yes/no')
			c=input()
			if c=='no':
				break
	return(b)
def jobtracker():
	import subprocess 
	f=open('/etc/hosts'  , 'a')

	print('Enter ip of system you want to add as Job tracker')
	b=input('')
	a=subprocess.getstatusoutput("ping {} -c 2".format(b))
	if a[0]!=0:
		print('this ip is not reachable . Do you still want to add it yes/no')
		ans=input()
		if ans=='yes':
			c='{}          jt.avn\n'.format(b)
			f.write(c)
	else:
		c='{}          jt.avn\n'.format(b)
		f.write(c)
	return(c)

		

