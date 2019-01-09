import os
import subprocess

def make_hostfile(hosts):
    string = "scontrol show hostname " +hosts
    cmd = string.split(" ")
    with open("hosts.txt","w") as stdout:
    	process = subprocess.Popen(cmd, stdout=stdout)
    process.communicate()

hosts = os.environ['SLURM_JOB_NODELIST']
make_hostfile(hosts)


#def get_hosts():
#    f = open("hosts.txt",'r')
#    hosts = f.readlines()
#    f.close()
#    for i in hosts:
#    	cmd = ['ssh-copy-id', str(i)]
#        process = subprocess.Popen(cmd)
#        process.communicate()
#
#get_hosts()
