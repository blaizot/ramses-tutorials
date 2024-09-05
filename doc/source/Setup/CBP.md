# Instructions to get started on the CBP machine

For the 1st edition of the RAMSES school, participants are granted access to the Centre Blaise Pascal ([CBP](http://www.cbp.ens-lyon.fr/doku.php?id=accueil:cbp)) machine.

The following instructions will guide you to obtain, compile and run the RAMSES code in parallel on the CBP machine, but they can be adapted for the use of any other HPC environment. If you want to use your own laptop, you can refer to the **Instructions to get started on your laptop** section.
<!-- Make link instead of bold text-->

## Getting RAMSES

In order to **obtain and compile the RAMSES code**, please follow the first steps of the documentation at [this link](https://ramses-organisation.readthedocs.io/en/latest/wiki/Start.html). You will also find information about the content of the RAMSES repository and some (old) instructions about compiling the code.

## Compilers

You will need a **fortran compiler** to compile RAMSES, along with some version of **MPI** if you want to run RAMSES in parallel.

On a supercomputer, fortran compilers and MPI libraries will generally be installed and you need to find out how to use them. Often, this is done by loading modules. Once logged to the supercomputer, you can check what are the possible modules already installed by running the following command in the terminal:

```bash
module spider
```

You can then load the modules needed via:

```bash
module load name-of-the-module
```

On the CBP machine, you can simply copy the following lines to load the GCC (gfortran) compiler and OpenMPI:

```bash
module purge
module use /applis/PSMN/debian11/Cascade/modules/all
module load OpenMPI/4.1.1-GCC-10.3.0
```

**IMPORTANT NOTE: I (Marion) copied what I use on the PSMN, this might need to be changed for the CBP machine?**

## Environment and data visualisation with python

Explain here how to create a python environment and install the packages needed for the tutorials?

We use notebooks for these tutorials (`.ipynb` extensions) to use both Python code and Markdown in the same file. Notebook use kernels to run code (upper right of the visualiser). To use the Notebook, you can run a cell with <kbd>Ctrl</kbd>+<kbd>Enter</kbd>, navigate between cells with <kbd>↑</kbd> and <kbd>↓</kbd>, create new cells above (resp. below) with <kbd>A</kbd> (resp. <kbd>B</kbd>), and delete them with <kbd>D</kbd><kbd>D</kbd>