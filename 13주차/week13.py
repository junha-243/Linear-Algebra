import numpy as np


def check_cross_product(u, v):
    u1, u2, u3 = u
    v1, v2, v3 = v
    # 행렬식 전개에서 가운데 성분의 부호를 바꾼다.
    cross = np.array([
        u2 * v3 - u3 * v2,
        -(u1 * v3 - u3 * v1),
        u1 * v2 - u2 * v1,
    ])
    reference = np.cross(u, v)
    print("i, j, k 성분 =", *cross)
    print("u × v =", cross)
    print("NumPy 결과 =", reference)
    print("결과 일치 =", np.array_equal(cross, reference))
    print("u · (u × v) =", np.dot(u, cross))
    print("v · (u × v) =", np.dot(v, cross))


def main():
    print("[실습 1] 외적 계산과 수직 확인")
    check_cross_product(np.array([4, 1, 1]), np.array([2, 1, 0]))

    print("\n[실습 2] 외적 계산과 수직 확인")
    check_cross_product(np.array([3, -1, 2]), np.array([1, -2, 4]))

    print("\n[실습 3-1] 평행사변형의 넓이")
    u = np.array([3, 1, 0])
    v = np.array([1, 3, 2])
    cross = np.cross(u, v)
    print("u × v =", cross)
    print("넓이의 제곱 =", np.dot(cross, cross))
    print(f"평행사변형의 넓이 = {np.linalg.norm(cross):.6f}")

    print("\n[실습 3-2] 삼각형의 넓이")
    a = np.array([-1, 2, 0])
    b = np.array([2, 1, 3])
    c = np.array([1, 1, -1])
    u = b - a
    v = c - a
    cross = np.cross(u, v)
    area = np.linalg.norm(cross)
    print("u =", u)
    print("v =", v)
    print("u × v =", cross)
    print(f"평행사변형의 넓이 = {area:.6f}")
    print(f"삼각형의 넓이 = {area / 2:.6f}")

    print("\n[실습 4] 평행육면체의 체적")
    u = np.array([4, 1, 1])
    v = np.array([2, 1, 0])
    w = np.array([0, 2, 3])
    cross = np.cross(u, v)
    base_area = np.linalg.norm(cross)
    height = abs(np.dot(w, cross / base_area))
    print("u × v =", cross)
    print(f"밑면 넓이 = {base_area:.6f}")
    print(f"수직 높이 = {height:.6f}")
    print(f"밑면 × 높이로 구한 체적 = {base_area * height:.6f}")
    print(f"삼중곱으로 구한 체적 = {abs(np.dot(cross, w)):.6f}")
    print(f"행렬식으로 구한 체적 = {abs(np.linalg.det(np.vstack([u, v, w]))):.6f}")

    print("\n[실습 5] 세 가지 방법으로 내적 계산")
    u = np.array([2, -5, -1])
    v = np.array([3, 2, -3])
    products = u * v
    uv = np.dot(u, v)
    vu = np.dot(v, u)
    u_column = u.reshape(3, 1)
    v_column = v.reshape(3, 1)
    print("성분별 곱 =", products)
    print("성분별 곱의 합 =", np.sum(products))
    print("u · v =", uv)
    print("v · u =", vu)
    print("u^T v =", (u_column.T @ v_column).item())
    print("교환법칙 확인 =", uv == vu)

    print("\n[실습 6] 직교 여부와 사이각")
    u = np.array([2, -4])
    v = np.array([4, 2])
    dot = np.dot(u, v)
    print("u · v =", dot)
    print("직교합니다." if np.isclose(dot, 0) else "직교하지 않습니다.")
    length_product = np.linalg.norm(u) * np.linalg.norm(v)
    if length_product > 0:
        cosine = np.clip(dot / length_product, -1.0, 1.0)
        print(f"두 벡터의 사이각 = {np.degrees(np.arccos(cosine)):.2f}도")
    else:
        print("영벡터가 포함되면 사이각을 구할 수 없습니다.")


if __name__ == "__main__":
    main()
