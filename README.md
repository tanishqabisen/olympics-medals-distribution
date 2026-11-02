# Olympic Report Analysis – Flask + Tableau

## 🌐 Live Website

[Click here to view the live project](https://olympics-medals-distribution-0.onrender.com/)# Olympic Report Analysis – Flask + Tableau

## Files
- `app.py` – Flask application
- `templates/index.html` – responsive page with Dashboard and Story tabs
- `requirements.txt` – Python dependencies
- `Procfile` – Render start command

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Run: `pip install -r requirements.txt`
4. Run: `python app.py`
5. Open: http://127.0.0.1:5000

## Deploy on Render
1. Push this folder to a GitHub repository.
2. In Render, choose **New +** → **Web Service** and connect the repository.
3. Select **Python** as the runtime.
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn app:app`
6. Choose a plan and click **Create Web Service**.

The Procfile also contains the same start command.

## Tableau note
The views are embedded from Tableau Public. They must be published and publicly accessible.
If Tableau's sharing/privacy settings prevent embedding, open each view in Tableau Public and
check its sharing/embed permissions.
