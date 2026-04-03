from collections import Counter

class TrafficStats:
    def __init__(self):
        self.total_packets = 0
        self.protocol_counter = Counter()
        self.top_sources = Counter()
        self.top_destinations = Counter()

    def update(self, packet_info):
        self.total_packets += 1
        self.protocol_counter[packet_info["protocol"]] += 1
        self.top_sources[packet_info["src"]] += 1
        self.top_destinations[packet_info["dst"]] += 1

    def summary(self):
        return {
            "total_packets": self.total_packets,
            "protocols": dict(self.protocol_counter),
            "top_sources": dict(self.top_sources.most_common(5)),
            "top_destinations": dict(self.top_destinations.most_common(5)),
        }
