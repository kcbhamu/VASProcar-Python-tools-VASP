
import os
import sys
import shutil

print(" ")
print("##########################################################################")
print("# VASProcar versão 1.0.77                                               ##")
print("# https://doi.org/10.5281/zenodo.6343960                                ##")
print("# https://github.com/Augusto-Dlelis/VASProcar-Tools-Python              ##")
print("##########################################################################")
print("# Autores:                                                              ##")
print("# ===================================================================== ##")
print("# Augusto de Lelis Araujo                                               ##")
print("# Federal University of Uberlandia (Uberlândia/MG - Brazil)             ##")
print("# e-mail: augusto-lelis@outlook.com                                     ##")
print("# ===================================================================== ##")
print("# Renan da Paixao Maciel                                                ##")
print("# Uppsala University (Uppsala/Sweden)                                   ##")
print("# e-mail: renan.maciel@physics.uu.se                                    ##")
print("##########################################################################")
print(" ")

print("###############################################################")
print("## Arquivos basicos para execucao: CONTCAR, OUTCAR e PROCAR  ##")
print("## Dependendo do calculo: DOSCAR, LOCPOT ou WAVECAR -------- ##")
print("###############################################################")   
print(" ")

dir_files = os.getcwd()

os.chdir(os.path.dirname(os.path.realpath(__file__)))

#----------------------------------------------------
# src directory to the main python codes ------------
#----------------------------------------------------

main_dir = 'src/'
run = main_dir + '_settings.py'
exec(open(run).read())
