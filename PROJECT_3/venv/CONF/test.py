import rich
t = [
    '192.168.1.15',
    {
        'interface Loopback0': 'ip address 150.1.5.5 255.255.255.255',
        'interface Tunnel0': 'ip address 155.1.0.5 255.255.255.0',
        'interface GigabitEthernet0/0': 'ip address 192.168.1.15 255.255.255.0',
        'interface GigabitEthernet0/1.5': 'ip address 155.1.5.5 255.255.255.0',
        'interface GigabitEthernet0/1.45': 'ip address 155.1.45.5 255.255.255.0',
        'interface GigabitEthernet0/1.58': 'ip address 155.1.58.5 255.255.255.0',
        'interface GigabitEthernet0/1.100': 'ip address 169.254.100.5 255.255.255.0'
    }
    '192.168.1.11',
    {
        'interface Loopback0': 'ip address 150.1.2.2 255.255.255.255',
        'interface Tunnel0': 'ip address 155.1.0.5 255.255.255.0',
        'interface GigabitEthernet0/0': 'ip address 192.168.1.15 255.255.255.0',
        'interface GigabitEthernet0/1.5': 'ip address 155.1.5.5 255.255.255.0',
        'interface GigabitEthernet0/1.45': 'ip address 155.1.45.5 255.255.255.0',
        'interface GigabitEthernet0/1.58': 'ip address 155.1.58.5 255.255.255.0',
        'interface GigabitEthernet0/1.100': 'ip address 169.254.100.5 255.255.255.0'
    }
]
print(t)
