# Guidelines to develop RAMSES tutorials

## Style 

Python notebooks are handy for tutorials. Please make sure that your tutorial starts with a markdown cell containing the title of the tutorial after a single hash sign. For example 
```
# My New Tutorial
```
Then you should use markdown cells to structure the tutorial into sections and sub-sections, starting with `##` for sections, `###` for sub-sections, etc. For example: 
```
## 1. Pre-requisites 
### 1.1. compiling RAMSES with the right options ... 
```
This will help the table of contents look good in the overall documentation. 

Please, before pushing your tutorial to the common repo, make sure it works end-to-end. When you are happy with your tutorial, the best practice is to restart the kernel and clear all cells, then run cells one by one till the end, save the notebook, and commit this version. 


## Turning your tutorial into documentation with sphinx

Each tutorial is in the form of a notebook within a directory, for example `Cosmological-Volumes/tutorial.ipynb`. The global documentation consists of all the tutorials listed in the file `doc/source/index.rst`. If you create a new tutorial `MyNewTutorial/tutorial.ipynb`, you should first add a symbolic link of your tutorial's directory into the `doc/source` directory:
```
cd doc/source
ln -s ../../MyNewTutorial .
```
Then you should edit the file `doc/source/index.rst` to insert a line in the list of existing tutorials (mind the spaces), for example as follows:
```
   Cosmological-Volume/tutorial.ipynb
   Idealised-Disc-Galaxy/tuto_disc.ipynb
   MyNewTutorial/tutorial.ipynb
```

In order to generate the documentation on your side, before committing and pushing to github, you should first install the required sphinx packages:
```
cd doc
pip install -r rtd_requirements.txt
```
Once this is done you should run the following commnand:
```
cd doc
sphinx-build -M html source  build
```
This will generate a the file `doc/build/html/index.html` that you can open in your browser to check the results. Please make sure your tutorial appears OK on this before you push your developments. 

You can also generate a pdf file using the following commnand:
```
cd doc
sphinx-build -M latexpdf source  build
```
Again, please make sure this works before pushing. 

## Credits

If you provide a new tutorial, you should add your name and
contribution to the **Credits section** by editing the file `doc/source/credits.rst`.
