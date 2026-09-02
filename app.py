from flask import Flask, render_template

from src.market.calculos import gerar_ranking_acoes
from src.market.dados_demo import obter_dados_demonstracao

app = Flask(__name__)


@app.route("/ranking")
def ranking():
    ranking_acoes = gerar_ranking_acoes(obter_dados_demonstracao())
    return render_template("ranking.html", ranking=ranking_acoes)


if __name__ == "__main__":
    app.run(debug=True)
