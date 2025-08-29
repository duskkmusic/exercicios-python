times_brasileirao = (
    "Flamengo",
    "Palmeiras",
    "Cruzeiro",
    "Bahia",
    "Botafogo",
    "Mirassol",
    "São Paulo",
    "Bragantino",
    "Fluminense",
    "Ceará SC",
    "Corinthians",
    "Atlético-MG",
    "Internacional",
    "Grêmio",
    "Santos",
    "Vasco da Gama",
    "EC Vitória",
    "Juventude",
    "Fortaleza",
    "Sport Recife"
)
print(f"Os 5 Primeiros colocados sao: {times_brasileirao[:5]} ")
print("-=-"*20)
print(f"Os 4 Ultimos colocados sao: {times_brasileirao[-4:]} ")
print("-=-"*20)
print(f"Times em ordem alfabetica: {sorted(times_brasileirao)} ")
print("-=-"*20)
print(f"O Bahia esta na {times_brasileirao.index('Bahia') + 1} posicao")

