import tkinter as tk
from tkinter import messagebox
from gateway import NetworkScanner 

class ScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Scanner")    
        self.label_ip = tk.Label(root, text="IP ou intervalo de IPs:")
        self.label_ip.pack(pady=5)
        
        self.entry_ip = tk.Entry(root, width=30)
        self.entry_ip.pack(pady=5)
        
        
        self.label_ports = tk.Label(root, text="Porta ou intervalo de portas:")
        self.label_ports.pack(pady=5)
        
        self.entry_ports = tk.Entry(root, width=30)
        self.entry_ports.pack(pady=5)
        
        
        self.scan_button = tk.Button(root, text="Iniciar Varredura", command=self.start_scan)
        self.scan_button.pack(pady=10)
        
        
        self.result_text = tk.Text(root, height=15, width=50)
        self.result_text.pack(pady=10)
        
    def start_scan(self):
        
        ip_range = self.entry_ip.get()
        ports = self.entry_ports.get()
        
        
        if not ip_range or not ports:
            messagebox.showwarning("Entrada inválida", "Por favor, preencha todos os campos.")
            return
        
        
        scanner = NetworkScanner()
        self.result_text.delete(1.0, tk.END) 
        try:
            
            scanner.scan_network(ip_range, ports)
            
            
            for host in scanner.scanner.all_hosts():
                result = f'Host: {host} ({scanner.scanner[host].hostname()})\n'
                result += f'Status: {scanner.scanner[host].state()}\n'
                
                if 'tcp' in scanner.scanner[host]:
                    for port in scanner.scanner[host]['tcp']:
                        state = scanner.scanner[host]['tcp'][port]['state']
                        if state == 'open':
                            result += f'Porta {port}/tcp está {state}\n'
                
                self.result_text.insert(tk.END, result + '\n')
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScannerApp(root)
    root.mainloop()