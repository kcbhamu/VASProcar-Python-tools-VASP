
print ("##############################################################")
print ("## Digite o nome do arquivo a ser corrigido: ============== ##")
print ("## Por exemplo: PROCAR, DOSCAR, PARCHG, OUTCAR ============ ##")
print ("##############################################################") 
print ("Exemplos das correcoes aplicadas =============================")
print ("0.50000000-0.50000000   >>   0.50000000 -0.50000000")
print ("0.12345000-123   >>   0.12345000e-123")
print ("0.86000000-209   >>   0.86000000e-209")
print ("##############################################################") 
name = input ("name: "); name = str(name)
print (" ")

print ("..................")
print ("... Corrigindo ...")
print ("..................")
print (" ")

#---------------------------------------------------------------------------

original = name
copia    = name + '_Original'
shutil.copyfile(original, copia)

#---------------------------------------------------------------------------

with open(name, 'rt') as file:
     r = file.read()

for i in range (10):     
    with open(name, 'wt') as file:
         r = r.replace('-' + str(i) + '.', ' -' + str(i) + '.')
         file.write(r)

for i in range (10):     
    with open(name, 'wt') as file:
         r = r.replace(str(i) + '-', str(i) + 'e-')
         file.write(r)

file.close()

#-----------------------------------------------------------------
print("======================= Concluido =======================")
#-----------------------------------------------------------------
