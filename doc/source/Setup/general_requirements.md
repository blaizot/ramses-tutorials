# General setup requirements

Running the RAMSES tutorials requires that a number of softwares be installed (compilers, python libraries, ...). We list these requirements in [Section Requirements](#1-list-of-requirements) and the expert users should make sure they have installed everything consistently. 

For the **non expert users**, we provide guidelines in [Section Conda Setup](#2-conda-setup) to install all we need using a conda environment. 

If you are running the tutorials on the **Centre Blaise Pascal** (CBP), please follow the [dedicated instructions on this page](CBP.md).

## 1. List of Requirements 
Here is a **list of all required packages**. More details are given below the list. 
```
# general
- git
- make
- cmake

# compilers
- gfortran 
- gcc
- gxx
- openmpi

# python 
- python=3.12
- pip
- numpy
- astropy
- matplotlib
- jupyter
- scipy
- f90nml
- yt
- yt_astro_analysis # install with pip
- colossus          # install with pip
- osyris            # install with pip

# libraries (used by some third-party codes, e.g. MUSIC, DICE, ... )
- fftw
- gsl
- ffmpeg
```

### General environment 
You will need `git` to download RAMSES and other codes used in the tutorials. Compilation will require using `make` (for RAMSES) and `cmake` for third-party codes. You should also install `pip` to be able to install python packages (see below). 

### Compilers
You will need a **fortran compiler** to compile RAMSES, along with some version of **MPI** if you have access to multiple cores and want to run RAMSES in parallel. We recommend installing recent versions of the GNU fortran compiler [gfortran](https://gcc.gnu.org/fortran/) and [openmpi](https://www.open-mpi.org/). 
 
 For some third-party codes, you will also need recent versions of **C and C++ compilers** (at least C++14 compliant). We again recommend using [gcc/gxx](https://gcc.gnu.org/)

### python
The tutorials come in the form of python notebooks that the user can execute and modify. In order to run these you need at least the following basic python packages installed with your standard package installer.
```
- python=3.12  
- numpy
- astropy
- matplotlib
- jupyter
- scipy
- f90nml
``` 
On top of thes general packages we will use more astro-specific packages to visualize and analyze data. These are the following packages that can be installed with `pip`:
```
- yt
- yt_astro_analysis
- colossus
- osyris
```

### libraries
Some third-party codes used in the tutorials require the following libraries: 
- FFTW, which should be installed from the [fftw website](http://www.fftw.org). 
- GSL, which should be installed from the [GSL
  website](lhttp://www.gnu.org/software/gsl/). 
- FFMPEG will be used to generate videos.


## 2. Conda Setup 

The instructions below have been tested to some extent but cause trouble on some recent Macs (with the M* chips).

### 2.1. install miniconda
Install miniconda by following instructions provided on their website
[https://docs.anaconda.com/miniconda](https://docs.anaconda.com/miniconda). (See
e.g. the quick command line install at the bottom of the page: select
your OS and copy paste the commands into a terminal.)

For example, with **MacOS**, run the following commands in a terminal:
```
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
conda update -n base conda
```

Or on **Linux**, run these commands in a terminal:
```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
conda update -n base conda
```

**After this, close the terminal.**

### 2.2. Download the ramses tutorials repository
Open a new terminal and type the following:
```
git clone https://github.com/blaizot/ramses-tutorials.git
```
This will create a new directory `ramses-tutorials` which contains the tutorials and environment specifications. 

### 3. Install required python packages

In order to install all the packages we need, type the following:
```
conda env create -f ramses-tutorials/doc/source/Setup/ramses-environment.yml
```
Now, the conda environment for the ramses tutorials is created, as you can see by typing `conda env list`. In order to **use** the ramses environment, you have to **activate** it by running following command:
```
conda activate ramses-env
```
**Note that this has to be done in any new terminal.** (You may add this line to your .bashrc file if you are familiar with this, so that you don't have to type in the command each time you open a new terminal).  

Once you activate the conda environment `ramses-env` in a terminal, all packages listed in the file `ramses-tutorials/doc/source/Setup/ramses-environment.yml` become available. You can have a look at this file and edit it if need be. 

Finish the installation with some additional packages best installed with pip by running the following commands:
```
pip install yt_astro_analysis
pip install colossus
pip install osyris
```
### 2.4. Compiling third-party libraries

Some tutorials will use extra codes in order to generate initial conditions for RAMSES experiments. Follow the instructions below to install them according to your needs. 

#### MUSIC (v2)
In some tutorials (Cosmological-Volumes), we will use the code
MUSIC (v2). Install MUSIC2 as follows, in some terminal:
```
git clone https://github.com/cosmo-sims/MUSIC2.git
cd MUSIC2
mkdir build
cd build
ccmake ..
```
This last command will open an interactive session where you need to
enter `c` to start the configuration, `e` to exit the log, `c` again, and then `g` to generate the Makefile. Once this is done
successfully, type:
```
make -j
```

#### DICE
Some tutorials (e.g. Idealised galaxies) will use [DICE](https://bitbucket.org/vperret/dice/src/master/). Install this by running the following lines in a terminal.
```
git clone https://bitbucket.org/vperret/dice
cd dice
mkdir build
cd build
cmake -DCMAKE_C_FLAGS=-fcommon ..
make
make install
```


