import tkinter as tk
from tkinter import messagebox, simpledialog
import queue
import os
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    try:
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:])
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        sys.exit()
    except Exception as e:
        print(f"Kesalahan: {e}")
        sys.exit()


# Path to the file that will store the usage count and license key
USAGE_FILE = "usage_count.txt"
LICENSE_KEY_FILE = "license_key.txt"
LICENSE_KEY = "userutgc"  # Replace with your actual license key
MAX_USAGE = 10

# Read usage count from file
def read_usage_count():
    if os.path.exists(USAGE_FILE):
        with open(USAGE_FILE, 'r') as file:
            return int(file.read().strip())
    return 0

# Write usage count to file
def write_usage_count(count):
    with open(USAGE_FILE, 'w') as file:
        file.write(str(count))

# Read license key from file
def read_license_key():
    if os.path.exists(LICENSE_KEY_FILE):
        with open(LICENSE_KEY_FILE, 'r') as file:
            return file.read().strip()
    return ""

# Write license key to file
def write_license_key(key):
    with open(LICENSE_KEY_FILE, 'w') as file:
        file.write(key)

# Check if the license key is valid
def is_license_valid():
    license_key = read_license_key()
    return license_key == LICENSE_KEY

# Prompt user to enter license key
def prompt_license_key():
    license_key = simpledialog.askstring("Masukkan Kode Lisensi", "Masukkan kode lisensi Anda:")
    if license_key:
        if license_key == LICENSE_KEY:
            write_license_key(license_key)
            messagebox.showinfo("Lisensi Diterima", "Kode lisensi valid. Terima kasih telah mendaftar.")
        else:
            messagebox.showwarning("Lisensi Tidak Valid", "Kode lisensi tidak valid. Silakan coba lagi.")

# Increase usage count and check for license validation
def increase_usage_count():
    if is_license_valid():
        return
    usage_count = read_usage_count() + 1
    write_usage_count(usage_count)
    if usage_count >= MAX_USAGE:
        messagebox.showwarning("Batas Penggunaan Tercapai", "Anda telah mencapai batas penggunaan. Silakan masukkan kode lisensi.")
        prompt_license_key()

# Initializing usage count
increase_usage_count()

# Fungsi untuk keluar dari aplikasi
def exit_app():
    root.quit()

# The rest of your code...
# ...

# Modifying the about_program function
def about_program():
    messagebox.showinfo("Tentang Program", 
                        "Program ini terdaftar untuk:\n"
                        "-\n"
                        "Untuk membeli lisensi silahkan hubungi kami di whatsapp:\n"
                        "YogiApp : 081358113087")

# Fungsi untuk menampilkan dialog masukkan kode lisensi
def masukkan_kode_lisensi():
    prompt_license_key()

# Membuat jendela utama
root = tk.Tk()
root.title("SISTEM ANTRIAN")

# Menambahkan menu bar
menubar = tk.Menu(root)

# Menu File
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Simpan", command=lambda: messagebox.showinfo("Info", "Tersimpan dengan baik :)"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)

# Menu Edit
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Undo", command=lambda: messagebox.showinfo("Info", ":)"))
edit_menu.add_command(label="Cut", command=lambda: messagebox.showinfo("Info", "Terpotong :("))
edit_menu.add_command(label="Copy", command=lambda: messagebox.showinfo("Info", "Tiket Tersalin"))
menubar.add_cascade(label="Edit", menu=edit_menu)

# Menu View
view_menu = tk.Menu(menubar, tearoff=0)
view_menu.add_command(label="Minimize", command=root.iconify)
view_menu.add_command(label="Maximize", command=lambda: root.state('zoomed'))
view_menu.add_command(label="Close", command=exit_app)
menubar.add_cascade(label="View", menu=view_menu)

# Menu Registrasi
registrasi_menu = tk.Menu(menubar, tearoff=0)
registrasi_menu.add_command(label="Tentang Program", command=about_program)
registrasi_menu.add_command(label="Masukkan Kode Lisensi", command=masukkan_kode_lisensi)
menubar.add_cascade(label="Registrasi", menu=registrasi_menu)

root.config(menu=menubar)

# Header
header_frame = tk.Frame(root)
header_frame.pack(pady=10)

header_label = tk.Label(header_frame, text="SISTEM ANTRIAN\n", font=("Helvetica", 16, "bold"))
header_label.pack()

# Variabel untuk menampilkan tiket di setiap loket
loket_1_display_var = tk.StringVar()
loket_1_display_var.set("")

loket_2_display_var = tk.StringVar()
loket_2_display_var.set("")

loket_3_display_var = tk.StringVar()
loket_3_display_var.set("")

