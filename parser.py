from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.inet6 import IPv6

def extract_ip_info(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = "OTHER"

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"

        return {
            "version": 4,
            "src": ip_layer.src,
            "dst": ip_layer.dst,
            "ttl": ip_layer.ttl,
            "length": ip_layer.len,
            "protocol": protocol
        }

    if IPv6 in packet:
        ip_layer = packet[IPv6]
        protocol = "OTHER"

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"

        return {
            "version": 6,
            "src": ip_layer.src,
            "dst": ip_layer.dst,
            "ttl": getattr(ip_layer, "hlim", None),
            "length": ip_layer.plen,
            "protocol": protocol
        }

    return None
