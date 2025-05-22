#%%
import matplotlib.pyplot as plt
import joblib
import pathlib
from src.wrappers import plot_tree_and_forest

# Experiment variables (set defaults)
experiment_id = "main_experiment"
site_id = "valencia"
model_type = "Random Forest"
sampling_strategy = "balanced_random"
sampling_size = 500
iteration_idx = 2
tuning_strategy = "no_tuning"

# Set which variable to compare and its values
compare_variable = "sampling_strategy"  # e.g. "tuning_strategy", "sampling_strategy", etc.
compare_values = ["balanced_random", "simple_random"]  # Set the values you want to compare

out_dir = f"../sarFlood/data/experiments/{experiment_id}/plots/trees/compare_{compare_variable}/"
pathlib.Path(out_dir).mkdir(parents=True, exist_ok=True)

for value in compare_values:
    # Set the variable dynamically
    vars()[compare_variable] = value
    title = f"{model_type}_{sampling_strategy}_{sampling_size}_{tuning_strategy}_{site_id}_iter{iteration_idx}"
    model_path = f"../sarFlood/data/experiments/{experiment_id}/models/{model_type}_{sampling_strategy}_{sampling_size}_{tuning_strategy}_{site_id}_iter{iteration_idx}.joblib"
    print(f"Comparing {compare_variable}: {value}")
    print(f"Loading model: {model_path}")
    model = joblib.load(model_path)
    print("Loaded model:", model)
    print("Features:", model.feature_names_in_)
    print("Plotting tree and forest for:", title)
    plot_tree_and_forest(
        model,
        tree_idx=0,
        n_trees_to_plot=16,
        figsize=(12, 8),
        out_dir=out_dir,
        title=title
    )
#%%
