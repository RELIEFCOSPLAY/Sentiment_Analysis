# %%
import subprocess
# %%
def snmpwalk_command(oid, ip, community):
    # Running snmpwalk using subprocess and capturing the output
    command = ['snmpwalk', '-v2c', '-c', community, ip, oid]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def get_router_name(ip, community):
    # OID for the router name (sysName)
    oid = '1.3.6.1.2.1.1.5.0'
    output = snmpwalk_command(oid, ip, community)
    print("Router Name:", output)

def get_interface_names(ip, community):
    # OID for interface names (ifDescr)
    oid = '1.3.6.1.2.1.2.2.1.2'
    output = snmpwalk_command(oid, ip, community)
    print("Interface Names:\n", output)

def get_bandwidth(ip, community):
    # OID for interface bandwidth (ifSpeed)
    oid = '1.3.6.1.2.1.2.2.1.5'
    output = snmpwalk_command(oid, ip, community)
    print("Interface Bandwidth:\n", output)

# Example usage
router_ip = '192.168.1.1'  # Replace with the actual router IP
community_string = 'public'  # Replace with the actual SNMP community string

get_router_name(router_ip, community_string)
get_interface_names(router_ip, community_string)
get_bandwidth(router_ip, community_string)
