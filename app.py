from flask import Flask, render_template

app = Flask(__name__)

DASHBOARD_URL = "https://public.tableau.com/app/profile/tanishqa.bisen/viz/GlobalOlympicsAthlete_17936424000820/Dashboard1?publish=yes"

STORY_URL = "https://public.tableau.com/app/profile/tanishqa.bisen/viz/GlobalOlympicsAthlete_17936424000820/Story1?publish=yes"


@app.route("/")
def home():
    return render_template(
        "index.html",
        dashboard_url=DASHBOARD_URL,
        story_url=STORY_URL
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)