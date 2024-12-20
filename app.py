from flask import Flask, render_template
from tables import calendar_table, pricing_tables, pricing_tables_credit, pricing_tables_extra
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Habilita CORS para solicitudes desde el frontend


@app.route("/")
def index():
    # Pasar las tablas a la plantilla
    return render_template("index.html", calendar_table=calendar_table, pricing_tables=pricing_tables,pricing_tables_credit=pricing_tables_credit,pricing_tables_extra=pricing_tables_extra)

if __name__ == "__main__":
    app.run(debug=True)

