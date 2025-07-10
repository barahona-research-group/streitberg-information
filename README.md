# Streitberg Information: Higher-Order Interaction Measures

This repository provides an implementation of Streitberg information, an information-theoretic measure for quantifying higher-order interactions from observational data. The codebase also supports related measures such as Lancaster information and total correlation for interactions of order 2, 3, 4, and 5.


## Usage

- **Jupyter Tutorial:**  
  See `tutorial.ipynb` for a step-by-step guide on using Streitberg information measures with a toy example.

- **Core Implementation:**  
  - `hoi_info.py`: Main implementation of Streitberg, Lancaster, and total correlation measures.
  - `synthetic_data.py`: Functions to generate synthetic higher-order datasets (e.g., XOR gate, COPY gate, Multivariate Gaussian).

- **Example:**
  ```python
  from hoi_info import Streitberg_4
  from ite.cost.x_factory import co_factory
  co = co_factory(cost_name='BDTsallis_KnnK', mult=True, alpha=0.5, k=30) 
  data = np.random.randn(100, 4)
  si = Streitberg_4(data, co.estimation)
  ```

## Repository Structure

- `ite/`: Contains code from the ITE Python package ([ITE on Bitbucket](https://bitbucket.org/szzoli/ite-in-python/src/master/)), including functions for estimating Tsallis-alpha divergence.
- `hoi_info.py`: Core implementation of information measures.
- `synthetic_data.py`: Synthetic data generators.
- `tutorial.ipynb`: Jupyter notebook tutorial.


## Citation

If you use this code in your work, please cite:

```
@InProceedings{pmlr-v258-liu25f,
  title = {Information-Theoretic Measures on Lattices for Higher-Order Interactions},
  author = {Liu, Zhaolu and Barahona, Mauricio and Peach, Robert},
  booktitle = {Proceedings of The 28th International Conference on Artificial Intelligence and Statistics},
  pages = {2206--2214},
  year = {2025},
  volume = {258},
  series = {Proceedings of Machine Learning Research},
  publisher = {PMLR},
  url = {https://proceedings.mlr.press/v258/liu25f.html}
}
```