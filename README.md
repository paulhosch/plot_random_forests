# plot_random_forests

Minimal wrappers for visualizing and comparing scikit-learn random forest models trained for flood mapping, using [pybaobabdt](https://gitlab.tue.nl/20040367/pybaobab).

**Python 3.8 required** :snake:

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

## Usage

See `visualize_model.py` and `compare_models.py` for example scripts to visualize and compare models.

**Note:** Only models trained with scikit-learn <=1.3 are guaranteed to plot correctly.

---

## Credits

All credit for the visualization technique goes to [pybaobabdt](https://gitlab.tue.nl/20040367/pybaobab):

> S. van den Elzen and J. J. van Wijk, "BaobabView: Interactive construction and analysis of decision trees," 2011 IEEE Conference on Visual Analytics Science and Technology (VAST), 2011, pp. 151-160, doi: [10.1109/VAST.2011.6102453](https://doi.org/10.1109/VAST.2011.6102453)
