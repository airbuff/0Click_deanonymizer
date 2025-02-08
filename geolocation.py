def estimate_location(caches):
    """
    Estimate the target's location based on the datacenter that cached the resource.
    """
    # Simulated datacenter locations
    CLOUDFLARE_DATACENTERS = {
        "IAD": {"lat": 38.9517, "lng": -77.4481},  # Washington, D.C.
        "SEA": {"lat": 47.6062, "lng": -122.3321},  # Seattle
        "LHR": {"lat": 51.5074, "lng": -0.1278},    # London
        "NRT": {"lat": 35.6895, "lng": 139.6917},   # Tokyo
    }

    # Get the location of the first datacenter with a cache hit
    datacenter = caches[0]
    return CLOUDFLARE_DATACENTERS.get(datacenter, {"lat": 37.7749, "lng": -122.4194})  # Default to San Francisco