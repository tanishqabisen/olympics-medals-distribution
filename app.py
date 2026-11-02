from flask import Flask, render_template

app = Flask(__name__)

# Tableau Public views
DASHBOARD_URL = (
    "https://public.tableau.com/views/olympicreportanalysis/"
    "OlympicDashboard?:showVizHome=no&:embed=true"
)
STORY_URL = (
    "https://public.tableau.com/views/olympicreportanalysis/"
    "Story1?:showVizHome=no&:embed=true"
)

@app.route("/")
def home():
    return render_template(
        "index.html",
        dashboard_url=DASHBOARD_URL,
        story_url=STORY_URL
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
