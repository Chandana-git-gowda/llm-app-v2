from flask import Flask, request, jsonify, render_template_string
from app.llm import ask_llm

# Create Flask web app
app = Flask(__name__)


# HTML page for the chatbot UI
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>LLM Chatbot v2</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 { color: #333; text-align: center; }
        form { display: flex; gap: 10px; margin: 20px 0; }
        input[type="text"] {
            flex: 1;
            padding: 12px;
            font-size: 16px;
            border: 2px solid #ddd;
            border-radius: 8px;
        }
        button {
            padding: 12px 24px;
            font-size: 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        button:hover { background-color: #45a049; }
        .answer {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #ddd;
            margin-top: 20px;
            white-space: pre-wrap;
        }
        .label { font-weight: bold; color: #555; }
    </style>
</head>
<body>
    <h1>LLM Chatbot v2</h1>
    <form method="POST" action="/">
        <input type="text" name="prompt" placeholder="Ask something..." required>
        <button type="submit">Ask</button>
    </form>
    {% if response %}
    <div class="answer">
        <span class="label">Response:</span><br><br>
        {{ response }}
    </div>
    {% endif %}
</body>
</html>
"""


# Home page - shows the chatbot UI
@app.route("/", methods=["GET", "POST"])
def home():
    response = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = ask_llm(prompt)
    return render_template_string(HTML_PAGE, response=response)


# API endpoint - for programs to use (not browser)
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("prompt", "")
    response = ask_llm(prompt)
    return jsonify({"response": response})


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
