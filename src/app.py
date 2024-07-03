from flask import Flask
import os

from status import status
from static import static

app = Flask(__name__)

app.config['pg_user'] = os.environ.get("PGUSER")
app.config['pg_db'] = os.environ.get("PGDATABASE")
app.config['pg_host'] = os.environ.get("PGHOST")
app.config['pg_pass'] = os.environ.get("PGPASSWORD")

app.register_blueprint(status)
app.register_blueprint(static)

@app.route('/health')
def health():
    if os.environ.get("ENVIRONMENT") == "development":
        env_dict = dict(os.environ)
        env_dict = {key:("REDACTED" if "KEY" in key else val) for key, val in env_dict.items()}
        env_dict = {key:("REDACTED" if "PASS" in key else val) for key, val in env_dict.items()}
        return dict(env_dict)
    else:
        return "healthy"

if __name__ == '__main__':
   from waitress import serve
   serve(app, host='0.0.0.0', port=8080)
