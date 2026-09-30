# Regresión y ANOVA

Apuntes de la asignatura **Regresión y ANOVA** (3.º del Grado en Estadística / INdat,
Universidad de Valladolid, curso 2026–2027).

## Contenido

**Bloque de regresión**
1. Introducción a los modelos lineales
2. El modelo de regresión simple
3. Inferencias en regresión
4. Validación del modelo de regresión lineal simple
5. El modelo de regresión lineal en notación matricial
6. Introducción al modelo de regresión lineal múltiple

**Bloque de ANOVA**: pendiente (Temas 7 en adelante).

## Compilar

El código LaTeX está en [`Apuntes_TeX/`](Apuntes_TeX/). Se necesita una distribución de LaTeX
con `latexmk` (por ejemplo, TeX Live o MiKTeX).

Dentro de `Apuntes_TeX/`:

```bash
latexmk
```

El PDF se genera en `Apuntes_TeX/build/Apuntes_RANO.pdf`, junto con los archivos auxiliares.
Para borrarlos: `latexmk -C`.

**VS Code:** abrir la carpeta `Apuntes_TeX` con la extensión LaTeX Workshop, que usa la
configuración incluida en `.vscode/`: recompila al guardar y muestra el PDF con `Ctrl+Alt+V`.

## Estructura

```
Apuntes_TeX/
├── main.tex               documento principal (bloque de regresión)
├── bloque_regresion.tex   lista de temas del bloque
├── latexmkrc              configuración de latexmk
├── preambulo/             paquetes, cajas y notación común
├── temas/temaN/           un archivo por sección de cada tema
└── datos/                 datos de las gráficas (TikZ/pgfplots)
```

## Aviso

Los apuntes se han elaborado con ayuda de herramientas de inteligencia artificial a partir de
las diapositivas de la asignatura. Pueden contener errores o imprecisiones y no sustituyen al
material oficial, que debe consultarse ante cualquier duda.
