
print ("##############################################################")
print ("## Digite o nome do arquivo a ser corrigido: ============== ##")
print ("## Por exemplo: PROCAR, DOSCAR, PARCHG, OUTCAR ============ ##")
print ("##############################################################") 
print ("Exemplos das correcoes aplicadas =============================")
print ("0.50000000-0.50000000   >>   0.50000000 -0.50000000")
print ("0.12345000-123   >>   0.12345000E-123")
print ("0.86000000-209   >>   0.86000000E-209")
print ("##############################################################") 
name = input (" "); name = str(name)
print (" ")

print ("...................")
print ("... Corrigindo ... ")
print ("...................")
print (" ")

import os

#---------------------------------------------------------------------------

file_old = open(name, "r")
file_new = open(name + '_New1', "w")

for line in file_old: file_new.write(line.replace('-0.', ' -0.'))

file_old.close()
file_new.close()

porc = (1/11)*100; porc = int(porc)
print(f'Aplicando Correcao ({porc}%)')

#---------------------------------------------------------------------------

for i in range (1,(10+1)):
    file_old = open(name + '_New' + str(i), "r")
    file_new = open(name + '_New' + str(i+1), "w")
    
    for line in file_old: file_new.write(line.replace(str(i-1) + '-', str(i-1) + ' -'))
    
    file_old.close()
    file_new.close()

    os.remove(name + '_New' + str(i))

    porc = ((i+1)/11)*100; porc = int(porc)
    print(f'Aplicando Correcao ({porc}%)')

#---------------------------------------------------------------------------

os.rename(name, name + '.Original')
os.rename(name + '_New11', name)

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------
