EPS = 1e-9

# =====================================
# CLASES
# =====================================

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equals(self, other):
        return abs(self.x - other.x) < EPS and abs(self.y - other.y) < EPS

    def __repr__(self):
        return f"({self.x:.3f}, {self.y:.3f})"


class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"[{self.p1} - {self.p2}]"


# =====================================
# GEOMETRÍA
# =====================================

def orientation(p, q, r):
    val = (q.y - p.y)*(r.x - q.x) - (q.x - p.x)*(r.y - q.y)
    if abs(val) < EPS:
        return 0
    return 1 if val > 0 else 2


def on_segment(p, q, r):
    return (min(p.x, r.x) - EPS <= q.x <= max(p.x, r.x) + EPS and
            min(p.y, r.y) - EPS <= q.y <= max(p.y, r.y) + EPS)


def compute_intersection(s1, s2):
    x1, y1 = s1.p1.x, s1.p1.y
    x2, y2 = s1.p2.x, s1.p2.y
    x3, y3 = s2.p1.x, s2.p1.y
    x4, y4 = s2.p2.x, s2.p2.y

    denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)

    if abs(denom) < EPS:
        return None  # paralelos o colineales

    px = ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4 - y3*x4)) / denom
    py = ((x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4 - y3*x4)) / denom

    return Point(px, py)


# =====================================
# EJERCICIO 2.4
# =====================================

def find_all_intersections(segments):

    proper_intersections = []
    endpoint_map = {}   # punto -> lista de segmentos que lo contienen
    overlaps = []

    n = len(segments)

    # Revisar todos contra todos
    for i in range(n):
        for j in range(i + 1, n):

            s1 = segments[i]
            s2 = segments[j]

            p1, q1 = s1.p1, s1.p2
            p2, q2 = s2.p1, s2.p2

            o1 = orientation(p1, q1, p2)
            o2 = orientation(p1, q1, q2)
            o3 = orientation(p2, q2, p1)
            o4 = orientation(p2, q2, q1)

            # ------------------------------
            # 1️⃣ INTERSECCIÓN PROPIA
            # ------------------------------
            if o1 != o2 and o3 != o4:
                inter = compute_intersection(s1, s2)
                if inter is not None:
                    duplicate = False
                    for p in proper_intersections:
                        if p.equals(inter):
                            duplicate = True
                            break
                    if not duplicate:
                        proper_intersections.append(inter)

            # ------------------------------
            # 2️⃣ COLINEALIDAD Y OVERLAP
            # ------------------------------
            if o1 == 0 and o2 == 0 and o3 == 0 and o4 == 0:
                # Segmentos colineales
                overlaps.append((s1, s2))

            # ------------------------------
            # 3️⃣ ENDPOINTS COMPARTIDOS
            # ------------------------------
            for point in [p1, q1]:
                if on_segment(p2, point, q2):
                    key = (round(point.x, 9), round(point.y, 9))
                    if key not in endpoint_map:
                        endpoint_map[key] = []
                    endpoint_map[key].append(s2)

            for point in [p2, q2]:
                if on_segment(p1, point, q1):
                    key = (round(point.x, 9), round(point.y, 9))
                    if key not in endpoint_map:
                        endpoint_map[key] = []
                    endpoint_map[key].append(s1)

    return proper_intersections, overlaps, endpoint_map


# =====================================
# DEMOSTRACIÓN
# =====================================

if __name__ == "__main__":

    segments = [
        Segment(Point(0,0), Point(4,4)),        # diagonal
        Segment(Point(0,4), Point(4,0)),        # diagonal cruzada
        Segment(Point(2,0), Point(2,4)),        # vertical
        Segment(Point(0,0), Point(2,2)),        # comparte extremo
        Segment(Point(-1,0), Point(2,0)),       # colineal horizontal
        Segment(Point(0,0), Point(1,0))         # colineal horizontal
    ]

    proper, overlaps, endpoint_map = find_all_intersections(segments)

    print("INTERSECCIONES PROPIAS:")
    for p in proper:
        print(p)

    print("\nSEGMENTOS COLINEALES / OVERLAP:")
    for pair in overlaps:
        print(pair)

    print("\nENDPOINTS Y SEGMENTOS QUE LOS CONTIENEN:")
    for key in endpoint_map:
        print(key, "->", endpoint_map[key])
