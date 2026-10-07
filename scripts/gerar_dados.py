"""Gera os sete arquivos da prática. Dados fictícios de um posto de combustível
(litros vendidos por hora). A semente fixa garante sempre os mesmos arquivos.
Uso: python scripts/gerar_dados.py"""
import numpy as np, pandas as pd, datetime as dt
from pathlib import Path
rng = np.random.default_rng(7)
OUT = Path(__file__).resolve().parent.parent / "dados"; OUT.mkdir(exist_ok=True)

# ---------- GASOLINA: 72 valores com estatísticas de referência fixas ----------
# mín 329 | Q1 640,75 | mediana 822 | Q3 1055,75 | máx 1373 | soma 60874 (média 845,47)
# 17 valores <= 600 e 18 valores >= Q3
def bloco(n, lo, hi):
    return sorted(int(x) for x in rng.integers(lo, hi + 1, n))
g = ([329] + bloco(16, 340, 600) + [640, 641] + bloco(16, 645, 815) + [821, 823]
     + bloco(16, 830, 1050) + [1055, 1058] + bloco(16, 1065, 1360) + [1373])
livres = list(range(1, 17)) + list(range(19, 35)) + list(range(37, 53)) + list(range(55, 71))
lim = {**{i: (340, 600) for i in range(1, 17)}, **{i: (645, 815) for i in range(19, 35)},
       **{i: (830, 1050) for i in range(37, 53)}, **{i: (1065, 1360) for i in range(55, 71)}}
dif = 60874 - sum(g)
while dif != 0:                      # ajusta a soma sem sair das faixas
    i = int(rng.choice(livres)); p = 1 if dif > 0 else -1
    if lim[i][0] <= g[i] + p <= lim[i][1]:
        g[i] += p; dif -= p
g = sorted(g)

# ---------- distribui os valores pelas horas seguindo o movimento do dia ----------
perfil = np.array([.25, .2, .15, .12, .15, .3, .55, .8, .9, .75, .7, .8, .95, .85, .7, .7, .8, .95, 1.0, 1.0, .8, .6, .45, .3])
dias = [dt.date(2025, 3, 10), dt.date(2025, 3, 11), dt.date(2025, 3, 12)]
score = np.concatenate([perfil * f + rng.normal(0, .06, 24) for f in (1.05, .95, 1.0)])
score[19] = 9                                     # dia 1, 19h recebe o maior valor
ordem = np.argsort(score); gas = np.empty(72, int); gas[ordem] = g
alc = np.clip((gas * rng.uniform(.38, .55, 72)).astype(int), 90, None)
die = np.clip((gas * rng.uniform(.15, .28, 72) + rng.integers(20, 120, 72)).astype(int), 60, None)
alc[19], die[19] = 640, 2348 - 1373 - 640         # maior movimento: total 2348
for i in range(72):                               # nenhum outro total chega a 2348
    while i != 19 and gas[i] + alc[i] + die[i] >= 2300: alc[i] -= 25
base = pd.DataFrame({"DATA": [pd.Timestamp(d) for d in dias for _ in range(24)], "HORA": list(range(24)) * 3,
                     "GASOLINA": gas, "ALCOOL": alc, "DIESEL": die})
for n in range(3):
    base.iloc[n * 24:(n + 1) * 24].to_excel(OUT / f"dia0{n + 1}.xlsx", index=False)

# ---------- planilha "geradora": colunas auxiliares + linha de total sem DATA ----------
gg = (perfil * 1100 * rng.normal(1, .08, 24)).astype(int) + 250
bruto = pd.DataFrame({"DATA": [pd.Timestamp(2025, 3, 13)] * 24, "HORA": range(24), "GASOLINA": gg,
                      "ALCOOL": (gg * rng.uniform(.38, .55, 24)).astype(int),
                      "DIESEL": (gg * rng.uniform(.18, .3, 24)).astype(int)})
bruto["FATOR_MOVIMENTO"] = perfil.round(2)
bruto["ALEATORIO"] = rng.random(24).round(4)
bruto["OBS"] = ["gerado automaticamente"] * 24
total = {"DATA": None, "HORA": "TOTAL", "GASOLINA": bruto.GASOLINA.sum(), "ALCOOL": bruto.ALCOOL.sum(),
         "DIESEL": bruto.DIESEL.sum(), "FATOR_MOVIMENTO": None, "ALEATORIO": None, "OBS": None}
pd.concat([bruto, pd.DataFrame([total])], ignore_index=True).to_excel(OUT / "diaxx_gerador_aleatorio.xlsx", index=False)

# ---------- mesma tabela em três formatos ----------
m = pd.DataFrame({"CODIGO": range(101, 111),
                  "PRODUTO": ["Gasolina comum", "Gasolina aditivada", "Etanol", "Diesel S10", "Diesel S500",
                              "Óleo de motor", "Aditivo de radiador", "Fluido de freio", "Palheta", "Lavagem simples"],
                  "DESCRICAO": ["Combustível vendido por litro", "Combustível com aditivos de limpeza", "Álcool hidratado, por litro",
                                "Diesel com baixo teor de enxofre", "Diesel para veículos antigos", "Frasco de 1 litro",
                                "Frasco de 1 litro, pronto para uso", "Frasco de 500 ml", "Par de palhetas para para-brisa",
                                "Lavagem externa do veículo"]})
m.to_excel(OUT / "mussum.xlsx", index=False)
m.to_csv(OUT / "mussum.csv", sep=";", index=False)
m.to_csv(OUT / "mussum2.txt", sep="|", index=False)
