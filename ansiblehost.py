def datanode(slave):
	f=open('/etc/ansible/hosts' , 'a')
	a='[slave]\n'
	f.write(a)
	for i in slave:
		c='{}	ansible_user=root	ansible_ssh_pass=toor\n'.format(i)
		f.write(c)


def tasktraker(tt):
	f=open('/etc/ansible/hosts' , 'a')
	a='[tt]\n'
	f.write(a)
	for i in tt:

		c='{}	ansible_user=root	ansible_ssh_pass=toor\n'.format(i)
		f.write(c)


def namenode(master):
	f=open('/etc/ansible/hosts' , 'a')
	a='[master]\n'
	f.write(a)
	c='{}	ansible_user=root	ansible_ssh_pass=toor\n'.format(master)
	f.write(c)

def jobtracker(jt):
	f=open('/etc/ansible/hosts' , 'a')
	a='[jt]\n'
	f.write(a)
	c='{}	ansible_user=root	ansible_ssh_pass=toor\n'.format(jt)
	f.write(c)
