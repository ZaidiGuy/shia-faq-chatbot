from flask import Flask, request, jsonify, send_file
from openai import OpenAI
import os
from dotenv import load_dotenv
import sys

load_dotenv()  # Load environment variables from .env file

# Validate required environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("ERROR: OPENAI_API_KEY environment variable is not set!")
    print("Please set your OpenAI API key in a .env file or environment variable.")
    sys.exit(1)

# Initialize OpenAI client with the new API format
client = OpenAI(api_key=api_key)

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_question = data.get("question", "")

    if not user_question:
        return jsonify({"error": "No question provided."}), 400

    try:
        # Use the new OpenAI client format
        response = client.chat.completions.create(
            model="gpt-4",  # You can change to "gpt-3.5-turbo" if needed
            messages=[
                {
                    "role": "system",
                    "content": "You are an Islamic FAQ assistant for a Shia Muslim community. Always answer according to Ja'fari Fiqh. If unsure, advise the user to consult a qualified scholar."
                },
                {"role": "user", "content": user_question}
            ]
        )

        answer = response.choices[0].message.content.strip()
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/faq-sample", methods=["GET"])
def sample_faq():
    return jsonify({
        "faq": [
            {
                "question": "When does Muharram start?",
                "answer": "Muharram begins with the sighting of the new moon. Dates may vary by location."
            },
            {
                "question": "What is Ziyarat Ashura?",
                "answer": "Ziyarat Ashura is a recommended supplication recited to remember the martyrdom of Imam Hussain (a.s)."
            },
            {
                "question": "Can I combine Zuhr and Asr prayers while traveling?",
                "answer": "Yes, according to Ja'fari Fiqh, it is permissible to combine prayers while traveling."
            },
            {
                "question": "What is the ruling on temporary marriage (Mut'ah)?",
                "answer": "Mut'ah (temporary marriage) is permissible in Ja'fari jurisprudence under certain conditions."
            },
            {
                "question": "Why do Shia Muslims commemorate Arbaeen?",
                "answer": "Arbaeen marks the 40th day after the martyrdom of Imam Hussain (a.s) and is observed to honor his sacrifice."
            }
        ]
    })

@app.route("/")
def home():
    return send_file("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
