from setuptools import setup, find_packages  # You aways need setuptools

packages = find_packages()  # self explanitory

setup(name='magicsmoke',  # name of your package (insert yours here)
      packages=packages,
      package_dir={'': 'src'},  # entry point to your package, this should be src
      zip_safe=False,  # can't run the package from a zip file (you can change this if you need)
      package_data={'magicsmoke': ['assets/*']})  # make your assests, or data sets etc stored in src/magicsmoke/assets, discoverable to the package user
