from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
DB_FILE = "data.json"

def load_data():
    if not os.path.exists(DB_FILE): return {}
    with open(DB_FILE, "r", encoding="utf-8") as f:
        try: return json.load(f)
        except: return {}

def save_to_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.route("/")
def home():
    data = load_data()
    return render_template("one.html", titles=list(data.keys()))

# --- 這裡加上 path: 解決日期斜線導致 404 的問題 ---
@app.route("/get_content/<path:title>")
def get_content(title):
    data = load_data()
    print(f"正在讀取標題: {title}") # 除錯用
    return jsonify({"content": data.get(title, "")})

@app.route("/save_all", methods=["POST"])
def save_all():
    req = request.get_json()
    title = req.get("title")
    content = req.get("content", "")
    if title:
        data = load_data()
        data[title] = content
        save_to_db(data)
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 400

@app.route("/delete_title", methods=["POST"])
def delete_title():
    req = request.get_json()
    title = req.get("title")
    data = load_data()
    if title in data:
        del data[title]
        save_to_db(data)
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
    #要進行網頁使用時 (Python app.py)
