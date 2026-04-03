from scapy.all import sniff
from parser import extract_ip_info

def start_sniffing(interface, packet_callback, packet_count=0, bpf_filter="ip or ip6"):
    def process_packet(packet):
        packet_info = extract_ip_info(packet)
        if packet_info:
            packet_callback(packet_info)

    sniff(
        iface=interface,
        prn=process_packet,
        filter=bpf_filter,
        store=False,
        count=packet_count
    )
