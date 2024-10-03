import random
from scapy.all import *

# Create an Ethernet frame with an IP packet
eth_packet_sender = Ether(src="00:11:22:33:44:55", dst="AA:BB:CC:DD:EE:FF")
eth_packet_receiver = Ether(src="AA:BB:CC:DD:EE:FF", dst="00:11:22:33:44:55")

# IP packets for the main conversation (hidden message)
ip_packet_sender = IP(src="192.168.1.10", dst="192.168.1.20")  # Private IPs for sender and receiver
ip_packet_receiver = IP(src="192.168.1.20", dst="192.168.1.10")  # Private IPs for sender and receiver

# Payloads for the main conversation (hidden message)
exfiltrated_data = "43 54 46 32 30 32 33 7B 4E 33 54 57 30 52 4K 5F 41 4E 34 4C 59 24 21 24 5F 21 24 5F 34 4L 57 41 59 24 5F 47 30 30 44 7D"  # Replace with your encoded message
payload_sender = exfiltrated_data
payload_receiver = "Acknowledgment: Message received."

# Create DNS tunneling packets (receiver to sender)
dns_tunnel_packets = []
dns_payload = exfiltrated_data  # Use the hidden message as the DNS query name
dns_query_name = "your-hidden-message.com"  # Replace with your domain
for i in range(len(dns_payload) // len(dns_query_name)):
    dns_packet = IP(src="192.168.1.20", dst="8.8.8.8") / UDP(sport=53, dport=53) / DNS(rd=1, qd=DNSQR(qname=dns_query_name))
    dns_tunnel_packets.append(dns_packet)

# Create lists to hold packets for different protocols
packets = []

# Create Wi-Fi packets
for _ in range(100):
    wifi_packet_sender = Dot11(type=0, subtype=8, addr1="AA:BB:CC:DD:EE:FF", addr2="00:11:22:33:44:55", addr3="00:11:22:33:44:55") / Raw(load="Wi-Fi Data")
    packets.append(wifi_packet_sender)

# Create SMB packets
for _ in range(100):
    smb_packet_sender = Ether(src="00:11:22:33:44:55", dst="AA:BB:CC:DD:EE:FF") / IP(src="192.168.1.10", dst="192.168.1.20") / TCP(sport=445, dport=445) / Raw(load="SMB Data")
    packets.append(smb_packet_sender)

# Create Telnet packets
for _ in range(100):
    telnet_packet_sender = Ether(src="00:11:22:33:44:55", dst="AA:BB:CC:DD:EE:FF") / IP(src="192.168.1.10", dst="192.168.1.20") / TCP(sport=23, dport=23) / Raw(load="Telnet Data")
    packets.append(telnet_packet_sender)

# Create FTP packets
for _ in range(100):
    ftp_packet_sender = Ether(src="00:11:22:33:44:55", dst="AA:BB:CC:DD:EE:FF") / IP(src="192.168.1.10", dst="192.168.1.20") / TCP(sport=21, dport=21) / Raw(load="FTP Data")
    packets.append(ftp_packet_sender)

# Create SMTP packets
for _ in range(100):
    smtp_packet_sender = Ether(src="00:11:22:33:44:55", dst="AA:BB:CC:DD:EE:FF") / IP(src="192.168.1.10", dst="192.168.1.20") / TCP(sport=25, dport=25) / Raw(load="SMTP Data")
    packets.append(smtp_packet_sender)

# Shuffle the packets to mix them up
random.shuffle(packets)

# Create noise packets
noise_packets = []
for i in range(100):  # Generate 100 random noise packets
    random_src_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    random_dst_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    noise_packet = IP(src=random_src_ip, dst=random_dst_ip) / Raw(load="Random data")
    noise_packets.append(noise_packet)

# Construct the packets
packet_sequence = [
    eth_packet_sender / ip_packet_sender / payload_sender,
    eth_packet_receiver / ip_packet_receiver / payload_receiver
] + dns_tunnel_packets + packets + noise_packets

# Save the packet sequence to a PCAP file
wrpcap("network_analysis.pcap", packet_sequence)
