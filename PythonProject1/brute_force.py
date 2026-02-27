import random
import time
from itertools import combinations

# =============================
# GEOMETRY
# =============================

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if abs(val) < 1e-9:
        return 0
    return 1 if val > 0 else 2


def on_segment(p, q, r):
    return (min(p.x, r.x) <= q.x <= max(p.x, r.x) and
            min(p.y, r.y) <= q.y <= max(p.y, r.y))


def segments_intersect(s1, s2):
    p1, q1 = s1.p1, s1.p2
    p2, q2 = s2.p1, s2.p2

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, p2, q1): return True
    if o2 == 0 and on_segment(p1, q2, q1): return True
    if o3 == 0 and on_segment(p2, p1, q2): return True
    if o4 == 0 and on_segment(p2, q1, q2): return True

    return False


# =============================
# BRUTE FORCE
# =============================

def brute_force(segments):
    count = 0
    for s1, s2 in combinations(segments, 2):
        if segments_intersect(s1, s2):
            count += 1
    return count


def generate_segments(n, coord_range=1000):
    segments = []
    for _ in range(n):
        p1 = Point(random.uniform(0, coord_range),
                   random.uniform(0, coord_range))
        p2 = Point(random.uniform(0, coord_range),
                   random.uniform(0, coord_range))
        segments.append(Segment(p1, p2))
    return segments


def run_brute_force(n):
    segments = generate_segments(n)

    start = time.perf_counter()
    intersections = brute_force(segments)
    end = time.perf_counter()

    elapsed_ms = (end - start) * 1000
    return intersections, elapsed_ms


if __name__ == "__main__":
    N = int(input("Número de segmentos: "))
    inters, time_ms = run_brute_force(N)

    print(f"\nIntersecciones encontradas: {inters}")
    print(f"Tiempo de ejecución: {time_ms:.3f} ms")
