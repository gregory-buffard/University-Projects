from fonctionsSupport import chargeFichierCsv, traceCourbe

data = chargeFichierCsv('./traceAtraiter.csv')

def extraireDonne(data: list[list[str, str]]) -> list[list[float], list[float]]:
    output = [[], []]
    for i in data:
        output[0].append(float(i[0]))
        output[1].append(float(i[1]))
    return output

sep = extraireDonne(data)
X, Y = sep[0], sep[1]

# print(X[:4])
# print(Y[:4])

# traceCourbe(X, Y, [], "Courbe du parametre brut")

def moyenne(L: list[float]) -> float:
    output = 0
    for i in L:
        output += i
    return output / len(L)

assert (abs(10 - moyenne([10])) < 0.01)
assert (abs(9 - moyenne([8.5, 9.5])) < 0.01)
assert (abs(12.5 - moyenne([10, 12.5, 15])) < 0.01)

def moyenneGlissante(Y: list[float], n: int) -> list[float]:
    YLisse = [0] * len(Y)
    k = n // 2
    for i in range(k, len(Y) - k):
        YLisse[i] = moyenne(Y[i - k : i + k + 1])
    return YLisse

traceCourbe(X, Y, moyenneGlissante(Y, 5), "Courbe du parametre lisse")

def pente(X: list[float], Y_bruite: list[float]) -> float:
    n = len(X)
    if n < 2:
        return 0
    return (Y_bruite[-1] - Y_bruite[0]) / (X[-1] - X[0])