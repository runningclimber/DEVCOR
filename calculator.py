import ipaddress
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--network', help="The network in the format x.x.x.x/x.")
    args = parser.parse_args()
    return args.network

class IPCalculator:

    def __init__(self, network):
        self.network = ipaddress.IPv4Network(network)

    @property
    def broadcast_address(self):
        if self.network: 
            return self.network.broadcast_address

    @property
    def network_address(self):
        if self.network:
            return self.network.network_address

    @property
    def netmask(self):
        if self.network:
            return self.network.netmask

    def get_network(self):
        """ Returns the network """

        return str(self.network)

    def get_first_ip(self):
        """ Calculates the first IP address. """

        first_ip = list(self.network.hosts())[0]
        return str(first_ip)

    def get_last_ip(self):
        """ Calculates the last IP address."""

        last_ip = list(self.network.hosts())[-1]
        return str(last_ip)
 
    def calculate(self):
        """ Prints the calculation results. """

        print('The results of the calculation is:')
        print(f'-> Input network:\t\t{self.get_network()}')
        print(f'-> Network address:\t\t{self.get_network_address()}')
        print(f'-> Netmask:\t\t\t{self.get_netmask()}')
        print(f'-> Broadcast address:\t\t{self.get_broadcast_address()}')
        print(f'-> First IP address:\t\t{self.get_first_ip()}')
        print(f'-> Last IP address:\t\t{self.get_last_ip()}')

if __name__ == "__main__":
    net = parse_arguments()
    calc = IPCalculator(net)
    calc.calculate()
