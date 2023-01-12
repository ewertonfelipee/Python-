# def trata_texto(texto):
#     return texto.replace("'","").strip()

futebol = [
    "sa'o paulo, sp     ",
    "man unite''d',ing"
]

# fut = []
# for soccer in futebol:
#     fut.append(trata_texto(soccer))
# print(fut)

result = list(map(lambda texto: texto.replace("'","").strip(), futebol))
print(result)

result_filter = list(filter(lambda fut: "sp" in fut, result))
print(result_filter)