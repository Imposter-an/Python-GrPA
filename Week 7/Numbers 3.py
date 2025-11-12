def manhattan_distance_via_b(a: tuple, b: tuple, c: tuple) -> int:
    '''
    Given three points a, b, and c on the Cartesian plane, 
    calculate the Manhattan distance to go from point a to point c via point b.
    Manhattan distance is the sum of the absolute differences of their Cartesian coordinates.
    Args:
        a (tuple): Coordinates of point a as (x1, y1).
        b (tuple): Coordinates of point b as (x2, y2).
        c (tuple): Coordinates of point c as (x3, y3).
    Returns:
        int: The Manhattan distance from point a to point c via point b.
    '''
    # Distance from a to b
    distance_a_to_b = abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    # Distance from b to c
    distance_b_to_c = abs(b[0] - c[0]) + abs(b[1] - c[1])
    
    # Total distance via b
    return distance_a_to_b + distance_b_to_c