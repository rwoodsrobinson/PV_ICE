#!/usr/bin/env python
# coding: utf-8

# # 0 - quickStart Example
# ***

# This notebook will guide you through the basic functionality of PV_ICE. Once you are done with this tutorial, you will be able to:
# * Set up a PV_ICE simulation and create scenarios.
# * Compute Mass and Energy flows calculations.
# * Plot results.
# 
# Please refer to the [PV_ICE documentation page](https://pv-ice.readthedocs.io/en/latest/index.html) to get a complete insight of the package.

# ## 0.1 &emsp; Simulation Setup <a id='0.1'></a>

# To setup a PV_ICE simulation we need (1) import necessary packages, (2) create simulation folder path, (3) create a baseline path.
# 
# First let's import the necessary libraries for this notebook:

# In[1]:


import os # Creates and removes a directory (folder), fetch its contents, change and identify the current directory
from pathlib import Path
import PV_ICE # Load PV_ICE package

print("Successfully imported PV_ICE, version ", PV_ICE.__version__)


# #### 1. Create a folder for your simulation, and load PV ICE
# 
# Let's set the folder where the **simulation** will be saved. By default, this is the TEMP folder in the PV_ICE distribution, however, we have created a TEMP folder in the present folder for simplicity.
# 
# <div class="alert alert-block alert-info">
# <b>Tip:</b> The lines below find the location of the folder relative to this Jupyter Journal, where `Path().resolve()` points at the current notebook absolute location, add `.parent` to navigate to previous folders and `/ 'folder' / ...` to navigate within a specific folder.. You can alternatively point to an empty directory (it will open a load GUI Visual Interface) or specify any other directory in your computer.
# </div>
# 
# 
# Using the same logic, setup the **baselines** folder. This is where all the baselines are stored in .csv format. A folder with multiple baselines can be found in the PV_ICE repository (PV_ICE/PV_ICE/baselines), you can always copy this folder and put it in a path of your choice. You may also create your own baselines (following the key structure used in PV_ICE for scenarios and materials).

# In[2]:


testfolder = str(Path().resolve() / 'TEMP') # Path to the simulation folder.

baselinesfolder = str(Path().resolve().parent.parent.parent / 'PV_ICE' / 'baselines')  # Path to baselines and data.

# Another option using relative address; for some operative systems you might need '/' instead of '\'
# testfolder = os.path.abspath(r'..\..\PV_DEMICE\TEMP')  

print ("Your simulation will be stored in %s" % testfolder)
print ("Your baselines are stored in %s" % baselinesfolder)


# ## 0.2.  Create Simulation Object <a id='0.2'></a>
# 

# The simulation object will create a container for all the different scenario(s) you might want to test. The method Simulation requires two inputs:
# * `name` for the simulation (in this example `'Simulation_1'`), if no name is given the program will autogenerate a default name with the current date
# * `path`, this is where we insert `testfolder` defined above, we named this simulation object `r1`

# In[3]:


wr0 = PV_ICE.Simulation(name='Simulation_1', path=testfolder); # Is it possible to define more than one simulation here?
print(r0.name) # Shows the name of the simulation object
print(r0.path) # Shows the path of the simulation object


# In[ ]:


r1 = PV_ICE.Simulation(name='Simulation1', path=testfolder)


# ### 3. Specify your baseline Scenario 
# 
# We have put together scenarios representing the average module for various situations, for example throughout the US history. We will load this baseline scenario now, and it will be named ``standard``:

# In[ ]:


r1.createScenario(name='standard', file=r'..\baselines\baseline_modules_US.csv')


# If a file is not provided, the automatic file loader will pop-up.
# 
# 
# 
# ### 4. Specify material(s)
# 
# We will add the material 'glass' to our simulation. Years of data must match, and they do if using the provided baselines.

# In[ ]:


r1.scenario['standard'].addMaterial('glass', file=r'..\baselines\baseline_material_glass.csv')


# ### 5. Run the Mass Flow with Circular Pathways Calculations

# In[ ]:


r1.calculateMassFlow()


# In[ ]:


r1.scenario['standard'].data.head()


# ###  6. Plot Mass Flow Results

# In[ ]:


r1.plotScenariosComparison(keyword='Cumulative_Area_disposedby_Failure')
r1.plotMaterialComparisonAcrossScenarios(material='glass', keyword='mat_EOL_Recycled_2_HQ')

