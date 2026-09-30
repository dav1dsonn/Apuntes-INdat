"""Datos sintéticos (semilla fija) para las figuras del Tema 4."""
import math
import os
import random
from statistics import NormalDist

OUT = r"C:\Users\David\Documents\!3INDat\rano\Apuntes_TeX\datos\tema4"
os.makedirs(OUT, exist_ok=True)
rng = random.Random(2026)
N01 = NormalDist()


def save(name, header, rows):
    with open(os.path.join(OUT, name), "w", encoding="ascii") as f:
        f.write(" ".join(header) + "\n")
        for r in rows:
            f.write(" ".join(f"{v:.4f}" for v in r) + "\n")


# --- Patrones en el gráfico de residuos -------------------------------------
n = 32
xs = sorted(rng.uniform(0.5, 9.5) for _ in range(n))
save("nulo.dat", ["x", "r"], [(x, rng.gauss(0, 1)) for x in xs])
save("curva1.dat", ["x", "r"],
     [(x, 1.7 * math.sin((x - 2.2) * math.pi / 5.5) + rng.gauss(0, 0.18)) for x in xs])
save("curva2.dat", ["x", "r"],
     [(x, 0.13 * (x - 5) ** 2 - 1.3 + rng.gauss(0, 0.18)) for x in xs])
save("embudo_crec.dat", ["x", "r"], [(x, rng.gauss(0, 0.1 + 0.32 * x)) for x in xs])
save("embudo_decr.dat", ["x", "r"], [(x, rng.gauss(0, 0.1 + 0.32 * (10 - x))) for x in xs])
save("diamante.dat", ["x", "r"],
     [(x, rng.gauss(0, 0.15 + 2.0 * math.exp(-((x - 5) ** 2) / 4))) for x in xs])

# --- QQ-plots (n = 150) --------------------------------------------------------
m = 150
q = [N01.inv_cdf((i - 0.375) / (m + 0.25)) for i in range(1, m + 1)]


def std(v):
    mu = sum(v) / len(v)
    s = math.sqrt(sum((a - mu) ** 2 for a in v) / (len(v) - 1))
    return sorted((a - mu) / s for a in v)


asim_der = std([rng.expovariate(1.0) for _ in range(m)])
asim_izq = std([-rng.expovariate(1.0) for _ in range(m)])
colas = std([rng.gauss(0, 1) / math.sqrt(rng.gammavariate(1.0, 2.0) / 2.0) for _ in range(m)])
save("qq.dat", ["q", "der", "izq", "colas"],
     list(zip(q, asim_der, asim_izq, colas)))

# --- Masa muscular: residuos frente a la edad, por sexo ---------------------
rows = []
for sexo, centro in ((0, -0.75), (1, 0.75)):          # 0 = mujer, 1 = hombre
    for _ in range(38):
        rows.append((rng.uniform(40, 80), max(-2.9, min(2.9, rng.gauss(centro, 0.85))), sexo))
save("masa.dat", ["edad", "t", "sexo"], rows)

# --- Punto influyente ----------------------------------------------------------
base = []
for _ in range(20):
    x = rng.uniform(0, 0.95)
    base.append((x, 3.0 * x + rng.gauss(0, 0.35)))
save("infl_sin.dat", ["x", "y"], base)
save("infl_con.dat", ["x", "y"], base + [(2.0, 0.0)])
print("ok")
