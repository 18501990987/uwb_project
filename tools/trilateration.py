import math

# 三个 Anchor 坐标
A = (0.0, 0.0)
B = (3.0, 0.0)
C = (0.0, 2.5)

def trilaterate(d1, d2, d3):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    A1 = 2 * (x2 - x1)
    B1 = 2 * (y2 - y1)
    C1 = d1**2 - d2**2 - x1**2 + x2**2 - y1**2 + y2**2

    A2 = 2 * (x3 - x1)
    B2 = 2 * (y3 - y1)
    C2 = d1**2 - d3**2 - x1**2 + x3**2 - y1**2 + y3**2

    denom = A1 * B2 - B1 * A2
    if abs(denom) < 1e-6:
        return None

    x = (C1 * B2 - B1 * C2) / denom
    y = (A1 * C2 - C1 * A2) / denom
    return (x, y)

if __name__ == "__main__":
    # 假设某个点到三个 Anchor 的距离
    d1 = 1.56
    d2 = 2.06
    d3 = 1.92

    pos = trilaterate(d1, d2, d3)
    print("position =", pos)