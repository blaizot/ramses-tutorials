# Idealised Disc Galaxy

This tutorial will take you through the process of generating idealised disc simulations: 
- generation of initial conditions with DICE
- running different flavours of RAMSES (hydro, RHD, ...)
- running RASCAS ?
- ...
- 

# Dependencies
To install the different packages needed, you need a package manager such as `apt` for Ubuntu or `brew` for OSX. Refer to your respective operating system for more information. In the following, replace `sudo apt install package` by that of your OS (`sudo dnf install` or Fedora, `sudo pacman -S` for Arch Linux, or `brew install package` on OSX).

### **[DICE](https://bitbucket.org/vperret/dice/src/master/)** - initial conditions.   
To install DICE, you first need to install CMake, GSL and FFTW3. We do so and verify their proper installation with:
```bash
sudo apt install gsl cmake fftw        
gsl-config --version        
cmake --version        
brew list | grep fftw        
```

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
If you encounter any problem, please refer to the [DICE instructions for installation](https://bitbucket.org/vperret/dice/wiki/Compile%20&%20Install).

### **Python** - data visualisation
First you will need to install python and several of its modules. To directly install several common modules, you can install Anaconda or Miniconda. In that case, replace `pip install module` by `conda install module` in the following.
```bash
pip install notebook yt numpy matplotlib pandas scipy
```

We use notebooks for these tutorials (`.ipynb` extensions) to use both Python code and Markdown in the same file. If you use vscode, you will need to additionally download the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) (more information on VScode notebooks [here](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)). Notebook use kernels to run code (upper right of the visualiser). If you have different python versions, you might fail to install modules in the correct ones. In that case, you can run the command above in a notebook cell.   
To use the Notebook, you can run a cell with <kbd>Ctrl</kbd>+<kbd>Enter</kbd>, navigate between cells with <kbd>↑</kbd> and <kbd>↓</kbd>, create new cells above (resp. below) with <kbd>A</kbd> (resp. <kbd>B</kbd>), and delete them with <kbd>D</kbd><kbd>D</kbd>

### FFMPEG - processing images
  ```bash
  sudo apt install ffmpeg
  ```
