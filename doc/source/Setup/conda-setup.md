# Setting up a complete environment with conda

Install miniconda by following instructions provided on their website
[https://docs.anaconda.com/miniconda](https://docs.anaconda.com/miniconda). (See
e.g. the quick command line install at the bottom of the page: select
your OS and copy paste the commands into a terminal.)

For example, with MacOS, run the following commands in a terminal:
```
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

Or on Linux, run these commands in a terminal:
```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

After this, close the terminal.

## Installing compilers and python packages 

In order to install all packages that are required by the turorials, open a new terminal and type the following commands in your rascas-tutorials directory:
```
cd doc/source/Setup
conda update -n base conda
conda env create -f ramses-environment.yml
```
Now, the conda environment for the ramses tutorials is created, as you can see by typing `conda env list`. In order to use the ramses environment, you have to *activate* it by running following command:
```
conda activate ramses-env
```
Note that this has to be done in any new terminal. 

Finish the installation with some additional packages best installed with pip by running the following commands:
```
pip install yt_astro_analysis
pip install colossus
pip install osyris
```

## Compiling third-party libraries

### MUSIC
In some tutorials (Cosmological-Volumes), we will use the code
MUSIC. This can be tricky to compile with the conda setup above. The
instructions below should work out. 

```
git clone https://bitbucket.org/ohahn/music.git
cd music
make CC=$CONDA_PREFIX/bin/clang++ LPATHS="-L$CONDA_PREFIX/lib -Wl,-rpath,$(CONDA_PREFIX)/lib" CPATHS="-I$CONDA_PREFIX/include -I./src" HAVEHDF5=no
```
### DICE 


