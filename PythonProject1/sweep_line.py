import random
import time
import heapq
from itertools import combinations

# =====================================================
# CONFIGURACIÓN
# =====================================================

RANDOM_SEED = 42
COORD_RANGE = 1000

# =====================================================
# GEOMETRÍA
# =====================================================

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, p1, p2):
        if p1.x < p2.x:
            self.left = p1
            self.right = p2
        else:
            self.left = p2
            self.right = p1


def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if abs(val) < 1e-9:
        return 0
    return 1 if val > 0 else 2


def on_segment(p, q, r):
    return (min(p.x, r.x) <= q.x <= max(p.x, r.x) and
            min(p.y, r.y) <= q.y <= max(p.y, r.y))


def segments_intersect(s1, s2):
    p1, q1 = s1.left, s1.right
    p2, q2 = s2.left, s2.right

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


# =====================================================
# GENERADOR DE SEGMENTOS (MISMO PARA AMBOS)
# =====================================================

def generate_segments(n):
    random.seed(RANDOM_SEED)
    segments = []
    for _ in range(n):
        p1 = Point(random.uniform(0, COORD_RANGE),
                   random.uniform(0, COORD_RANGE))
        p2 = Point(random.uniform(0, COORD_RANGE),
                   random.uniform(0, COORD_RANGE))
        segments.append(Segment(p1, p2))
    return segments


# =====================================================
# FUERZA BRUTA
# =====================================================

def brute_force(segments):
    count = 0
    for s1, s2 in combinations(segments, 2):
        if segments_intersect(s1, s2):
            count += 1
    return count


# =====================================================
# SWEEP LINE (MISMAS INTERSECCIONES)
# =====================================================

def sweep_line(segments):
    events = []
    active = []
    intersections = 0

    for seg in segments:
        heapq.heappush(events, (seg.left.x, 0, seg))
        heapq.heappush(events, (seg.right.x, 1, seg))

    while events:
        x, event_type, seg = heapq.heappop(events)

        if event_type == 0:
            for other in active:
                if segments_intersect(seg, other):
                    intersections += 1
            active.append(seg)
        else:
            if seg in active:
                active.remove(seg)

    return intersections


# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    N = int(input("Número de segmentos: "))

    segments = generate_segments(N)

    # ---- Fuerza Bruta ----
    start = time.perf_counter()
    brute_count = brute_force(segments)
    brute_time = (time.perf_counter() - start) * 1000

    # ---- Sweep Line ----
    start = time.perf_counter()
    sweep_count = sweep_line(segments)
    sweep_time = (time.perf_counter() - start) * 1000

    print("\nRESULTADOS")
    print("====================================")
    print(f"Intersecciones (Fuerza Bruta): {brute_count}")
    print(f"Tiempo Fuerza Bruta: {brute_time:.3f} ms\n")

    print(f"Intersecciones (Sweep Line): {sweep_count}")
    print(f"Tiempo Sweep Line: {sweep_time:.3f} ms\n")

    if brute_count == sweep_count:
        print("✔ Ambos algoritmos encontraron exactamente las mismas intersecciones.")
    else:
        print("✘ Hay diferencia en el conteo (revisar implementación).")
