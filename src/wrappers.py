import pybaobabdt
import matplotlib.pyplot as plt
import pathlib
from src.vis_params import CMAP
import matplotlib.patheffects as path_effects
import numpy as np

def plot_tree(model, tree_idx=0, figsize=(12, 8), out_dir=None, title=None):
    print(f"Plotting tree {tree_idx} out of {len(model.estimators_)} trees")
    fig, ax = plt.subplots(figsize=figsize)

    ax = pybaobabdt.drawTree(
        model.estimators_[tree_idx],
        model=model,
        features=list(model.feature_names_in_),
        colormap=CMAP,
        ratio=1,
        ax=ax
    )
        
    # Rotate Tree
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    ax.set_xlim(xlim[::-1])
    ax.set_ylim(ylim[::-1])

    # Adjust transparency
    for patch in ax.patches:
        patch.set_alpha(1)

    if title:
        plt.suptitle(f"Tree {tree_idx} \n{title}")

    plt.tight_layout()
    # Save and show
    if out_dir:
        out_path = pathlib.Path(out_dir) / f"tree_{tree_idx}_{title}.png"
        plt.savefig(out_path, format='png', dpi=300, transparent=True)
        print(f"Saved to {out_path}")

    plt.show()

def plot_forest(model, n_trees_to_plot=16, figsize=(12, 8), out_dir=None, title=None):

    fig = plt.figure(figsize=figsize)

    n_trees = len(model.estimators_)

    print(f"Plotting {n_trees_to_plot} out of {n_trees} trees")

    for idx, tree in enumerate(model.estimators_[:n_trees_to_plot]):
        n_cols = int(np.ceil(np.sqrt(n_trees_to_plot)))
        n_rows = int(np.ceil(n_trees_to_plot / n_cols))
        ax1 = fig.add_subplot(n_rows, n_cols, idx+1)
        pybaobabdt.drawTree(tree, 
                            model=model, 
                            colormap=CMAP,
                            features=list(model.feature_names_in_) ,
                                ax=ax1,
                                ratio=1)
        xlim = ax1.get_xlim()
        ylim = ax1.get_ylim()
        ax1.set_xlim(xlim[::-1])
        ax1.set_ylim(ylim[::-1])
        ax1.set_title(f'Tree {idx+1}', fontsize=8)

        for patch in ax1.patches:
            patch.set_alpha(1)  # Set to your desired opacity (0.0 = fully transparent, 1.0 = fully opaque)

        for text in ax1.texts:
            # Remove the outline by setting path effects to an invisible stroke
            text.set_path_effects([
                path_effects.Stroke(linewidth=0, foreground='none', alpha=0),
                path_effects.Normal()
            ])
            # Also make the text itself invisible
            text.set_color('none')
    if title:
        fig.suptitle(f"First {n_trees_to_plot} trees of forest \n{title}")
    plt.tight_layout()

    if out_dir:
        out_path = pathlib.Path(out_dir) / f"forest_{n_trees_to_plot}_{title}.png"
        fig.savefig(out_path, format='png', dpi=300)
        print(f"Saved to {out_path}")
    plt.show()

def plot_tree_and_forest(model, tree_idx=0, n_trees_to_plot=16, figsize=(16, 12), out_dir=None, title=None):
    n_cols = int(np.ceil(np.sqrt(n_trees_to_plot)))
    n_rows_forest = int(np.ceil(n_trees_to_plot / n_cols))

    fig = plt.figure(figsize=figsize)
    # Make first column twice as wide as other columns
    widths = [4] + [1] * n_cols
    gs = fig.add_gridspec(n_rows_forest, n_cols + 1, width_ratios=widths)

    # Left column: single tree, spanning all rows
    ax_tree = fig.add_subplot(gs[:, 0])

    pybaobabdt.drawTree(
        model.estimators_[tree_idx],
        model=model,
        features=list(model.feature_names_in_),
        colormap=CMAP,
        ratio=1,
        ax=ax_tree
    )
    xlim = ax_tree.get_xlim()
    ylim = ax_tree.get_ylim()
    ax_tree.set_xlim(xlim[::-1])
    ax_tree.set_ylim(ylim[::-1])
    for patch in ax_tree.patches:
        patch.set_alpha(1)

    # Forest: grid of trees
    for idx in range(n_trees_to_plot):
        row = idx // n_cols
        col = 1 + idx % n_cols
        ax = fig.add_subplot(gs[row, col])
        pybaobabdt.drawTree(
            model.estimators_[idx],
            model=model,
            features=list(model.feature_names_in_),
            colormap=CMAP,
            ratio=1,
            ax=ax
        )
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        ax.set_xlim(xlim[::-1])
        ax.set_ylim(ylim[::-1])
        for patch in ax.patches:
            patch.set_alpha(1)
        for text in ax.texts:
            text.set_path_effects([
                path_effects.Stroke(linewidth=0, foreground='none', alpha=0),
                path_effects.Normal()
            ])
            text.set_color('none')
    if title:
        fig.suptitle(f"Tree {tree_idx} and first {n_trees_to_plot} trees of forest \n{title}")
    plt.tight_layout()
    if out_dir:
        out_path = pathlib.Path(out_dir) / f"tree_and_forest_{title}.png"
        fig.savefig(out_path, format='png', dpi=300)
        print(f"Saved to {out_path}")
    plt.show()