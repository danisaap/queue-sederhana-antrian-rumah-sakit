import tkinter as tk
from tkinter import messagebox
import heapq

class rumahsakit:
    def __init__(self, root):
        self.root = root
        self.root.title("Antrian Rumah Sakit")
        self.root.configure(bg="#D5E4F9")

        self.queue = []
        self.counter = 0  # Counter untuk melacak waktu input pasien
        
        # Frame untuk Input Pasien
        self.frame_input = tk.Frame(root, bg="#D5E4F9")
        self.frame_input.pack(pady=10)
        
        tk.Label(self.frame_input, text="Nama Pasien :", font='Arial 10', bg="#D5E4F9").grid(row=0, column=0, padx=10, pady=10)
        self.entry_name = tk.Entry(self.frame_input, font='Arial 10')
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.frame_input, text="Prioritas :", font='Arial 10', bg="#D5E4F9").grid(row=1, column=0, padx=10, pady=10)
        
        # Option Menu untuk memilih prioritas
        self.priority_var = tk.StringVar()
        self.priority_var.set("Umum")  # nilai default
        self.option_menu = tk.OptionMenu(self.frame_input, self.priority_var, "Kritis", "Serius", "Ringan", "Umum")
        self.option_menu.grid(row=1, column=1, padx=10, pady=10)
        
        self.button_add = tk.Button(self.frame_input, text="Tambah ke Antrian", command=self.add_patient, font='Arial 10')
        self.button_add.grid(row=2, column=1, pady=10)
        
        # Frame untuk Pencarian Pasien
        self.frame_search = tk.Frame(root, bg="#A9CCE2")
        self.frame_search.pack(pady=10)
        
        tk.Label(self.frame_search, text="Cari Pasien: ", font='Arial 10', bg="#A9CCE2").grid(row=0, column=0, padx=10, pady=10)
        self.entry_search = tk.Entry(self.frame_search, font='Arial 10')
        self.entry_search.grid(row=0, column=1, padx=10, pady=10)
        
        self.button_search = tk.Button(self.frame_search, text="Cari", command=self.search_patient, font='Arial 10')
        self.button_search.grid(row=0, column=2, padx=10, pady=10)
        
        # Frame untuk Daftar Antrian
        self.frame_queue = tk.Frame(root, bg="#A9CCE2")
        self.frame_queue.pack(pady=10)
        
        self.label_queue = tk.Label(self.frame_queue, text="Daftar Antrian:", font='Arial 10', bg="#A9CCE2")
        self.label_queue.pack()
        
        self.listbox_queue = tk.Listbox(self.frame_queue, width=50, font='Arial 10')
        self.listbox_queue.pack()

        # Warna untuk setiap prioritas
        self.priority_colors = {
            1: '#CD0027',    # Kritis
            2: '#FFE001', # Serius
            3: '#89B524', # Ringan
            4: '#FFFFFF'   # Umum
        }
        
        self.button_next = tk.Button(root, text="Panggil Pasien Selanjutnya", command=self.call_next_patient, font='Arial 10')
        self.button_next.pack(pady=10)
        
    def add_patient(self):
        patient_name = self.entry_name.get().title()
        priority = self.priority_var.get()
        
        priority_map = {"Kritis": 1, "Serius": 2, "Ringan": 3, "Umum": 4}
        if patient_name and priority in priority_map:
            for i, (p, c, name) in enumerate(self.queue):
                if name == patient_name:
                    if p == priority_map[priority]:
                        messagebox.showwarning("Peringatan", "Pasien dengan nama dan prioritas yang sama sudah ada dalam antrian!")
                        return
                    else:
                        if messagebox.askyesno("Konfirmasi", f"Pasien dengan nama {patient_name} sudah ada dalam antrian dengan prioritas berbeda. Apakah Anda ingin mengubah prioritasnya menjadi {priority}?"):
                            self.queue[i] = (priority_map[priority], c, patient_name)
                            heapq.heapify(self.queue)
                            self.update_queue_listbox()
                        return

            self.counter += 1  # Meningkatkan counter setiap kali pasien ditambahkan
            heapq.heappush(self.queue, (priority_map[priority], self.counter, patient_name))
            self.update_queue_listbox()
            self.entry_name.delete(0, tk.END)
            self.priority_var.set("Umum")
        else:
            messagebox.showwarning("Peringatan", "Nama pasien tidak boleh kosong!")
    
    def update_queue_listbox(self):
        self.listbox_queue.delete(0, tk.END)
        for index, (priority, _, patient) in enumerate(sorted(self.queue), start=1):
            priority_str = {1: "Kritis", 2: "Serius", 3: "Ringan", 4: "Umum"}[priority]
            self.listbox_queue.insert(tk.END, f"{index}. {patient} (Prioritas: {priority_str})")
            self.listbox_queue.itemconfig(tk.END, {'bg': self.priority_colors[priority]})
    
    def call_next_patient(self):
        if self.queue:
            next_patient = heapq.heappop(self.queue)[2]
            messagebox.showinfo("Panggilan Pasien", f"Panggil pasien: {next_patient}")
            self.update_queue_listbox()
        else:
            messagebox.showinfo("Informasi", "Tidak ada pasien dalam antrian.")
    
    def search_patient(self):
        search_name = self.entry_search.get().strip().title()
        if not search_name:
            messagebox.showwarning("Peringatan", "Nama pasien tidak boleh kosong!")
            return
        
        # Linear search dalam queue
        results = [(priority, patient) for priority, _, patient in self.queue if search_name in patient]
        
        if results:
            result_str = "\n".join([f"{patient} (Prioritas: {priority})" for priority, patient in results])
            messagebox.showinfo("Hasil Pencarian", result_str)
        else:
            messagebox.showinfo("Hasil Pencarian", "Pasien tidak ditemukan dalam antrian.")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = rumahsakit(root)
    root.mainloop()
