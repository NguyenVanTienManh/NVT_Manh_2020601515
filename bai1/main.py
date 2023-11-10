import numpy as np

def giai_he_phuong_trinh(A, b):
    try:
        x = np.linalg.solve(A, b)
        return x
    except np.linalg.LinAlgError as e:
        if 'Singular matrix' in str(e):
            return None  # Hệ phương trình vô số nghiệm
        return "Vô nghiệm"  # Hệ phương trình vô nghiệm

def nhap_ma_tran():
    n = int(input("Nhập số phương trình và số ẩn n: "))
    A = []
    b = []
    for i in range(n):
        print(f"Nhập phương trình thứ {i + 1} (dạng [a1, a2, ..., an]):")
        row = list(map(float, input().split()))
        A.append(row)
        b.append(float(input(f"Nhập giá trị b{i + 1}: ")))

    return A, b

if __name__ == "__main__":
    A, b = nhap_ma_tran()
    result = giai_he_phuong_trinh(A, b)

    if result is not None:
        if type(result) == str:
            print(result)  # Hệ phương trình vô nghiệm
        else:
            print("Nghiệm của hệ phương trình:")
            for i in range(len(result)):
                print(f"x{i+1} = {result[i]}")
    else:
        print("Hệ phương trình có vô số nghiệm.")
