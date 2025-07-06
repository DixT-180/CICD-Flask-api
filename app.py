from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return "Titanic Data Quality API is running"

@app.route('/check', methods=['POST'])
def check_data():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    try:
        df = pd.read_csv(file)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    report = {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum())
    }
    print(report)
    return jsonify(report)


if __name__ == '__main__': 
    app.run(host="0.0.0.0", port=5000)   #make the container acessible from outside the docker.
# Tells Flask to listen on all available network interfaces, not just localhost(its internal host)