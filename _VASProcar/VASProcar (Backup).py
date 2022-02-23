print (" ")
print ("###############################################################")
print ("## VASProcar v1.0.32 (23/02/2022)                            ##")
print ("## https://github.com/Augusto-Dlelis/VASProcar-Tools-Python  ##")
print ("###############################################################")
print ("## Autores: ================================================ ##")
print ("## ========================================================= ##")
print ("## Augusto de Lelis Araujo --------------------------------- ##")
print ("## Federal University of Uberlandia (Uberlandia/MG - Brazil) ##")
print ("## e-mail: augusto-lelis@outlook.com ----------------------- ##")
print ("## ========================================================= ##")
print ("## Renan da Paixão Maciel ---------------------------------- ##")
print ("## Uppsala University (Uppsala/Sweden) --------------------- ##")
print ("## e-mail: renan.maciel@physics.uu.se ---------------------- ##")
print ("###############################################################")
print (" ")

print ("###############################################################")
print ("## Arquivos básicos: CONTCAR, OUTCAR e PROCAR -------------- ##")
print ("## Dependendo do calculo: DOSCAR, LOCPOT ou WAVECAR -------- ##")
print ("###############################################################")
print (" ")

print ("###############################################################")
print ("## Observacao: --------------------------------------------- ##")
print ("## Alguma configuracoes do codigo podem ser alteradas no     ##")
print ("## arquivo ''_configuracoes.py'', como por exemplo o formato ##")
print ("## de saida (.png, .pdf, .eps) dos Plot via Matplotlib       ##")
print ("###############################################################")
print (" ")

import os

#--------------------------------------------------------------------------------------------------------------
# Caso queira modificar a localização da pasta "_VASProcar", informe abaixo o novo diretório, como por exemplo:
# Diretorio = 'C:\Program Files\_VASProcar'
#--------------------------------------------------------------------------------------------------------------
Diretorio = '_VASProcar'  # Diretorio = '_VASProcar'

#----------------------------------------------------------------------
# Lendo as configurações gerais e executando o VASProcar --------------
#----------------------------------------------------------------------
executavel = Diretorio + '/_configuracoes.py'
exec(open(executavel).read())
#--------------------------------------------

#######################################################################
#######################################################################
#######
####### FIM DO CÓDIGO #################################################
#######
#######################################################################
#######################################################################
