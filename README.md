# Resources

## Python

* [Exercises](python/exercises/)
* [Solutions](python/solutions/)
* [Slides](python/slides/)

## R
* [classes and variables](R/scripts/s01_operators_classes_and_variables.ipynb)
* [data objects](R/scripts/s02_data_storage_objects.ipynb)
* [control flow and repetition](R/scripts/s03_control_flow_and_repetition.ipynb)
* [functions](R/scripts/s04_functions.ipynb)
* [dplyr & tidyr](R/scripts/s05_dplyr_and_tidyr.ipynb)
* [reshaping data](R/scripts/s06_data_reshaping_summarization_and_merging.ipynb)
* [visualization](R/scripts/s07_data_visualization.ipynb)
* [read and write](R/scripts/s08_read_and_write.ipynb)

# Software

# Requirements for server setup

Each txt contains the libraries that are needed from the matching repository. So, if an extra requirement is needed, add this to the correct(!) file.

## Python - conda environment
1. Create environment
```
conda env create -f conda_env_BPiDD.yml
```
2. Add kernel to notebook kernels visible in Jupyter:
```
python -m ipykernel install --user --name BPiDD --display-name "Python3 (BPiDD)"
```
