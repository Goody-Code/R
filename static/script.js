function fetchLogs() {
    fetch('/logs')
        .then(response => response.json())
        .then(data => {
            const tbody = document.querySelector("#syslog-table tbody");
            tbody.innerHTML = '';  // تفريغ الجدول

            data.forEach(log => {
                const row = document.createElement('tr');
                const timeCell = document.createElement('td');
                const messageCell = document.createElement('td');

                timeCell.textContent = new Date().toLocaleTimeString();
                messageCell.textContent = log;

                row.appendChild(timeCell);
                row.appendChild(messageCell);
                tbody.appendChild(row);
            });
        });
}

// تحديث السجلات كل 5 ثوانٍ
setInterval(fetchLogs, 5000);
