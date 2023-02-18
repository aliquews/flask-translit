import os
import sys
import subprocess

from flask import Flask, send_file, render_template, request
from transliterate import translit

sys.path = ['','..'] + sys.path[1:]
from src.logic import export_data, get_data
from src.db.db_operations import create
from src.db.models import Translit


app = Flask(__name__, template_folder="templates")

test_db = [i for i in range(15)]

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
    
    result = [Translit.from_orm(t.Translation) for t in get_data.get_latest()]

    return [f'{t.text} -> {t.text_translit}' for t in result]



if __name__ == "__main__":
    subprocess.run(["alembic", "upgrade", "head"])
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)