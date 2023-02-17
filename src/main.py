from flask import Flask, send_file, render_template, request
from transliterate import translit

from src.logic import export_data
from src.db.db_operations import create


app = Flask(__name__, template_folder="templates")


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/api/translate")
def translate_ru_en():
    text = request.json["text"]
    translated_text = translit(text.lower(), language_code='ru', reversed=True)
    create(text, translated_text)
    return {
        "text": translated_text
    }


@app.get("/api/download_xls")
def download_xls():
    export_data.migrate_db_xls()
    path = "files/data.xlsx"
    try:
        return send_file(path, as_attachment=True)
    except Exception as e:  
        print(str(e))
        return "error"
    

@app.get("/api/report")
def report():
    pass