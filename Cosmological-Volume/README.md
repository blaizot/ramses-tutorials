# Cosmological Volume Tutorial

This tutorial will take you through the generation of a large-scale cosmological simulation and some analysis of its outputs. The are 5 steps in the tutorial.
1. Install pre-requisites;
2. Generate initial conditions;
3. Run the cosmological simulation with RAMSES;
4. Analyse the outpiuts;
5. Experiment with different options in RAMSES. 

## 1. Pre-requisites
**JB: I use MUSIC and postpone using monofonic to later when i can compile it... The aim will be to produce a conda environment where everything works smoothly.**

In this tutorial we are going to use a number of third-party tools that must be installed before we start. Follow the steps below. 

### MUSIC / MONOFONIC



To generate initial condition, we will use either [monofonic](https://bitbucket.org/ohahn/monofonic/src/master/) or [MUSIC](https://www-n.oca.eu/ohahn/MUSIC/). Use `monofonic` if you are interested only in large-scale volumes, and use `MUSIC` if you anticipate you will run zoom-in simulations later. 

Both codes require FFTW3, GSL, CMake, and a reasonably recent C++14 compliant compiler. 

Follow the detailed installation guide by for [monofonic](https://bitbucket.org/ohahn/monofonic/wiki/Home) or [MUSIC](h).
Once this step performed, it should be possible to install monofonic doing  
   ```
   git clone https://bitbucket.org/ohahn/monofonic.git
   mkdir monofonic/build; cd monofonic/build
   cmake ..
   make
   ```
leading to an executable.

### python packages
Colossus, yt, 

### RAMSES 
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

## 2. Initial condition generation 

We now  can be use it generate initial condition using for instance the file [monofonic.conf](./monofonic.conf):
   ```
   ./build/monofonIC /monofonic.conf
   ```
 At that stage, initial condition files of the type `ics_ramses/level_007/ic_posx` should have been generated.

## 3. RAMSES simulation (non-linear evolution)
We will now use RAMSES to solve the non-linear Poisson equation. RAMSES uses a parameter file, for instance the file [ramses.nml](./ramses.nml). To run, type:
  ```
  bin/ramses3d namelist/ramses.nml 
  ```
  or, if you compiled with MPI: 
  ```
  mpirun -np 5 $RAMSESDIR/bin/ramses3d namelist/ramses.nml
  ```
At that stage, the simulation should be finished and folders of the type `output_00002` should have been generated.
## 4. Data analysis out the output generated:
We will work in python and use (among others) [Pylians](https://pylians3.readthedocs.io/en/master/index.html) and [yt](https://yt-project.org/), to install them, some usefull information may be found  [here](https://pylians3.readthedocs.io/en/master/installation.html) and [here](https://yt-project.org/doc/installing.html).
We will now follow this  [notebook](./cosmology_ramses.ipynb) to analyse the data produced by the simulation.


## 5. More fun. 