loket_4_display_var = tk.StringVar()
loket_4_display_var.set("")

loket_5_display_var = tk.StringVar()
loket_5_display_var.set("")

# Frame untuk Loket 1
frame_loket_1 = tk.Frame(root)
frame_loket_1.pack(padx=10, pady=10)

label_loket_1 = tk.Label(frame_loket_1, text="Loket 1:")
label_loket_1.pack(side=tk.LEFT)

entry_loket_1 = tk.Entry(frame_loket_1, textvariable=loket_1_display_var, state='readonly', width=20)
entry_loket_1.pack(side=tk.LEFT, padx=5)

button_generate_1 = tk.Button(frame_loket_1, text="Cetak", command=lambda: generate_ticket(1))
button_generate_1.pack(side=tk.LEFT, padx=5)

button_print_1 = tk.Button(frame_loket_1, text="Print", command=lambda: print_ticket(1))
button_print_1.pack(side=tk.LEFT, padx=5)

# Frame untuk Loket 2
frame_loket_2 = tk.Frame(root)
frame_loket_2.pack(padx=10, pady=10)

label_loket_2 = tk.Label(frame_loket_2, text="Loket 2:")
label_loket_2.pack(side=tk.LEFT)

entry_loket_2 = tk.Entry(frame_loket_2, textvariable=loket_2_display_var, state='readonly', width=20)
entry_loket_2.pack(side=tk.LEFT, padx=5)

button_generate_2 = tk.Button(frame_loket_2, text="Cetak", command=lambda: generate_ticket(2))
button_generate_2.pack(side=tk.LEFT, padx=5)

button_print_2 = tk.Button(frame_loket_2, text="Print", command=lambda: print_ticket(2))
button_print_2.pack(side=tk.LEFT, padx=5)

# Frame untuk Loket 3
frame_loket_3 = tk.Frame(root)
frame_loket_3.pack(padx=10, pady=10)

label_loket_3 = tk.Label(frame_loket_3, text="Loket 3:")
label_loket_3.pack(side=tk.LEFT)

entry_loket_3 = tk.Entry(frame_loket_3, textvariable=loket_3_display_var, state='readonly', width=20)
entry_loket_3.pack(side=tk.LEFT, padx=5)

button_generate_3 = tk.Button(frame_loket_3, text="Cetak", command=lambda: generate_ticket(3))
button_generate_3.pack(side=tk.LEFT, padx=5)

button_print_3 = tk.Button(frame_loket_3, text="Print", command=lambda: print_ticket(3))
button_print_3.pack(side=tk.LEFT, padx=5)

# Frame untuk Loket 4
frame_loket_4 = tk.Frame(root)
frame_loket_4.pack(padx=10, pady=10)

label_loket_4 = tk.Label(frame_loket_4, text="Loket 4:")
label_loket_4.pack(side=tk.LEFT)

entry_loket_4 = tk.Entry(frame_loket_4, textvariable=loket_4_display_var, state='readonly', width=20)
entry_loket_4.pack(side=tk.LEFT, padx=5)

button_generate_4 = tk.Button(frame_loket_4, text="Cetak", command=lambda: generate_ticket(4))
button_generate_4.pack(side=tk.LEFT, padx=5)

button_print_4 = tk.Button(frame_loket_4, text="Print", command=lambda: print_ticket(4))
button_print_4.pack(side=tk.LEFT, padx=5)

# Frame untuk Loket 5
frame_loket_5 = tk.Frame(root)
frame_loket_5.pack(padx=10, pady=10)

label_loket_5 = tk.Label(frame_loket_5, text="Loket 5:")
label_loket_5.pack(side=tk.LEFT)

entry_loket_5 = tk.Entry(frame_loket_5, textvariable=loket_5_display_var, state='readonly', width=20)
entry_loket_5.pack(side=tk.LEFT, padx=5)

button_generate_5 = tk.Button(frame_loket_5, text="Cetak", command=lambda: generate_ticket(5))
button_generate_5.pack(side=tk.LEFT, padx=5)

button_print_5 = tk.Button(frame_loket_5, text="Print", command=lambda: print_ticket(5))
button_print_5.pack(side=tk.LEFT, padx=5)

# Menambahkan nama aplikasi dan kredit
label_app_name = tk.Label(root, text="SISTEM ANTRIAN", font=("Helvetica", 16, "bold"))
label_app_name.pack(pady=5)
label_app_name = tk.Label(root, text=" ", font=("Helvetica", 10))
label_app_name.pack(pady=5)

# Tombol keluar
button_exit = tk.Button(root, text="Keluar", command=exit_app)
button_exit.pack(pady=10)

# Memulai loop utama aplikasi
root.mainloop()
