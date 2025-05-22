#%%
import matplotlib.pyplot as plt
import pybaobabdt
from matplotlib.colors import ListedColormap
import matplotlib.patheffects as path_effects
import joblib
import pathlib
import numpy as np
from src.wrappers import plot_tree, plot_forest, plot_tree_and_forest


experiment_id = "main_experiment"
site_id = "valencia"
model_type = "Random Forest" # Balanced Random Forest, Weighted Random Forest, Random Forest
sampling_strategy = "balanced_random" # balanced_random, simple_random, weighted_random, simple_systematic, weighted_systematic, balanced_systematic, simple_grts, weighted_grts, balanced_grts
sampling_size = 500
tuning_strategy = "no_tuning" # no_tuning, BayesianSearchCV
iteration_idx = 2

title = f"{model_type}_{sampling_strategy}_{sampling_size}_{tuning_strategy}_{site_id}_iter{iteration_idx}"
out_dir = f"../sarFlood/data/experiments/{experiment_id}/plots/trees/"
pathlib.Path(out_dir).mkdir(parents=True, exist_ok=True)

model_path = f"../sarFlood/data/experiments/{experiment_id}/models/{model_type}_{sampling_strategy}_{sampling_size}_{tuning_strategy}_{site_id}_iter{iteration_idx}.joblib"
model = joblib.load(model_path)
print("Loaded model:", model)




#%% Visualize tree
# Get the first tree to visualize

plot_tree(model, tree_idx=0, figsize=(12, 8), out_dir=out_dir)

# %% Visualize forest

plot_forest(model, n_trees_to_plot=16, figsize=(12, 8), out_dir=out_dir)

# %%
from src.vis_params import CMAP

# Visualize tree and forest in one figure
plot_tree_and_forest(model, tree_idx=0, n_trees_to_plot=16, figsize=(12, 8), out_dir=out_dir, title=title)

# %%
