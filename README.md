# Magic Smoke

"Magic Smoke" refers to the smoke which is installed in all electrical components, and is essential for them working correctly. You will usually hear it refered to by a sad Huntsman student who just blew up something up: "%@!# the magic smoke is escaping!" Once the magic smoke has escaped, the electrical component will no longer work (unless you purchase a magic smoke refill from IBM) 

This is a skeleton package for you to develop your own classes and packages based on my learnings from Huntsman. I hope these learnings are the magic smoke that makes your code, and your work flow a little easier and faster.  

I'd like to reiterate however, there is no right or wrong way to do any of this. Expore, try new things, and enjoy having the freedom of being able to code however you like! Often our adversion to coding tools, operating systems, IDE's etc, stems from the fact we simply don't understand how they work just yet!  

## Byobu

Byobu is useful for those who often have lots of terminals open to do lots of processes, those who need to work on machines remotely, working on hardware in headless mode (no monitor) or if you want to close the window, but keep the process running (in particular flaking VPN's, bad connections etc, but you want the process to keep running even if you detatch from the bash terminal). 

#### Installing on OSX:

If you need to install homebrew:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then:
```
brew install byobu 
```

If you are running 10.14.3 or lower (because, reasons) you may also need to install:

```
brew install coreutils
```

#### Installing on Linux:

```
sudo apt-get install byobu
```

#### Installing on Windows:

```
Coming soon! Sorry Windows friends :(
```

Byobu is a **STEEP** learning curve, but it is worth it! A really good byobu cheat sheet can be found [here](https://medium.com/russian-it-stories/byobu-cheatsheet-%D0%BCost-used-hotkeys-5a8bbd8476fd)

## Environments 

I think of environments like rooms in your house. You wouldn't cook in the bathroom? Or sleed in the garage? A particular room in the house has all the tools you need for certain tasks. So make sure you are developing code in the right room!

In short, the envirnment holds all your packages, python versions etc for a particular project. Examples for me, are `Huntsman`, `SkyHopper`, `PRAXIS` and `SkySurf`, four of the projects I am working on, that have their own, unique coding envirnments. 

#### Getting started:

As a python developer, I prefer to use conda - and there are lots of way install it. If you are just starting out, or if you like GUI's (there is absolutly no proplem with this, I like visual tools as well) it is a good idea to install [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/#:~:text=Anaconda%20Navigator%20is%20a%20desktop,in%20a%20local%20Anaconda%20Repository.).

Installation of Anaconda, both the graphical interface and conda the command line interface on all operating systems can be found [here](https://docs.anaconda.com/anaconda/install/).

If you'd like a quick start command line option, on a Mac you can do:

```
pip install conda
```

The major commands for environment management are:

```
conda create --name myenv
```
Where `myenv` is replaced with the name of your environment. Tips on how to make environments with certain packages installed, and specific python environments, check out [these docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

```
source activate myenv
```
This will activate your environment in a bash terminal

```
conda deactivate
```
This will deactivate any environments currently in use, and take you back to `base`.

```
conda info --envs
```
This will list all the environments on your machine. 

## Docstrings

These are great if you leave your code for a few months, come back and forget how to use a function or class! You can also call `help()` on an object, function/method etc, and it will show you your docstrings. I use the google standard, which you can find [here](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html). 

## Classes 

## Packages 

## Installing Packages 

Once you have created your package, make sure you are in the environment you want to install it in. Then, navigate to the top directory of the package. 

Once here, install the dependacies by running:

```
pip install -r requirements.txt
```

Then you want to install you package in a dynamic way (in otherwords, you can edit it as you go, and those changes will be automatically linked to the installed version) 

```
python setup.py develop
```

If you want to install it in a static way, you can do:

```
python setup.py install 
```

You should now be able to import your package and it's modules for use in the everyday world!

## Licenses

I know it sucks to think about these sort of things, but they are important. Make sure you pick the correct license when you start up a repo on github. MIT liceses are usualy the way to go, as it ensures you are not liable for any issues that people using your code may encounter. In this example, I've included an MIT license. Read more about it [here](https://opensource.org/licenses/MIT).

## .gitignore

This is a handy little file that includes everything that you don't want git to pick up on and push up to your remote origin. Things that come to mind for Mac users are those frustrating `.DS_Store` files. Also, **IP Addresses** inside config files and other things like this. BTW, if you are dealing with things like this often, you might want to make your repo private, and the make it public after you are 100% sure there is nothing that shouldn't be there. 





