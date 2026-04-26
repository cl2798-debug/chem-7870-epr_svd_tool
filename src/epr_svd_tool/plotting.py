import matplotlib.pyplot as plt
import numpy as np

def _plot_waterfall(ax, field, matrix, title, every=1):
    n_spectra = matrix.shape[1]
    sampled = matrix[:, ::every]
    max_amp = np.nanmax(np.abs(sampled))
    offset = 0.2 * max_amp if max_amp > 0 else 1.0
    yticks = []
    ylabels = []
    for j, i in enumerate(range(0, n_spectra, every)):
        y_shift = j * offset
        ax.plot(field, matrix[:, i] + y_shift, linewidth=1)
        if i == 0 or (i + 1) % 5 == 0:
            yticks.append(y_shift)
            ylabels.append(str(i + 1))
    ax.set_xlabel("Magnetic Field")
    ax.set_ylabel("Scan Number")
    ax.set_title(title)
    ax.set_yticks(yticks)
    ax.set_yticklabels(ylabels)

def save_comparison_waterfall(field, raw_matrix, svd_matrix, outpath, title, every=1):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharex=True, sharey=True)
    _plot_waterfall(axes[0], field, raw_matrix, f"{title} | Raw", every=every)
    _plot_waterfall(axes[1], field, svd_matrix, f"{title} | SVD cleaned", every=every)
    axes[0].tick_params(axis="y", labelleft=True)
    axes[1].tick_params(axis="y", labelleft=True)
    fig.tight_layout()
    fig.savefig(outpath, dpi=300)
    plt.close(fig)