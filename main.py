import argparse
from sniffer import start_sniffing
from stats import TrafficStats

def main():
    parser = argparse.ArgumentParser(description="LAN IP Packet Sniffer")
    parser.add_argument("--iface", required=True, help="Network interface to sniff on")
    parser.add_argument("--count", type=int, default=20, help="Number of packets to capture (0 = unlimited)")
    args = parser.parse_args()

    stats = TrafficStats()

    def handle_packet(packet_info):
        stats.update(packet_info)
        print(
            f"[IPv{packet_info['version']}] "
            f"{packet_info['src']} -> {packet_info['dst']} "
            f"| proto={packet_info['protocol']} "
            f"| len={packet_info['length']} "
            f"| ttl/hlim={packet_info['ttl']}"
        )

    try:
        start_sniffing(interface=args.iface, packet_callback=handle_packet, packet_count=args.count)
    except KeyboardInterrupt:
        pass
    finally:
        print("\n=== Traffic Summary ===")
        print(stats.summary())

if __name__ == "__main__":
    main()
