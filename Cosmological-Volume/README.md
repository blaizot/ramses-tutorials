In this tutorial we are going to use a number of third-party tools that must be installed before we start. 

If you are not familiar with the installation of packages, you may skip to [Section 2](#2-installation-with-conda) where we provide instructions to install a working environment with conda. If you are familiar with the installation of packages, you should follow the steps outlined in [Section 1](#1-expert-mode). 

The compilation of RAMSES and the definition of useful environment variables are covered in [Section 3](#3-setting-up-ramses). 


**Once everything is installed, you can start the tutorial by opening the python notebook `tutorial.ipynb`.**


# 1. Expert mode 

## compilers

We will need a **fortran compiler** for RAMSES, and a **C++ and C compiler** for some third-party tools (MUSIC, monophonic). We will also need some MPI version if you have access to multiple cores. Monophonic also requires `CMAKE`.

We recommend installing recent versions of `gcc` (incl. `gfortran`) and `openmpi`. 

## python

The tutorial requires running `python3` in a `Jupyter notebook`. 

We will use a the following python packages: 
```
numpy, astropy, matplotlib, yt, yt_astro_analysis, colossus
```

## MUSIC / MONOFONIC

To generate initial condition, we will use either [monofonic](https://bitbucket.org/ohahn/monofonic/src/master/) or [MUSIC](https://www-n.oca.eu/ohahn/MUSIC/). Use `monofonic` if you are interested only in large-scale volumes, and use `MUSIC` if you anticipate you will run zoom-in simulations later. 

Both codes require FFTW3, GSL, CMake, and a reasonably recent C++14 compliant compiler. Once these are installed, it should be possible to install monofonic or MUSIC doing: 
   ```
   git clone https://bitbucket.org/ohahn/monofonic.git
   mkdir monofonic/build; cd monofonic/build
   cmake ..
   make
   ```
or 
   ```
   git clone https://bitbucket.org/ohahn/music.git
   mkdir music/build; cd music/build
   cmake ..
   make
   ```




# 2. Installation with conda

**This is mostly copy/paste from RASCAS ... will be updated later...**

Conda is available for Windows, Linux, and macOS.

Install miniconda following the installation guide, or if you already have a version of conda installed, make sure to have an up-to-date version by running the following command in a terminal.

```
conda update -n base conda
```

Download the environment file rascas-environment.yml

Create the environment from the rascas-environment.yml file by executing the command below in a terminal.

```
conda env create -f rascas-environment.yml
```

Activate the new environment by executing the command below in a terminal.

```
conda activate rascas-env
```

Verify that the new environment was installed correctly with

```
conda env list
```

# 3. Setting up RAMSES

## RAMSES 
We will use [RAMSES](https://github.com/ramses-organisation/ramses) that needs a fortran compiler. It may be installed by running the following commands in a terminal
   ```
   git clone https://github.com/ramses-organisation/ramses.git
   cd ramses/bin
   make clean
   make NDIM=3
   ```
If you have MPI installed, use `make MPI=1 NDIM=3` instead. 

Within this tutorial, it helps to set an environment variable that points to the RAMSES executable. Do this with the following command (in any terminal you use to run RAMSES):
```
export RAMSESDIR=/path/to/your/ramses
```


NB: here we should define a number of environement variables, for example:
```
export MUSICDIR=/path/to/MUSIC/
export RAMSESDIR=/path/to/ramses/
```

