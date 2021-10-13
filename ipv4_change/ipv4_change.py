import wmi
import sys

# Set IP and Subnet
ip = u'192.168.1.22'
subnetmask = u'255.255.255.0'

# Set network configuration adapters to "network_config"
network_config = wmi.WMI('').Win32_NetworkAdapterConfiguration(IPEnabled=True)

# Get the first network adapter
network_adapter = network_config[0]

# Attempt to change IP and Subnet based on constants
try:
    network_adapter.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
except Exception as e:
    print('Failed to change IP and Subnet', e)
    sys.exit(1)

print('SUCCESS!! IP changed to: {0} | Subnet changed to: {1}'.format(ip, subnetmask))
