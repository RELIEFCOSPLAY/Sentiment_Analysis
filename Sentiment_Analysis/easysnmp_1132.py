from easysnmp import Session

# Set up the session (replace IP and community with your router's values)
session = Session(hostname='192.168.121.129', community='public', version=2)  # SNMPv2

# OIDs
oids = {
    'sysName': '1.3.6.1.2.1.1.5.0',       # Router Name OID
    'ifDescr': '1.3.6.1.2.1.2.2.1.2',     # Interface Name OID
    'ifSpeed': '1.3.6.1.2.1.2.2.1.5'      # Bandwidth OID
}

# Fetch the router name
router_name = session.get(oids['sysName'])
print(f"Router Name: {router_name.value}")

# Fetch all interface names
interface_names = session.walk(oids['ifDescr'])
print("\nInterface Names:")
for interface in interface_names:
    print(f" - {interface.value}")

# Fetch all interface bandwidths
bandwidths = session.walk(oids['ifSpeed'])
print("\nInterface Bandwidth (bps):")
for idx, bandwidth in enumerate(bandwidths):
    print(f"Interface {interface_names[idx].value}: {bandwidth.value} bps")
