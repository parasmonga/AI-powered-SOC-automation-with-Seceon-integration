from src.threat_intel.reputation import ThreatIntel

intel = ThreatIntel()

print(intel.lookup("192.168.10.5"))

print(intel.lookup("185.220.101.15"))

print(intel.lookup("8.8.8.8"))