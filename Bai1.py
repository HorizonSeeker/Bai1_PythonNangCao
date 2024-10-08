import tkinter as tk
from tkinter import messagebox
from googletrans import Translator

# Khởi tạo bộ dịch
translator = Translator()

# Hàm dịch từ tiếng Việt sang tiếng Anh
def translate_text():
    text_to_translate = input_text.get("1.0", tk.END).strip()  # Lấy nội dung từ ô nhập
    if text_to_translate:
        try:
            translation = translator.translate(text_to_translate, src='vi', dest='en')
            output_text.delete("1.0", tk.END)  # Xóa văn bản cũ
            output_text.insert(tk.END, translation.text)  # Hiển thị bản dịch
        except Exception as e:
            messagebox.showerror("Translation Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Vui lòng nhập văn bản cần dịch.")

# Hàm xóa văn bản trong cả hai ô nhập và xuất
def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# Thiết lập giao diện Tkinter
root = tk.Tk()
root.title("Vietnamese to English Translator")

# Nhãn cho phần nhập văn bản tiếng Việt
tk.Label(root, text="Văn bản Tiếng Việt:").grid(row=0, column=0)

# Ô nhập văn bản Tiếng Việt
input_text = tk.Text(root, height=10, width=50)
input_text.grid(row=1, column=0, padx=10, pady=10)

# Nhãn cho phần hiển thị văn bản dịch
tk.Label(root, text="Dịch sang Tiếng Anh:").grid(row=0, column=1)

# Ô hiển thị văn bản dịch sang Tiếng Anh
output_text = tk.Text(root, height=10, width=50)
output_text.grid(row=1, column=1, padx=10, pady=10)

# Nút để thực hiện dịch văn bản
btn_translate = tk.Button(root, text="Dịch", command=translate_text, height=2, width=15, bg="lightgreen")
btn_translate.grid(row=2, column=0, padx=10, pady=10)

# Nút để xóa nội dung cả hai ô
btn_clear = tk.Button(root, text="Xóa", command=clear_text, height=2, width=15, bg="lightcoral")
btn_clear.grid(row=2, column=1, padx=10, pady=10)

# Chạy giao diện
root.mainloop()