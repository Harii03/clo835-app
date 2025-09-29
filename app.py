from flask import Flask, render_template_string
import os, socket, pymysql

app = Flask(__name__)
BG = os.getenv("BG_COLOR", "white")
DB_HOST = os.getenv("DB_HOST", "mysql")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASSWORD", "secret")
DB_NAME = os.getenv("DB_NAME", "appdb")

TEMPLATE = """
<!doctype html>
<title>CLO835 App - {{color}}</title>
<body style="background: {{color}}; font-family: sans-serif;">
  <h1 style="color:#111">CLO835 Demo ({{color}})</h1>
  <p>Hostname: {{host}}</p>
  <p>DB status: {{db_status}}</p>
</body>
"""

@app.route("/")
def index():
    db_status = "Not checked"
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME, connect_timeout=3)
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
        conn.close()
        db_status = "OK (connected)"
    except Exception as e:
        db_status = f"ERROR: {e}"
    return render_template_string(TEMPLATE, color=BG, host=socket.gethostname(), db_status=db_status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
