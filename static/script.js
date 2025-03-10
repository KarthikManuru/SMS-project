document.getElementById("smsForm").addEventListener("submit", function (event) {
    event.preventDefault();

    let phone = document.getElementById("phone").value.trim();
    let message = document.getElementById("message").value.trim();

    if (!phone || !message) {
        alert("Phone number and message cannot be empty.");
        return;
    }

    fetch("http://127.0.0.1:5000/send-sms", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ phone: phone, message: message })
    })
    .then(async response => {
        if (!response.ok) {
            let errorData = await response.json();
            throw new Error(`HTTP error! Status: ${response.status} - ${errorData.error}`);
        }
        return response.json();
    })
    .then(data => {
        console.log("Response from Flask API:", data);
        alert("✅ SMS Sent Successfully!");
    })
    .catch(error => {
        console.error("Error:", error);
        alert(`Failed to send SMS. Error: ${error.message}`);
    });
});
