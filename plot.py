import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import pathlib
import subprocess

# Data for plotting

cwd = pathlib.Path(__file__).resolve().parent

set1 = pd.read_excel(cwd / 'Data' / 'Set1' / 'transfer-sat.xls')
set1totrows, set1totcols = set1.shape
set1col1 = 'GateV'
set1col1beg = 1
set1col1end = int(set1totrows/2)
set1col2 = 'DrainI'
set1col2beg = 1
set1col2end = int(set1totrows/2)
x1= set1[set1col1].values[set1col1beg:set1col1end]
y1= set1[set1col2].values[set1col2beg:set1col2end]

set2 = pd.read_excel(cwd / 'Data' / 'Set2' / 'transfer-sat.xls')
set2totrows, set2totcols = set2.shape
set2col1 = 'GateV'
set2col1beg = 1
set2col1end = int(set2totrows/2)
set2col2 = 'DrainI'
set2col2beg = 1
set2col2end = int(set2totrows/2)
x2= set2[set2col1].values[set2col1beg:set2col1end]
y2= set2[set2col2].values[set2col2beg:set2col2end]

set3 = pd.read_excel(cwd / 'Data' / 'Set3' / 'transfer-sat.xls')
set3totrows, set3totcols = set3.shape
set3col1 = 'GateV'
set3col1beg = 1
set3col1end = int(set3totrows/2)
set3col2 = 'DrainI'
set3col2beg = 1
set3col2end = int(set3totrows/2)
x3= set3[set3col1].values[set3col1beg:set3col1end]
y3= set3[set3col2].values[set3col2beg:set3col2end]

# Setup the plot
fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.plot(x2, y2)
ax.plot(x3, y3)
ax.set(xlabel='GateV') 
ax.set(ylabel='DrainI')
ax.tick_params(top=True, right=True, labeltop=False, labelright=False, which='both', direction = 'in', length = 5, width = 2, labelsize = 15)
plt.ticklabel_format(axis="y", style="sci", scilimits=(-6,-6), useMathText=True, useOffset=True)


# Show and save the plot
expfilename = 'plot1.pdf'
plt.tight_layout()
fig.savefig(cwd / 'Exported-plots' / expfilename, bbox_inches="tight")
subprocess.Popen([cwd / 'Exported-plots' / expfilename],shell=True)
#plt.show()