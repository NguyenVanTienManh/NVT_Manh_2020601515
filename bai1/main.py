import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import numpy as np

class LinearEquationSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Linear Equation Solver")

        self.num_equations = self.get_num_equations()

        self.create_widgets()

    def get_num_equations(self):
        # Hiển thị cửa sổ nhập số lượng phương trình
        num_equations = simpledialog.askinteger("Số phương trình", "Nhập số phương trình:")
        return num_equations

    def create_widgets(self):
        # Tạo các đối tượng UI
        self.label_a = ttk.Label(self.root, text="Ma trận hệ số (A):")
        self.entries_a = [[ttk.Entry(self.root, width=5) for _ in range(self.num_equations)] for _ in range(self.num_equations)]
        self.label_b = ttk.Label(self.root, text="Vector kết quả (b):")
        self.entries_b = [ttk.Entry(self.root, width=5) for _ in range(self.num_equations)]
        self.solve_button = ttk.Button(self.root, text="Giải", command=self.solve_equation)
        self.result_label = ttk.Label(self.root, text="Nghiệm:")
        self.exit_button = ttk.Button(self.root, text="Thoát", command=self.root.destroy)

        # Đặt các đối tượng UI lên giao diện
        self.label_a.grid(row=0, column=0, pady=5)
        for i in range(self.num_equations):
            for j in range(self.num_equations):
                self.entries_a[i][j].grid(row=i, column=j+1, padx=2, pady=2)
        self.label_b.grid(row=self.num_equations, column=0, pady=5)
        for i in range(self.num_equations):
            self.entries_b[i].grid(row=self.num_equations, column=i+1, padx=2, pady=2)
        self.solve_button.grid(row=self.num_equations+1, column=0, columnspan=self.num_equations+1, pady=10)
        self.result_label.grid(row=self.num_equations+2, column=0, columnspan=self.num_equations+1, pady=5)
        self.exit_button.grid(row=self.num_equations+3, column=0, columnspan=self.num_equations+1,pady=10)
        # Tự động điều chỉnh kích thước cửa sổ
        self.root.update()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())

    def solve_equation(self):
        try:
            # Nhận giá trị từ các ô nhập liệu và chuyển đổi thành mảng NumPy
            A_input = [[float(entry.get()) for entry in row] for row in self.entries_a]
            b_input = [float(entry.get()) for entry in self.entries_b]

            # Chuyển đổi danh sách thành mảng NumPy
            A = np.array(A_input)
            b = np.array(b_input)

            # Kiểm tra kích thước ma trận
            if A.ndim != 2 or b.ndim != 1 or A.shape[0] != len(b):
                raise ValueError("Kích thước ma trận không phù hợp")

            # Giải hệ phương trình
            solution = np.linalg.solve(A, b)

            # Tạo chuỗi kết quả
            result_str = "Nghiệm:"
            for i, sol in enumerate(solution):
                result_str += f" x{i + 1} = {sol}"

            # Hiển thị kết quả
            self.result_label.config(text=result_str)
        except Exception as e:
            self.result_label.config(text=f"Lỗi: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LinearEquationSolverApp(root)
    root.mainloop()
