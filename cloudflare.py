import random

# Simulated list of Cloudflare datacenters and their locations
CLOUDFLARE_DATACENTERS = {
    "IAD": {"lat": 38.9517, "lng": -77.4481},  # Washington, D.C.
    "SEA": {"lat": 47.6062, "lng": -122.3321},  # Seattle
    "LHR": {"lat": 51.5074, "lng": -0.1278},    # London
    "NRT": {"lat": 35.6895, "lng": 139.6917},   # Tokyo
}

def enumerate_caches(url):
    """
    Simulate cache enumeration by randomly selecting a datacenter.
    Replace this with actual Cloudflare Teleport logic in a real implementation.
    """
    # Simulate a cache hit in a random datacenter
    datacenter = random.choice(list(CLOUDFLARE_DATACENTERS.keys()))
    return [datacenter]