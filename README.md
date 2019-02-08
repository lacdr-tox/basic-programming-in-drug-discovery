# Resources

## Python

* [Exercises](python/exercises/)
* [Solutions](python/solutions/)
* [Slides](python/slides/)

#### Recommended resources for learning python on your own and/or refreshing your skills
* [Interactive tutorial at DataCamp (only free parts)](https://www.datacamp.com/courses/intro-to-python-for-data-science)
* [Interactive tutorial at Learn Python (skip advanced part)](https://www.learnpython.org)
* [Python for Biologists: covers same topics that were covered in the Python basics part of the course LACDR course](https://pythonforbiologists.com/index.php/introduction-to-python-for-biologists/python-for-biologists-introduction/)
#### Recommended resources for data analysis in Python
* [Python data science handbook](https://github.com/jakevdp/PythonDataScienceHandbook)
* [Matplotlib tutorial](https://matplotlib.org/users/pyplot_tutorial.html)
* [Seaborn tutorial](https://seaborn.pydata.org/tutorial.html)
* [Jupyter notebook introduction](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
* [Effective Pandas](https://github.com/TomAugspurger/effective-pandas)
* [Cheat sheets (R and Python)](https://www.datacamp.com/community/data-science-cheatsheets)

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
