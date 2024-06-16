import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import queue
import os
import webbrowser

# Antrian untuk setiap loket
loket_1_queue = queue.Queue()
loket_2_queue = queue.Queue()
loket_3_queue = queue.Queue()
loket_4_queue = queue.Queue()
loket_5_queue = queue.Queue()

# Variabel global untuk melacak nomor tiket terakhir
last_ticket_number_1 = 0
last_ticket_number_2 = 0
last_ticket_number_3 = 0
last_ticket_number_4 = 0
last_ticket_number_5 = 0

# Path untuk file penyimpanan jumlah kali program dijalankan
count_file_path = 'run_count.txt'
max_runs = 10

# Fungsi untuk membaca jumlah kali program dijalankan dari file
def read_run_count():
    if os.path.exists(count_file_path):
        with open(count_file_path, 'r') as file:
            return int(file.read())
    return 0

# Fungsi untuk menulis jumlah kali program dijalankan ke file
def write_run_count(count):
    with open(count_file_path, 'w') as file:
        file.write(str(count))

# Fungsi untuk mengecek apakah program sudah diaktivasi
def check_activation():
    run_count = read_run_count()
    if run_count >= max_runs:
        messagebox.showwarning("Warning", "Program belum diaktivasi. Anda hanya dapat membuka program ini sebanyak 10 kali.")
        root.destroy()
    else:
        run_count += 1
        write_run_count(run_count)

def add_ticket(loket, ticket):
    if loket == 1:
        loket_1_queue.put(ticket)
        update_loket_display(1)
    elif loket == 2:
        loket_2_queue.put(ticket)
        update_loket_display(2)
    elif loket == 3:
        loket_3_queue.put(ticket)
        update_loket_display(3)
    elif loket == 4:
        loket_4_queue.put(ticket)
        update_loket_display(4)
    elif loket == 5:
        loket_5_queue.put(ticket)
        update_loket_display(5)

def update_loket_display(loket):
    if loket == 1:
        if not loket_1_queue.empty():
            current_ticket = loket_1_queue.queue[0]
            loket_1_display_var.set(current_ticket)
        else:
            loket_1_display_var.set("")
    elif loket == 2:
        if not loket_2_queue.empty():
            current_ticket = loket_2_queue.queue[0]
            loket_2_display_var.set(current_ticket)
        else:
            loket_2_display_var.set("")
    elif loket == 3:
        if not loket_3_queue.empty():
            current_ticket = loket_3_queue.queue[0]
            loket_3_display_var.set(current_ticket)
        else:
            loket_3_display_var.set("")
    elif loket == 4:
        if not loket_4_queue.empty():
            current_ticket = loket_4_queue.queue[0]
            loket_4_display_var.set(current_ticket)
        else:
            loket_4_display_var.set("")
    elif loket == 5:
        if not loket_5_queue.empty():
            current_ticket = loket_5_queue.queue[0]
            loket_5_display_var.set(current_ticket)
        else:
            loket_5_display_var.set("")

def generate_ticket(loket):
    global last_ticket_number_1, last_ticket_number_2, last_ticket_number_3, last_ticket_number_4, last_ticket_number_5
    if loket == 1:
        last_ticket_number_1 += 1
        ticket = f"A{last_ticket_number_1} Loket 1"
        add_ticket(1, ticket)
    elif loket == 2:
        last_ticket_number_2 += 1
        ticket = f"B{last_ticket_number_2} Loket 2"
        add_ticket(2, ticket)
    elif loket == 3:
        last_ticket_number_3 += 1
        ticket = f"C{last_ticket_number_3} Loket 3"
        add_ticket(3, ticket)
    elif loket == 4:
        last_ticket_number_4 += 1
        ticket = f"D{last_ticket_number_4} Loket 4"
        add_ticket(4, ticket)
    elif loket == 5:
        last_ticket_number_5 += 1
        ticket = f"E{last_ticket_number_5} Loket 5"
        add_ticket(5, ticket)

