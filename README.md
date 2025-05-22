# Plot the decision trees of a Random Forests Classifier 

Minimal wrappers for visualizing and comparing scikit-learn random forest models trained for flood mapping, using [pybaobabdt](https://gitlab.tue.nl/20040367/pybaobab). 
The class is represented by color and the width of the link represents the number of samples flowing from one node to the other.

**Python 3.8 required** :snake:
**Note:** Only models trained with scikit-learn == 1.3 are guaranteed to plot correctly.

---

## Example

### Random Forest trained on balanced samples
![tree_and_forest_Random Forest_balanced_random_500_no_tuning_valencia_iter2](https://github.com/user-attachments/assets/3d3b8116-7b93-4a2b-91ce-42f712de4c5c)

### Random Forest trained on random samples
![tree_and_forest_Random Forest_simple_random_500_no_tuning_valencia_iter2](https://github.com/user-attachments/assets/b4097540-070d-4aff-a02b-b8d9e5f79189)
---

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/paulhosch/plot_random_forests.git
   cd plot_random_forests
   ```
2. **Create a Python 3.8 environment (recommended):**
   ```bash
   conda create -n pybaobab38 python=3.8
   conda activate pybaobab38
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   # or, to install the pybaobabdt fork directly:
   pip install git+https://github.com/paulhosch/pybaobab-fork-fork.git
   ```

---

## Credits

All credit for the visualization technique goes to [pybaobabdt](https://gitlab.tue.nl/20040367/pybaobab):

> S. van den Elzen and J. J. van Wijk, "BaobabView: Interactive construction and analysis of decision trees," 2011 IEEE Conference on Visual Analytics Science and Technology (VAST), 2011, pp. 151-160, doi: [10.1109/VAST.2011.6102453](https://doi.org/10.1109/VAST.2011.6102453)
