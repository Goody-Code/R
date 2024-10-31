import os

# السماح للبرنامج عبر جدار الحماية (قد تحتاج إلى تشغيل الكود كمسؤول)
def allow_program_in_firewall(program_path):
    command = f'netsh advfirewall firewall add rule name="app.py" dir=in action=allow program="{program_path}" enable=yes'
    os.system(command)

# استدعاء الدالة وتمرير مسار البرنامج
allow_program_in_firewall("C:\Users\KHALED\Documents\cmder\R\app.py")
