from ../main.py import get_direction_distance

def test_get_direction_and_distance():
    # Test case 1: San Francisco to Los Angeles
    start = (37.7749, -122.4194)  # San Francisco
    end = (34.0522, -118.2437)    # Los Angeles
    direction, distance = get_direction_and_distance(start, end)
    assert direction == "South"
    assert math.isclose(distance, 559.38, rel_tol=0.01)

    # Test case 2: New York City to Miami
    start = (40.7128, -74.0060)    # New York City
    end = (25.7617, -80.1918)      # Miami
    direction, distance = get_direction_and_distance(start, end)
    assert direction == "South"
    assert math.isclose(distance, 1759.48, rel_tol=0.01)

    # Test case 3: London to Paris
    start = (51.5074, -0.1278)     # London
    end = (48.8566, 2.3522)        # Paris
    direction, distance = get_direction_and_distance(start, end)
    assert direction == "South"
    assert math.isclose(distance, 343.93, rel_tol=0.01)

    # Test case 4: Sydney to Tokyo
    start = (-33.8651, 151.2099)   # Sydney
    end = (35.6895, 139.6917)      # Tokyo
    direction, distance = get_direction_and_distance(start, end)
    assert direction == "North"
    assert math.isclose(distance, 7799.36, rel_tol=0.01)

    print("All tests passed successfully.")

test_get_direction_and_distance()