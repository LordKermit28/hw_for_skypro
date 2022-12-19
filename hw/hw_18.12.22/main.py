from flask import Flask, render_template
import utils

app = Flask(__name__)

pk = ""
candidate_name = ''
skill = ''


@app.route("/")
def index():
    candidates = utils.get_all_candidates()
    return render_template('list.html', candidates=candidates)

@app.route("/candidates/<int:pk>")
def get_candidate(pk):
    candidate = utils.get_candidate_by_pk(pk)
    return render_template("card.html", candidate = candidate)

@app.route("/search/<candidate_name>")
def get_candidate_by_name(candidate_name):
    candidates = utils.get_candidate_by_name(candidate_name)
    return render_template("search.html", candidates = candidates, count_candidates = len(candidates))

@app.route("/skills/<skill>")
def get_candidate_by_skills(skill):
    candidates = utils.get_candidates_by_skill(skill)
    return render_template("skill.html", candidates = candidates, count_candidates = len(candidates))


app.run(debug=True)