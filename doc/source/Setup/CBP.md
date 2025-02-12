# Instructions to get started on the CBP machines

For the 1st edition of the RAMSES school, participants are hosted by the Centre Blaise Pascal ([CBP](http://www.cbp.ens-lyon.fr/doku.php?id=accueil:cbp)) and given access to individual desktop machines and to a more powerful cluster. 

These machines are provided with a number of installed softwares and libraries, but we will need a few extra things (python libraries) to go through the turorials. Please follow the instructions below in order to be able to execute the tutorials on the CBP servers. 

## 1. Install miniconda

Install miniconda by running the following commands in a new terminal:
```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```
After this, **close the terminal**.

## 2. Download the ramses tutorials repository
Open a new terminal and type the following:
```
git clone https://github.com/blaizot/ramses-tutorials.git
```

## 3. Install required python packages

In order to install all packages we need, type the following:
```
cd ramses-tutorials/doc/source/Setup
conda update -n base conda
conda env create -f ramses-environment-cbp.yml
```
Now, the conda environment for the ramses tutorials is created, as you can see by typing `conda env list`. In order to **use** the ramses environment, you have to **activate** it by running following command:
```
conda activate ramses-env
```
**Note that this has to be done in any new terminal.** (You may add this line to your .bashrc file if you are familiar with this).  

Finish the installation with some additional packages best installed with pip by running the following commands:
```
pip install yt_astro_analysis
pip install colossus
pip install osyris==2.11
```

## 4. Compiling third-party libraries

Some tutorials will use extra codes in order to generate initial conditions for RAMSES experiments. Follow the instructions below to install them according to your needs. 

### MUSIC (v2)
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

### DICE
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


