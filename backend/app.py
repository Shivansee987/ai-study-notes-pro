from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route("/summarize", methods=["POST"])
def summarize_text():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    text = file.read().decode("utf-8", errors="ignore")

    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    
    return jsonify({"summary": summary[0]['summary_text']})

if __name__ == "__main__":
    app.run(debug=True)
