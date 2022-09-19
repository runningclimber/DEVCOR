import ipaddress

class IPCalculator:

    def __init__(self, network):
        self.network = ipaddress.IPv4Network(network)

    def get_network(self):
        return str(self.network)

    def get_first_ip(self):
        nework_address = self.get_network_address()
        first_ip = network_address + 1
        return str(first_ip)

    def get_last_ip(self):
        broadcast_address = self.get_broadcast_address()
        last_ip = broadcast_address -1
        return str(last_ip)

    def get_broadcast_address(self):
        return self.network.broadcast_address

    def get_network_address(self):
        return self.network.network_address

    def get_netmask(self):
        return self.network.netmask
