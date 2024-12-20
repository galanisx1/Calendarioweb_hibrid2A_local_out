from flask import Flask, render_template
import os  # Añadir esta línea

# Importar las tablas
from tables import calendar_table, pricing_tables, pricing_tables_credit, pricing_tables_extra

app = Flask(__name__)

@app.route("/")
def index():
    # Pasar las tablas a la plantilla
    return render_template("index.html", calendar_table=calendar_table, pricing_tables=pricing_tables, pricing_tables_credit=pricing_tables_credit, pricing_tables_extra=pricing_tables_extra)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))





