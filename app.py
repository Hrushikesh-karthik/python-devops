from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Flask CI/CD Demo 🚀</h1>
    <p>Deployed using GitHub Actions + Docker + Helm + Argo CD + Kubernetes</p>
    """


@app.route("/health")
def health():
    return jsonify(
        status="healthy",
        service="flask-cicd-demo"
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

