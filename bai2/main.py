import sympy as sp
import tkinter as tk
from tkinter import messagebox
import webbrowser
import random

cau_hoi = [
    "Câu 1: Đạo hàm của hàm số f(x) = x^2 là gì?",
    "Câu 2: Tích phân của hàm số g(x) = sin(x) là gì?",
    "Câu 3: Tích phân xác định của hàm số h(x) = 1 từ 0 đến 1 là bao nhiêu?",
    "Câu 4: Đạo hàm của hàm số k(x) = e^x là gì?",
    "Câu 5: Đạo hàm riêng của hàm số m(x, y) = x^2y là gì?"
]
dap_an_dung = [
    ["2x", "-2x", "2", "2x^2"],
    ["-cos(x)", "tan(x)", "cot(x)", "cos(x)"],
    ["1", "-1", "2", "-2"],
    ["e^x", "-e^x", "x*e^x", "-x*e^x"],
    ["2xy", "-2xy", "2y^x", "-2y^x"]
]
# Hàm để tính đạo hàm của một hàm số
def tinh_dao_ham():
    try:
        bieu_thuc = sp.simplify(bieu_thuc_entry.get())
        dao_ham = sp.diff(bieu_thuc)
        ket_qua_label.config(text="Đạo hàm của hàm số là: " + str(dao_ham))
    except Exception as e:
        messagebox.showerror("Lỗi", "Lỗi xảy ra: " + str(e))

def tinh_nguyen_ham():
    try:
        bieu_thuc = sp.simplify(bieu_thuc_entry.get())
        nguyen_ham = sp.integrate(bieu_thuc)
        ket_qua_label.config(text="Nguyên hàm của hàm số là: " + str(nguyen_ham))
    except Exception as e:
        messagebox.showerror("Lỗi", "Lỗi xảy ra: " + str(e))

# Hàm để tìm kiếm tài liệu học tập trên trình duyệt web
def tim_kiem_tai_lieu():
    query = bieu_thuc_entry.get() + " tài liệu giải tích "
    search_url = "https://www.google.com/search?q=" + query
    webbrowser.open(search_url)
def kiem_tra_kien_thuc():
    # Tạo cửa sổ con
    second_window = tk.Toplevel(root)
    second_window.title("Kiểm tra kiến thức")

    ket_qua = tk.Label(second_window, text="", wraplength=300)
    ket_qua.pack(padx=10, pady=10)

    # Tạo biến để lưu trạng thái câu hỏi
    trang_thai_cau_hoi = tk.IntVar()
    trang_thai_cau_hoi.set(0)

    # Hàm kiểm tra câu hỏi
    def kiem_tra_cau_hoi():
        cau_hoi_so = trang_thai_cau_hoi.get()
        tra_loi = trang_thai_lua_chon.get()
        if tra_loi == dap_an_dung[cau_hoi_so][0]:
            ket_qua.config(text="Câu hỏi {} - Đúng".format(cau_hoi_so + 1))
        else:
            ket_qua.config(text="Câu hỏi {} - Sai".format(cau_hoi_so + 1))

    # Hàm để tạo đáp án ngẫu nhiên
    def tao_dap_an_ngau_nhien():
        cau_hoi_so = trang_thai_cau_hoi.get()
        dap_an_ngau_nhien = random.sample(dap_an_dung[cau_hoi_so], len(dap_an_dung[cau_hoi_so]))
        random.shuffle(dap_an_ngau_nhien)
        return dap_an_ngau_nhien

    # Tạo phần giao diện cho câu hỏi và đáp án
    cau_hoi_label = tk.Label(second_window, text=cau_hoi[0])
    cau_hoi_label.pack(padx=10, pady=10)

    trang_thai_lua_chon = tk.StringVar()
    dap_an_ngau_nhien = tao_dap_an_ngau_nhien()
    radio_buttons = []
    for i, lua_chon in enumerate(dap_an_ngau_nhien):
        radio_button = tk.Radiobutton(second_window, text=chr(65 + i) + ". " + lua_chon,
                                      variable=trang_thai_lua_chon, value=lua_chon)
        radio_button.pack(anchor='w', padx=10, pady=5)
        radio_buttons.append(radio_button)

    kiem_tra_button = tk.Button(second_window, text="Kiểm tra", command=kiem_tra_cau_hoi)
    kiem_tra_button.pack(padx=10, pady=10)

    # Tạo nút chuyển câu hỏi
    def chuyen_cau_hoi():
        nonlocal cau_hoi_label
        cau_hoi_so = trang_thai_cau_hoi.get()
        if cau_hoi_so < 4:
            cau_hoi_so += 1
            trang_thai_cau_hoi.set(cau_hoi_so)
            cau_hoi_label.config(text=cau_hoi[cau_hoi_so])
            ket_qua.config(text="")
            trang_thai_lua_chon.set(None)
            dap_an_ngau_nhien = tao_dap_an_ngau_nhien()
            for i, lua_chon in enumerate(dap_an_ngau_nhien):
                trang_thai_lua_chon.set(None)
                radio_buttons[i].config(text=chr(65 + i) + ". " + lua_chon, value=lua_chon)
        else:
            trang_thai_cau_hoi.set(0)
            second_window.destroy()

    chuyen_cau_hoi_button = tk.Button(second_window, text="Câu tiếp theo", command=chuyen_cau_hoi)
    chuyen_cau_hoi_button.pack(padx=10, pady=10)


# Hàm để đóng ứng dụng
def thoat_chuong_trinh():
    root.destroy()

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Chương trình Giải tích")

# Tạo và thiết lập các phần tử giao diện
bieu_thuc_label = tk.Label(root, text="Nhập biểu thức hàm số:")
bieu_thuc_label.grid(row=0, column=0, padx=10, pady=10)

bieu_thuc_entry = tk.Entry(root, width=40)
bieu_thuc_entry.grid(row=0, column=1, padx=10, pady=10)

tinh_dao_ham_button = tk.Button(root, text="Tính đạo hàm", command=tinh_dao_ham)
tinh_dao_ham_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

tinh_tich_phan_button = tk.Button(root, text="Tính nguyên hàm", command=tinh_nguyen_ham)
tinh_tich_phan_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

kiem_tra_button = tk.Button(root, text="Kiểm tra kiến thức", command=kiem_tra_kien_thuc)
kiem_tra_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

tim_kiem_button = tk.Button(root, text="Tìm tài liệu học tập", command=tim_kiem_tai_lieu)
tim_kiem_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

ket_qua_label = tk.Label(root, text="", wraplength=300)
ket_qua_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

thoat_button = tk.Button(root, text="Thoát", command=thoat_chuong_trinh)
thoat_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Bắt đầu chương trình
root.mainloop()
