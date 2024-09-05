# Instructions to get started on your laptop

The following (non exhaustive!) set of instructions will guide you to obtain, compile and run the RAMSES code in parallel on your laptop. To use RAMSES on a cluster and an HPC environment, refer to the **Instructions to get started on the CBP machine** section. 
<!-- Make link instead of bold text-->



Here is a summary of requirements depending on the tutorial you are following. `RAMSES`, `python` and `notebook` are necessary for all tutorials, and you should have access to at least 8 Gb of memory and 2 cores.
<!-- Check for all tutos 8gb/2cores, this is for idealised -->
<div align="center">

Tutorial name           | yt | Osyris | DICE  | ffmpeg 
----------------------  | -- | ------ | ----- | ------
Idealised disc          | ✔  | ✖      | ✔     | ✔     
Cosmological simulation | ✔  | ✖      | ✖     | ✖     
Dense core collapse     | ✖  | ✔      | ✖     | ✖     
Turbulent box           | ✖  | ✔      | ✖     | ✖     
</div>
<!-- Make text link to the sections, cp paste to CBP version. -->

## 1. Getting RAMSES

In order to **obtain and compile the RAMSES code**, please follow the first steps of the documentation at [this link](https://ramses-organisation.readthedocs.io/en/latest/wiki/Start.html). You will also find information about the content of the RAMSES repository and some (old) instructions about compiling the code.

## 2. Compilers

You will need a **fortran compiler** to compile RAMSES, along with some version of **MPI** if you have access to multiple cores and want to run RAMSES in parallel.

We recommend installing recent versions of the GNU fortran compiler `gfortran` [(link)](https://gcc.gnu.org/fortran/) and `openmpi` [(link)](https://www.open-mpi.org/). 


## 3. Python - data visualisation
### 3.1 Python
For all tutorials, you will need to install python and several of its modules. To directly install Python and several common modules, you can install Anaconda or Miniconda (lighter version). For simplicity, we recommend the use of a [conda](https://www.anaconda.com) distribution. Otherwise, replace `conda install module` by `pip install module` in the following commands.


### 3.2 Notebooks
We use notebooks for these tutorials (`.ipynb` extensions) to use both Python code and Markdown in the same file. Install the python module with:
```bash
conda install notebook
```
If you use vscode, you will need to additionally download the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) (more information on VScode notebooks [here](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)). Notebook use kernels to run code (upper right of the visualiser). If you have different python versions, you might fail to install modules in the correct ones. In that case, you can run the command used to download/install the module in a notebook cell.   

To use the Notebook, you can run a cell with <kbd>Ctrl</kbd>+<kbd>Enter</kbd>, navigate between cells with <kbd>↑</kbd> and <kbd>↓</kbd>, create new cells above (resp. below) with <kbd>A</kbd> (resp. <kbd>B</kbd>), and delete them with <kbd>D</kbd><kbd>D</kbd>

### 3.3 The yt project
[yt](https://yt-project.org) is an open-source python package that we will use for analyzing and visualizing RAMSES data (it is also compatible with data from other astrophysical codes). To download and install the yt code, we recommend the use of conda:
```bash
conda install numpy matplotlib pandas scipy
conda install -c conda-forge yt
```
Alternatively, use pip:
```bash
conda install numpy matplotlib pandas scipy
python -m pip install --user yt
```

### 3.4 Osyris
TODO


## 4. Other libraries
To install the packages needed, you need a package manager such as `apt` for Ubuntu or `brew` for OSX. Refer to your respective operating system for more information. In the following, replace `sudo apt install package` by that of your OS (`sudo dnf install` or Fedora, `sudo pacman -S` for Arch Linux, or `brew install package` on OSX). 
<!-- Not relevant if on local...
On Note that in most cases, the use of sudo and apt is not allowed on supercomputers. Instead, load modules when already installed on the machine (e.g. for compilers), download and install packages with `git` and `make` when appliable, or contact a member of the supercomputer support service. -->


### 4.1 FFMPEG - processing images

[ffmpeg](https://www.ffmpeg.org) will be used for processing and assembling images into a movie. To download ffmpeg and install ffmpeg, do as follows:

  ```bash
  sudo apt install ffmpeg
  ```
<!-- No need to make it complicated
```bash
git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg
cd ffmpeg
./configure
make
make install
``` -->

### 4.2 [DICE](https://bitbucket.org/vperret/dice/src/master/) - initial conditions.  
[DICE](https://bitbucket.org/vperret/dice/src/master/) is used to generate initial conditions for galactic disk. To install DICE, you first need to install CMake, GSL and FFTW3. We do so and verify their proper installation with:
```bash
sudo apt install gsl cmake fftw        
gsl-config --version        
cmake --version        
brew list | grep fftw        
```

<!-- You can directly go to the "Compile & install section" of the [DICE instructions webpage](https://bitbucket.org/vperret/dice/wiki/Compile%20&%20Install), or simply follow the instructions below. -> Useless?? -->
Then, install DICE with:
```bash
git clone https://bitbucket.org/vperret/dice
cd dice
mkdir build
cd build
cmake ..
make
make install
```
If you encounter any problem, please refer to the [DICE instructions for installation](https://bitbucket.org/vperret/dice/wiki/Compile%20&%20Install). Depending on your C compiler version, you may need the following 'extra' parameters with cmake when installing: `cmake .. -DCMAKE_C_FLAGS="-fcommon"`. After installation, you should obtain a `dice` directory which contains the executable in `dice/build/bin/dice`.


<!-- I think this is WAY too much. We give them the simple version that works on all machines with known OS, otherwise they go check on internet, not hard.
### CMAKE

You can use apt or brew to install CMake:

```bash
sudo apt install cmake
```

And verify its proper installation with:

```bash
cmake --version
```

### FFTW3

- Download the source code of the library from the [fftw website](http://www.fftw.org)
- Open a terminal and expand the gzipped archive
- Run the configure script with the following parameters:
```bash
./configure --prefix=$HOME/local/ --enable-openmp --enable-float
```
where `$HOME/local` will install the library into a directory "local" inside of your home directory. You should set this to a directory that exists and where you are allowed to write files.
Add `--enable-float` if you want to compile for single precision; omit it if you want to compile for double precision. Omit `--enable-openmp` if you do not want to compile the multi-threaded version of the library.

- Compile and install the library
```bash
make install
```

- If you want to install both the single and double precision versions, repeat from step 3 and omit/add `--enable-float` when configuring in step 3 in order to compile also for double/single precision.

Alternatively, you can use apt or brew to install FFTW:

```bash
sudo apt install fftw
```

And verify its proper installation with:

```bash
brew list | grep fftw
```

### GSL

- Download the source code of the library from the [GSL website](lhttp://www.gnu.org/software/gsl/)

- Open a terminal and expand the gzipped tar archive.

- Run the configure script with the following parameters:
```bash
./configure --prefix=$HOME/local/
```
where `$HOME/local` will install the library into a directory "local" inside of your home directory. You should set this to a directory that exists and where you are allowed to write files.

- Compile and install the library
```bash
make install
```

Alternatively, you can use apt or brew to install GSL:

```bash
sudo apt install gsl
```

And verify its proper installation with:

```bash
gsl-config --version
```

### Brew (Mac)

If you want to install the package manager brew (Mac), see [their website](https://brew.sh) and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then run the command indicted in your terminal, that looks like:
```bash
(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/yourusername/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
```

Finally, install brew:
```bash
brew install gsl cmake fftw
``` -->

<!-- Internet, first link gives the answer, very easy, too much here.
### Git

Should you need to install git on your machine, you can refer to the following [link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). -->

<!-- Same, way too much: they should use https. If they know what they're doing they can use ssh. Not the appropriate place to explain it. We want a minimal working setup. They will be free to pull (public repo) and I think free tomerge request, but they shouldn't, they should raise issues and we fix them. Feels like a reminder for you, not something for the tuto.
### Cloning via HTTPS versus SSH

Codes hosted on Bitbucket or GitHub can be cloned via SSH or HTTPS, which are two different secure protocols for cloning repositories.

HTTPS:

HTTPS is the easier option: it does not require SSH keys, and is universally accessible. However, you will need to enter your credentials
(username and password of your Bitbucket or GitHub account) every time you want to push or pull any change made to the code you cloned.
```bash
git clone https://bitbucket.org/repo/thecode.git
```

SSH:

With SSH, you authenticate to the server without having to provide your credentials at each visit. However, if you want to clone via SSH, you will first need to generate and associate the SSH key of your machine to your (Bitbucket or GitHub) account, as follows.
```bash
git clone git@bitbucket.org:repo/thecode.git
```

- On your local machine, generate a new SSH key pair:
```bash
ssh-keygen -t rsa
``` 
You can specify a file location for the key and a passphrase for extra security. 

- Add your SSH public key (`id_rsa.pub`) to GitHub or BitBucket: in the web portal, sign in, navigate to Settings > SSH and GPG keys > New SSH key, and paste your public key. You can print the content of the public key with (change the following with the location of your .ssh directory if needed):
```bash
cat ~/.ssh/id_rsa.pub
``` -->
