import re

class IPAddr:
    strIPAdress = str()
    block = list()

    def __init__(self, addr):
        self.strIPAdress = addr
        self.block = re.findall(r'(\d{1,3})' ,addr)

    def __eq__(self, other):
        return isinstance(other, IPAddr) and self.strIPAdress == other.strIPAdress

    def __hash__(self):
        return hash(self.strIPAdress)

    def __lt__(self, other):
        return ((self.block[0] != other.block[0]) and
                (self.block[1] != other.block[1]) and
                (self.block[2] != other.block[2]) and
                (self.block[3] < other.block[3]))

ip_regex_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

with open('access.log', 'r') as logFile:
    IPAdress = list({IPAddr(ip_regex_pattern.match(row).group(0)) for row in logFile})

IPAdress.sort()

for i in range (0, IPAdress.__len__()):
    print(IPAdress[i].strIPAdress)