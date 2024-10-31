from flask import Flask, render_template, jsonify
import threading
import syslog_server

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs')
def get_logs():
    # إرجاع السجلات بصيغة JSON
    return jsonify(syslog_server.logs[-100:])  # إرجاع آخر 100 رسالة فقط

def run_syslog_server():
    syslog_server.start_syslog_server()

if __name__ == '__main__':
    # تشغيل خادم Syslog في سلسلة منفصلة
    syslog_thread = threading.Thread(target=run_syslog_server)
    syslog_thread.daemon = True
    syslog_thread.start()

    # تشغيل تطبيق Flask
    app.run(host='0.0.0.0', port=8080, debug=True)
