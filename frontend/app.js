window.onload = () => {
    // URL of the backend API
    const apiUrl = "https://canary-project-backend.herokuapp.com/api/logs";  // Replace with your Flask API URL

    // Fetch logs from the backend and display them in the table
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById("logs-body");
            tableBody.innerHTML = "";  // Clear existing data

            data.forEach(log => {
                let row = `<tr>
                    <td>${log.email_id}</td>
                    <td>${log.public_ip}</td>
                    <td>${log.user_agent}</td>
                    <td>${log.access_time}</td>
                </tr>`;
                tableBody.innerHTML += row;
            });
        })
        .catch(error => console.error("Error fetching logs:", error));
}
