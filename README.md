# Resources

## Python

* [Exercises](python/exercises/)
* [Solutions](python/solutions/)
* [Slides](python/slides/)

## R


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
