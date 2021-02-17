import subprocess
import re

def getIP(ip):
    print('START TRACERT!')
    prcs = subprocess.Popen(f'tracert {ip}', shell=True, stdout=subprocess.PIPE)

    subprocess_return = prcs.stdout.read()

    addresses = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', str(subprocess_return));
    print('END TRACERT!')
    return addresses