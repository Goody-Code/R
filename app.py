from flask import Flask, render_template, request, jsonify
import socket
import threading

app = Flask(__name__)

# قائمة لحفظ الرسائل
messages = []

# إعداد استقبال الرسائل عبر Socket باستخدام TCP
def syslog_listener():
    # عنوان IP والمنفذ للاستماع
    syslog_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    syslog_socket.bind(("0.0.0.0", 515))
    syslog_socket.listen(5)  # تفعيل الاستماع مع 5 اتصالات متزامنة

    while True:
        conn, addr = syslog_socket.accept()  # قبول الاتصال الجديد
        with conn:
            data = conn.recv(1024)
            if not data:
                continue
            message = data.decode('utf-8')
            messages.append({"ip": addr[0], "message": message, "time": request_date()})
            # حد الرسائل لعرض آخر 10000 رسالة فقط
            if len(messages) > 10000:
                messages.pop(0)

# استدعاء التاريخ الحالي
def request_date():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# تشغيل المستمع في Thread منفصل
threading.Thread(target=syslog_listener, daemon=True).start()

# عرض السجلات في واجهة الويب
@app.route('/')
def index():
    return render_template("index.html", messages=messages)

# لتحديث الرسائل بدون إعادة تحميل الصفحة
@app.route('/api/messages', methods=['GET'])
def api_messages():
    return jsonify(messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090, debug=True)
