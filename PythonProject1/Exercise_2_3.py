import math

EPS = 1e-9

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x:.3f}, {self.y:.3f})"


class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


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


def segments_intersect(s1, s2):
    p1, q1 = s1.p1, s1.p2
    p2, q2 = s2.p1, s2.p2

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return compute_intersection(s1, s2)

    if o1 == 0 and on_segment(p1, p2, q1): return p2
    if o2 == 0 and on_segment(p1, q2, q1): return q2
    if o3 == 0 and on_segment(p2, p1, q2): return p1
    if o4 == 0 and on_segment(p2, q1, q2): return q1

    return None


# Ejemplo prueba
if __name__ == "__main__":
    s1 = Segment(Point(0, 0), Point(4, 4))
    s2 = Segment(Point(0, 4), Point(4, 0))

    inter = segments_intersect(s1, s2)

    if inter:
        print("Intersección en:", inter)
    else:
        print("No se intersectan")
