import numpy as np


def vector_angle(u, v):
    length_product = np.linalg.norm(u) * np.linalg.norm(v)
    if length_product == 0:
        raise ValueError("영벡터가 포함되면 각도를 구할 수 없습니다.")

    # 반올림 오차 때문에 arccos의 범위를 벗어나지 않도록 제한한다.
    cosine = np.clip(np.dot(u, v) / length_product, -1.0, 1.0)
    return cosine, np.arccos(cosine)


def main():
    print("[실습 1] 내적의 교환법칙")
    u = np.array([[2], [-5], [-1]])
    v = np.array([[3], [2], [-3]])
    uv = (u.T @ v).item()
    vu = (v.T @ u).item()
    print("u · v =", uv)
    print("v · u =", vu)
    print("교환법칙 확인:", uv == vu)

    print("\n[실습 2] 세 벡터 사이의 내적")
    u = np.array([1, 2, 4])
    v = np.array([2, -3, 5])
    w = np.array([4, 2, -3])
    print("u · v =", np.dot(u, v))
    print("u · w =", np.dot(u, w))
    print("v · w =", np.dot(v, w))

    print("\n[실습 3] 벡터의 길이와 거리")
    u = np.array([1, 2, 3])
    v = np.array([-4, 3, 5])
    difference = v - u
    print(f"u의 길이 = {np.linalg.norm(u):.6f}")
    print(f"v의 길이 = {np.linalg.norm(v):.6f}")
    print("v - u =", difference)
    print("각 성분의 제곱 =", difference ** 2)
    print(f"거리 = {np.linalg.norm(difference):.6f}")

    print("\n[실습 4] 내적, 길이의 제곱, 거리의 제곱")
    u = np.array([2, -5, -1])
    v = np.array([-7, -4, 6])
    difference = u - v
    print("u · v =", np.dot(u, v))
    print("||u||^2 =", np.dot(u, u))
    print("||u - v||^2 =", np.dot(difference, difference))

    print("\n[실습 5] 두 벡터 사이의 거리와 각도")
    u = np.array([1, 1, 0])
    v = np.array([0, 1, 1])
    cosine, radians = vector_angle(u, v)
    print("내적 =", np.dot(u, v))
    print(f"거리 = {np.linalg.norm(u - v):.6f}")
    print(f"cos(theta) = {cosine:.6f}")
    print(f"각도 = {np.degrees(radians):.6f}도")

    print("\n[실습 6] 라디안과 도 단위로 각도 구하기")
    u = np.array([1, -1, 0])
    v = np.array([2, -1, 2])
    cosine, radians = vector_angle(u, v)
    print("내적 =", np.dot(u, v))
    print(f"u의 길이 = {np.linalg.norm(u):.6f}")
    print(f"v의 길이 = {np.linalg.norm(v):.6f}")
    print(f"cos(theta) = {cosine:.6f}")
    print(f"각도(라디안) = {radians:.6f}")
    print(f"각도(도) = {np.degrees(radians):.6f}도")

    print("\n[실습 7] 직교 여부 확인")
    u = np.array([1, 2])
    v = np.array([6, -3])
    dot_product = np.dot(u, v)
    cosine, radians = vector_angle(u, v)
    print("내적 =", dot_product)
    print(f"cos(theta) = {cosine:.6f}")
    print(f"각도 = {np.degrees(radians):.6f}도")
    print("직교합니다." if dot_product == 0 else "직교하지 않습니다.")


if __name__ == "__main__":
    main()
