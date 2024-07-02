# Cosmological Volume Tutorial

This tutorial will take you through the generation of a large-scale cosmological simulation.
The slides may be found [here](https://github.com/cspotz/ramses-tutorials/tree/main/Cosmological-Volume/Slides/TUTO.pdf)
A (working) google collab version can be found [here](https://colab.research.google.com/drive/1ktrkdsTkbjnvwFCGzPxvVOl5n6l2nUkY?usp=sharing). Your first task will be to port it to your laptop, and them to a cluster facility.

## Initial condition generation 
To generate initial condition, we will use [monofonic](https://bitbucket.org/ohahn/monofonic/src/master/). An older alternative may be [MUSIC](https://www-n.oca.eu/ohahn/MUSIC/). They require FFTW3, GSL, as well as a CMake build system and a reasonably new C++14 compliant compiler. In order to install them, some usefull information may be found in the the [manual](https://bitbucket.org/ohahn/monofonic/wiki/Home).
Once this step performed, it should be possible to install monofonic doing  
   ```
   git clone https://bitbucket.org/ohahn/monofonic.git
   mkdir monofonic/build; cd monofonic/build
   cmake ..
   make
   ```
leading to an executable.
We now  can be use it generate initial condition using for instance the file [monofonic.conf](./monofonic.conf):
   ```
   ./build/monofonIC /monofonic.conf
   ```
 At that stage, initial condition files of the type `ics_ramses/ic_posx` should have been generated.

## Non-linear evolution
We will use [RAMSES](https://github.com/ramses-organisation/ramses) that needs a fortran compiler. It may be installed by running in a terminal
   ```
   git clone https://github.com/ramses-organisation/ramses.git
   cd ramses/bin
   make clean
   make NDIM=3
   ```
leading to an executable that can be used to solve the non-linear Poisson equation for instance the file [ramses.nml](./ramses.nml), to run
  ```
  bin/ramses3d namelist/ramses.nml
  ```
At that stage, the simulation should be finished and folders of the type `output_00002` should have been generated.
## Data analysis out the output generated:
We will work in python and use (among others) [Pylians](https://pylians3.readthedocs.io/en/master/index.html) and [yt](https://yt-project.org/), to install them, some usefull information may be found  [here](https://pylians3.readthedocs.io/en/master/installation.html) and [here](https://yt-project.org/doc/installing.html).
We will now follow this  [notebook](./cosmology_ramses.ipynb) to analyse the data produced by the simulation.
