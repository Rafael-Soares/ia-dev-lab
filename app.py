from flask import Flask, render_template

from src.market.calculos import gerar_ranking
from src.market.dados_demo import get_dados_demo

app = Flask(__name__)


@app.route("/ranking")
def ranking():
    dados = get_dados_demo()
    ranking_result = gerar_ranking(dados)
    return render_template("ranking.html", ranking=ranking_result)
