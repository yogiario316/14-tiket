import tkinter as tk
from tkinter import messagebox
import queue

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

def add_ticket(loket, ticket):
    # Menambahkan tiket ke antrian yang sesuai dan memperbarui tampilan loket
    if loket == 1:
        loket_1_queue.put(ticket)
        update_loket_display(1)
        print(f"Ticket '{ticket}' telah ditambahkan ke Loket 1.")
    elif loket == 2:
        loket_2_queue.put(ticket)
        update_loket_display(2)
        print(f"Ticket '{ticket}' telah ditambahkan ke Loket 2.")
    elif loket == 3:
        loket_3_queue.put(ticket)
        update_loket_display(3)
        print(f"Ticket '{ticket}' telah ditambahkan ke Loket 3.")
    elif loket == 4:
        loket_4_queue.put(ticket)
        update_loket_display(4)
        print(f"Ticket '{ticket}' telah ditambahkan ke Loket 4.")
    elif loket == 5:
        loket_5_queue.put(ticket)
        update_loket_display(5)
        print(f"Ticket '{ticket}' telah ditambahkan ke Loket 5.")

def update_loket_display(loket):
    # Memperbarui tampilan tiket di loket dengan tiket pertama dalam antrian
    if loket == 1:
        if not loket_1_queue.empty():
            current_ticket = loket_1_queue.queue[0]  # Menampilkan tiket pertama
            loket_1_display_var.set(current_ticket)
        else:
            loket_1_display_var.set("")
    elif loket == 2:
        if not loket_2_queue.empty():
            current_ticket = loket_2_queue.queue[0]  # Menampilkan tiket pertama
            loket_2_display_var.set(current_ticket)
        else:
            loket_2_display_var.set("")
    elif loket == 3:
        if not loket_3_queue.empty():
            current_ticket = loket_3_queue.queue[0]  # Menampilkan tiket pertama
            loket_3_display_var.set(current_ticket)
        else:
            loket_3_display_var.set("")
    elif loket == 4:
        if not loket_4_queue.empty():
            current_ticket = loket_4_queue.queue[0]  # Menampilkan tiket pertama
            loket_4_display_var.set(current_ticket)
        else:
            loket_4_display_var.set("")
    elif loket == 5:
        if not loket_5_queue.empty():
            current_ticket = loket_5_queue.queue[0]  # Menampilkan tiket pertama
            loket_5_display_var.set(current_ticket)
        else:
            loket_5_display_var.set("")

def generate_ticket(loket):
    # Menghasilkan tiket baru dan menambahkannya ke antrian yang sesuai
    global last_ticket_number_1, last_ticket_number_2, last_ticket_number_3, last_ticket_number_4, last_ticket_number_5  # Menggunakan variabel global
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
    # Mencetak tiket pertama dalam antrian dan memperbarui tampilan
    if loket == 1:
        if not loket_1_queue.empty():
            ticket = loket_1_queue.get()  # Mengeluarkan tiket pertama dari antrian
            messagebox.showinfo("Cetak Tiket", f"Ticket '{ticket}' dicetak.")
            update_loket_display(1)
        else:
            messagebox.showwarning("Cetak Tiket", "Antrian kosong, tidak ada tiket untuk dicetak.")
    elif loket == 2:
        if not loket_2_queue.empty():
            ticket = loket_2_queue.get()  # Mengeluarkan tiket pertama dari antrian
            messagebox.showinfo("Cetak Tiket", f"Ticket '{ticket}' dicetak.")
            update_loket_display(2)
        else:
            messagebox.showwarning("Cetak Tiket", "Antrian kosong, tidak ada tiket untuk dicetak.")
    elif loket == 3:
        if not loket_3_queue.empty():
            ticket = loket_3_queue.get()  # Mengeluarkan tiket pertama dari antrian
            messagebox.showinfo("Cetak Tiket", f"Ticket '{ticket}' dicetak.")
            update_loket_display(3)
        else:
            messagebox.showwarning("Cetak Tiket", "Antrian kosong, tidak ada tiket untuk dicetak.")
    elif loket == 4:
        if not loket_4_queue.empty():
            ticket = loket_4_queue.get()  # Mengeluarkan tiket pertama dari antrian
            messagebox.showinfo("Cetak Tiket", f"Ticket '{ticket}' dicetak.")
            update_loket_display(4)
        else:
            messagebox.showwarning("Cetak Tiket", "Antrian kosong, tidak ada tiket untuk dicetak.")
    elif loket == 5:
        if not loket_5_queue.empty():
            ticket = loket_5_queue.get()  # Mengeluarkan tiket pertama dari antrian
            messagebox.showinfo("Cetak Tiket", f"Ticket '{ticket}' dicetak.")
            update_loket_display(5)
        else:
            messagebox.showwarning("Cetak Tiket", "Antrian kosong, tidak ada tiket untuk dicetak.")

# Fungsi untuk keluar dari aplikasi
def exit_app():
    root.quit()

# Fungsi untuk menampilkan informasi tentang program
def about_program():
    messagebox.showinfo("Tentang Program", 
                        "Program ini terdaftar untuk:\n"
                        "Klinik Mitra Usaha Persada\n"
                        "Untuk membeli lisensi silahkan hubungi kami di whatsapp:\n"
                        "YogiApp : 081358113087")

# Membuat jendela utama
root = tk.Tk()
root.title("SISTEM ANTRIAN - KLINIK MITRA USAHA PERSADA")

# Menambahkan menu bar
menubar = tk.Menu(root)

# Menu File
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Simpan", command=lambda: messagebox.showinfo("Info", "Fungsi Simpan belum diimplementasikan."))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)

# Menu Edit
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Undo", command=lambda: messagebox.showinfo("Info", "Fungsi Undo belum diimplementasikan."))
edit_menu.add_command(label="Cut", command=lambda: messagebox.showinfo("Info", "Fungsi Cut belum diimplementasikan."))
edit_menu.add_command(label="Copy", command=lambda: messagebox.showinfo("Info", "Fungsi Copy belum diimplementasikan."))
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
menubar.add_cascade(label="Registrasi", menu=registrasi_menu)

root.config(menu=menubar)

# Header
header_frame = tk.Frame(root)
header_frame.pack(pady=10)

header_label = tk.Label(header_frame, text="SISTEM ANTRIAN\nKLINIK MITRA USAHA PERSADA", font=("Helvetica", 16, "bold"))
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
label_app_name = tk.Label(root, text="KLINIK MITRA USAHA PERSADA", font=("Helvetica", 10))
label_app_name.pack(pady=5)

# Tombol keluar
button_exit = tk.Button(root, text="Keluar", command=exit_app)
button_exit.pack(pady=10)

# Memulai loop utama aplikasi
root.mainloop()