def print_ticket(loket):
    if loket == 1:
        if not loket_1_queue.empty():
            ticket = loket_1_queue.get()
            messagebox.showinfo("Cetak Tiket", f"Ticket '{ticket}' dicetak.")
            update_loket_display(1)
        else:
            messagebox.showwarning("Cetak Tiket", "Antrian kosong, tidak ada tiket untuk dicetak.")
    elif loket == 2:
        if not loket_2_queue.empty():
            ticket = loket_2_queue.get()
            messagebox.showinfo("Cetak Tiket", f"Ticket '{ticket}' dicetak.")
            update_loket_display(2)
        else:
            messagebox.showwarning("Cetak Tiket", "Antrian kosong, tidak ada tiket untuk dicetak.")
    elif loket == 3:
        if not loket_3_queue.empty():
            ticket = loket_3_queue.get()
            messagebox.showinfo("Cetak Tiket", f"Ticket '{ticket}' dicetak.")
            update_loket_display(3)
        else:
            messagebox.showwarning("Cetak Tiket", "Antrian kosong, tidak ada tiket untuk dicetak.")
    elif loket == 4:
        if not loket_4_queue.empty():
            ticket = loket_4_queue.get()
            messagebox.showinfo("Cetak Tiket", f"Ticket '{ticket}' dicetak.")
            update_loket_display(4)
        else:
            messagebox.showwarning("Cetak Tiket", "Antrian kosong, tidak ada tiket untuk dicetak.")
    elif loket == 5:
        if not loket_5_queue.empty():
            ticket = loket_5_queue.get()
            messagebox.showinfo("Cetak Tiket", f"Ticket '{ticket}' dicetak.")
            update_loket_display(5)
        else:
            messagebox.showwarning("Cetak Tiket", "Antrian kosong, tidak ada tiket untuk dicetak.")

def activate_license():
    license_code = simpledialog.askstring("Activate", "Masukkan kode lisensi:")
    if license_code == " ":
        messagebox.showinfo("Activation", "Lisensi berhasil diaktifkan!")
        write_run_count(0)  # Reset jumlah kali program dijalankan setelah aktivasi
    else:
        messagebox.showerror("Activation", "Kode lisensi salah!")

def show_about():
    messagebox.showinfo("About", "Sistem Antrian v1.0\nBelilah lisensi agar program berjalan dengan baik\nbeli lisensi hanya di\nYogiApp: +62 813-5811-3087")

def exit_and_open_website():
    webbrowser.open("https://userutgc.github.io/yogiariohomeconnection/")  # Ganti URL dengan website Anda
    root.quit()

root = tk.Tk()
root.title("SIAT - 1.0")

# Cek aktivasi saat program dimulai
check_activation()

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Simpan")
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Undo", command=lambda: messagebox.showinfo("Info", ":)"))
edit_menu.add_command(label="Cut", command=lambda: messagebox.showinfo("Info", "Terpotong :("))
edit_menu.add_command(label="Copy", command=lambda: messagebox.showinfo("Info", "Tersalin"))
menubar.add_cascade(label="Edit", menu=edit_menu)

view_menu = tk.Menu(menubar, tearoff=0)
view_menu.add_command(label="Minimize", command=lambda: root.iconify())
view_menu.add_command(label="Maximize", command=lambda: root.state('zoomed'))
view_menu.add_command(label="Close", command=root.quit)
menubar.add_cascade(label="View", menu=view_menu)

registration_menu = tk.Menu(menubar, tearoff=0)
registration_menu.add_command(label="Activate", command=activate_license)
registration_menu.add_command(label="About", command=show_about)
menubar.add_cascade(label="Registrasi", menu=registration_menu)

root.config(menu=menubar)

header = tk.Label(root, text="SISTEM ANTRIAN", font=("Arial", 24))
header.pack(pady=10)

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

footer = tk.Label(root, text="SIAT - SISTEM ANTRIAN TIKET", font=("Arial", 10))
footer.pack(pady=5)

button_exit = tk.Button(root, text="Keluar", command=exit_and_open_website)
button_exit.pack(pady=5)

root.mainloop()
