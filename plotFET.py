import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import pathlib
import subprocess
from array import *
import sys
import os.path
from os import path

# Data for plotting
#cwd = pathlib.Path(__file__).resolve().parent
cwd = pathlib.Path(str(sys.argv[1]))

fig = plt.figure()
fig.suptitle(str(cwd), fontsize=16)

## Output
if os.path.isfile(cwd / 'output.xls'):
    outputsettings = pd.read_excel(cwd / 'output.xls',sheet_name="Settings")
    outputgatevnos = outputsettings.iloc[21][2]
    outputdata = pd.read_excel(cwd / 'output.xls',sheet_name="Data")
    outputdatatotrows, outputdatatotcols = outputdata.shape
    x1 = [ [9e9]*1 for i in range(int(outputgatevnos))]
    y1 = [ [9e9]*1 for i in range(int(outputgatevnos))]
    for idx in range(int(outputgatevnos)): 
        outputdatacol1 = 'DrainV('+str(idx+1)+')'
        outputdatacol1beg = 1
        outputdatacol1end = int(outputdatatotrows)
        outputdatacol2 = 'DrainI('+str(idx+1)+')'
        outputdatacol2beg = 1
        outputdatacol2end = int(outputdatatotrows)
        x1[idx] = outputdata[outputdatacol1].values[outputdatacol1beg:outputdatacol1end]
        y1[idx] = outputdata[outputdatacol2].values[outputdatacol2beg:outputdatacol2end]

    # Setup the output plot
    ax = fig.add_subplot(2, 2, 1)
    for idx in range(int(outputgatevnos)): 
        ax.plot(-1*x1[idx], -1*y1[idx])
    ax.set(xlabel='Drain Voltage') 
    ax.set(ylabel='Drain Current')
    ax.set(title='Output Plot')
    ax.tick_params(top=True, right=True, labeltop=False, labelright=False, which='both', direction = 'in', length = 5, width = 2, labelsize = 15)
    plt.ticklabel_format(axis="y", style="sci", scilimits=(-6,-6), useMathText=True, useOffset=True)

## Transfer-lin
if os.path.isfile(cwd / 'transfer-lin.xls'):
    tranlindata = pd.read_excel(cwd / 'transfer-lin.xls',sheet_name="Data")
    tranlindatatotrows, tranlindatatotcols = tranlindata.shape
    tranlindatacol1 = 'GateV'
    tranlindatacol1beg = 1
    tranlindatacol1end = int(tranlindatatotrows)
    tranlindatacol2 = 'DrainI'
    tranlindatacol2beg = 1
    tranlindatacol2end = int(tranlindatatotrows)
    x2 = tranlindata[tranlindatacol1].values[tranlindatacol1beg:tranlindatacol1end]
    y2 = tranlindata[tranlindatacol2].values[tranlindatacol2beg:tranlindatacol2end]

    # Setup the Transfer-lin plot
    ax = fig.add_subplot(2, 2, 2)
    ax.plot(-1*x2, -1*y2)
    ax.set(xlabel='Gate Voltage') 
    ax.set(ylabel='Drain Current')
    ax.set(title='Transfer Plot - Linear Regime')
    ax.tick_params(top=True, right=True, labeltop=False, labelright=False, which='both', direction = 'in', length = 5, width = 2, labelsize = 15)
    plt.ticklabel_format(axis="y", style="sci", scilimits=(-6,-6), useMathText=True, useOffset=True)

## Transfer-sat
if os.path.isfile(cwd / 'transfer-sat.xls'):
    transatdata = pd.read_excel(cwd / 'transfer-sat.xls',sheet_name="Data")
    transatdatatotrows, transatdatatotcols = transatdata.shape
    transatdatacol1 = 'GateV'
    transatdatacol1beg = 1
    transatdatacol1end = int(transatdatatotrows)
    transatdatacol2 = 'DrainI'
    transatdatacol2beg = 1
    transatdatacol2end = int(transatdatatotrows)
    x3 = transatdata[transatdatacol1].values[transatdatacol1beg:transatdatacol1end]
    y3 = transatdata[transatdatacol2].values[transatdatacol2beg:transatdatacol2end]

    # Setup the Transfer-sat plot
    ax = fig.add_subplot(2, 2, 3)
    ax.plot(-1*x3, -1*y3)
    ax.set(xlabel='Gate Voltage') 
    ax.set(ylabel='Drain Current')
    ax.set(title='Transfer Plot - Saturation Regime (Linear Scale)')
    ax.tick_params(top=True, right=True, labeltop=False, labelright=False, which='both', direction = 'in', length = 5, width = 2, labelsize = 15)
    plt.ticklabel_format(axis="y", style="sci", scilimits=(-6,-6), useMathText=True, useOffset=True)

    ax = fig.add_subplot(2, 2, 4)
    ax.plot(-1*x3, -1*y3)
    ax.set(xlabel='Gate Voltage') 
    ax.set(ylabel='Drain Current')
    ax.set(title='Transfer Plot - Saturation Regime (Logarithmic Scale)')
    ax.tick_params(top=True, right=True, labeltop=False, labelright=False, which='both', direction = 'in', length = 5, width = 2, labelsize = 15)
    ax.set_yscale('log')



# # Show and save the plot
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.tight_layout()
plt.show()
# expfilename = 'plot1.pdf'
# fig.savefig(cwd / 'Exported-plots' / expfilename, bbox_inches="tight")
# subprocess.Popen([cwd / 'Exported-plots' / expfilename],shell=True)
