from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # ✅ Import Flask-CORS
import requests

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS for all routes

SMS_GATEWAY_URL = "http://192.0.0.4:8082/sendsms"
API_KEY = "317db0ea-3b12-4816-8aae-19da60239cab"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send-sms", methods=["POST"])
def send_sms():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON format"}), 400
        
        phone_number = data.get("phone")
        message = data.get("message")

        if not phone_number or not message:
            return jsonify({"error": "Phone number and message are required"}), 400

        headers = {
            "Authorization": f"{API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(SMS_GATEWAY_URL, json={
            "to": phone_number,
            "message": message
        }, headers=headers, timeout=5)

        # ✅ Print Debugging Info
        print("📡 SMS Gateway Response:", response.status_code, response.text)

        if response.status_code == 200:
            return jsonify({"success": True, "message": "SMS sent successfully!"})
        else:
            return jsonify({"error": "Failed to send SMS", "details": response.text}), response.status_code

    except Exception as e:
        print("❌ Error:", str(e))  # ✅ Print the error in Flask terminal
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
