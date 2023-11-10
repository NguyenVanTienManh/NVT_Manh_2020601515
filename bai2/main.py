import sympy as sp
import tkinter as tk
from tkinter import messagebox
import webbrowser

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

tinh_tich_phan_button = tk.Button(root, text="Tính tích phân", command=tinh_nguyen_ham)
tinh_tich_phan_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

tim_kiem_button = tk.Button(root, text="Tìm tài liệu học tập", command=tim_kiem_tai_lieu)
tim_kiem_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

ket_qua_label = tk.Label(root, text="", wraplength=300)
ket_qua_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

thoat_button = tk.Button(root, text="Thoát", command=thoat_chuong_trinh)
thoat_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Bắt đầu chương trình
root.mainloop()
