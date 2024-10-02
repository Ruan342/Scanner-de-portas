import nmap

class NetworkScanner:

    def __init__(self):
        self.scanner = nmap.PortScanner()

    def scan_network(self, ip_range, ports):
        """
        Varre a rede com base no intervalo de IPs e nas portas fornecidas.
        """
        print(f"Iniciando a varredura na rede {ip_range} nas portas {ports}...")
        self.scanner.scan(hosts=ip_range, arguments=f'-p {ports}')  

        
        for host in self.scanner.all_hosts():
            print(f'\nHost: {host} ({self.scanner[host].hostname()})')
            print(f'Status: {self.scanner[host].state()}')

            
            if 'tcp' in self.scanner[host]:
                for port in self.scanner[host]['tcp']:
                    state = self.scanner[host]['tcp'][port]['state']
                    if state == 'open':
                        print(f'Porta {port}/tcp está {state}')
    
    def get_user_input(self):
        """
        Solicita o intervalo de IPs e portas ao usuário.
        """
        ip_range = input("Digite o IP ou intervalo de IPs (ex: 192.168.1.0/24): ")
        ports = input("Digite a porta ou intervalo de portas (ex: 22 ou 20-80): ")
        return ip_range, ports

if __name__ == "__main__":
    
    scanner = NetworkScanner()
    
    
    ip_range, ports = scanner.get_user_input()
    
    
    scanner.scan_network(ip_range, ports)
