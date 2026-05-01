"""
Génération des visualisations pour la présentation
"L'Ingénierie Biomédicale" — support reveal.js

Exécution :
    python3 generate_charts.py

Sorties :
    market_segments.png
    biomaterials_breakdown.png
    growth_projection.png
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

# ── Répertoire de sortie (même dossier que ce script) ─────────────────────────
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Palette sobre & classique ─────────────────────────────────────────────────
PALETTE_BLUES = ["#1565C0", "#1976D2", "#1E88E5", "#42A5F5", "#90CAF9"]
PALETTE_MIXED = ["#1565C0", "#2E7D32", "#6D4C41", "#7B1FA2", "#E65100"]
BG_COLOR      = "#F8F9FA"
TEXT_COLOR    = "#1A2B3C"

sns.set_theme(style="whitegrid", font_scale=1.15)


# ── 1. Segments du marché mondial des dispositifs médicaux (Mds USD, 2023) ────
def chart_market_segments():
    segments = [
        "Diagnostic in vitro",
        "Cardiologie & vasculaire",
        "Imagerie médicale",
        "Orthopédie",
        "Endoscopie",
        "Neurologie",
    ]
    values = [78, 61, 46, 41, 36, 19]   # Source : GlobalData / IMDRF 2023 estimates

    fig, ax = plt.subplots(figsize=(8, 4.5))
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    bars = ax.barh(segments, values, color=PALETTE_BLUES[:len(segments)],
                   edgecolor="white", height=0.6)

    for bar, val in zip(bars, values):
        ax.text(val + 0.8, bar.get_y() + bar.get_height() / 2,
                f"{val} Md$", va="center", fontsize=11, color=TEXT_COLOR)

    ax.set_xlabel("Milliards USD", color=TEXT_COLOR, fontsize=11)
    ax.set_title("Marché mondial des dispositifs médicaux — 2023\n(principaux segments)",
                 color=TEXT_COLOR, fontsize=12, pad=10)
    ax.tick_params(colors=TEXT_COLOR)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.xaxis.grid(True, linestyle="--", alpha=0.5)
    ax.set_xlim(0, 95)

    plt.tight_layout()
    path = os.path.join(OUT_DIR, "market_segments.png")
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close(fig)
    print(f"✔ Sauvegardé : {path}")


# ── 2. Répartition des types de biomatériaux (% des implants commercialisés) ──
def chart_biomaterials_breakdown():
    labels   = ["Métaux & alliages", "Polymères", "Céramiques", "Composites"]
    sizes    = [40, 35, 16, 9]    # estimations IUPAC / Ratner et al. 2020
    colors   = PALETTE_MIXED[:4]
    explode  = (0.05, 0.05, 0.05, 0.05)

    fig, ax = plt.subplots(figsize=(6, 5))
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    wedges, texts, autotexts = ax.pie(
        sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.0f%%", startangle=140,
        pctdistance=0.72, labeldistance=1.12,
        wedgeprops=dict(edgecolor="white", linewidth=2),
    )
    for t in texts + autotexts:
        t.set_color(TEXT_COLOR)
        t.set_fontsize(11)

    ax.set_title("Types de biomatériaux utilisés dans les implants commerciaux",
                 color=TEXT_COLOR, fontsize=11, pad=14)

    plt.tight_layout()
    path = os.path.join(OUT_DIR, "biomaterials_breakdown.png")
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close(fig)
    print(f"✔ Sauvegardé : {path}")


# ── 3. Projection de croissance du marché biomédical 2018-2030 ────────────────
def chart_growth_projection():
    years  = list(range(2018, 2031))   # 13 points : 2018 à 2030 inclus
    # Valeurs indicatives (Mds USD), CAGR ≈ 5,5 % (Evaluate MedTech / GlobalData)
    # Périmètre : dispositifs médicaux à usage unique + durables + diagnostique in vitro
    market = [430, 452, 475, 480, 495, 515, 545, 576, 608, 642, 678, 716, 756]

    fig, ax = plt.subplots(figsize=(8, 4.5))
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    ax.plot(years, market, color=PALETTE_BLUES[0], linewidth=2.5, marker="o",
            markersize=5, label="Taille du marché (Mds USD)")

    # Zone de projection (2024 →)
    proj_years  = years[6:]
    proj_values = market[6:]
    ax.fill_between(proj_years, proj_values,
                    alpha=0.15, color=PALETTE_BLUES[0], label="Projection (CAGR ≈ 5,5 %)")

    ax.axvline(x=2023.5, color="#E65100", linestyle="--", linewidth=1.5, alpha=0.7)
    ax.text(2023.6, 470, "2024", color="#E65100", fontsize=10)

    ax.set_xlabel("Année", color=TEXT_COLOR, fontsize=11)
    ax.set_ylabel("Milliards USD", color=TEXT_COLOR, fontsize=11)
    ax.set_title("Croissance du marché mondial des dispositifs médicaux",
                 color=TEXT_COLOR, fontsize=12, pad=10)
    ax.legend(fontsize=10, framealpha=0.6)
    ax.tick_params(colors=TEXT_COLOR)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    path = os.path.join(OUT_DIR, "growth_projection.png")
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close(fig)
    print(f"✔ Sauvegardé : {path}")


if __name__ == "__main__":
    chart_market_segments()
    chart_biomaterials_breakdown()
    chart_growth_projection()
    print("\nToutes les visualisations ont été générées.")
