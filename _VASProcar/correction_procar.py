
import os

###################################################

print(" ")

procar_old = open("PROCAR", "r")
procar_new = open("PROCAR_New1", "w")

for line in procar_old:
    # replacing the string and write to output file
    procar_new.write(line.replace('-0.', ' -0.'))
	
procar_old.close()
procar_new.close()

porc = (1/11)*100; porc = int(porc)
print(f'Aplicando Correcao ({porc}%)')

###################################################

procar_old = open("PROCAR_New1", "r")
procar_new = open("PROCAR_New2", "w")

for line in procar_old:
    # replacing the string and write to output file
    procar_new.write(line.replace('0-', '0 -'))    

procar_old.close()
procar_new.close()

os.remove("PROCAR_New1")

porc = (2/11)*100; porc = int(porc)
print(f'Aplicando Correcao ({porc}%)')

###################################################

procar_old = open("PROCAR_New2", "r")
procar_new = open("PROCAR_New3", "w")

for line in procar_old:
    # replacing the string and write to output file
    procar_new.write(line.replace('1-', '1 -'))    

procar_old.close()
procar_new.close()

os.remove("PROCAR_New2")

porc = (3/11)*100; porc = int(porc)
print(f'Aplicando Correcao ({porc}%)')

###################################################

procar_old = open("PROCAR_New3", "r")
procar_new = open("PROCAR_New4", "w")

for line in procar_old:
    # replacing the string and write to output file
    procar_new.write(line.replace('2-', '2 -'))    

procar_old.close()
procar_new.close()

os.remove("PROCAR_New3")

porc = (4/11)*100; porc = int(porc)
print(f'Aplicando Correcao ({porc}%)')

###################################################

procar_old = open("PROCAR_New4", "r")
procar_new = open("PROCAR_New5", "w")

for line in procar_old:
    # replacing the string and write to output file
    procar_new.write(line.replace('3-', '3 -'))    

procar_old.close()
procar_new.close()

os.remove("PROCAR_New4")
porc = (5/11)*100; porc = int(porc)
print(f'Aplicando Correcao ({porc}%)')

###################################################

procar_old = open("PROCAR_New5", "r")
procar_new = open("PROCAR_New6", "w")

for line in procar_old:
    # replacing the string and write to output file
    procar_new.write(line.replace('4-', '4 -'))    

procar_old.close()
procar_new.close()

os.remove("PROCAR_New5")

porc = (6/11)*100; porc = int(porc)
print(f'Aplicando Correcao ({porc}%)')

###################################################

procar_old = open("PROCAR_New6", "r")
procar_new = open("PROCAR_New7", "w")

for line in procar_old:
    # replacing the string and write to output file
    procar_new.write(line.replace('5-', '5 -'))    

procar_old.close()
procar_new.close()

os.remove("PROCAR_New6")

porc = (7/11)*100; porc = int(porc)
print(f'Aplicando Correcao ({porc}%)')

###################################################

procar_old = open("PROCAR_New7", "r")
procar_new = open("PROCAR_New8", "w")

for line in procar_old:
    # replacing the string and write to output file
    procar_new.write(line.replace('6-', '6 -'))    

procar_old.close()
procar_new.close()

os.remove("PROCAR_New7")

porc = (8/11)*100; porc = int(porc)
print(f'Aplicando Correcao ({porc}%)')

###################################################

procar_old = open("PROCAR_New8", "r")
procar_new = open("PROCAR_New9", "w")

for line in procar_old:
    # replacing the string and write to output file
    procar_new.write(line.replace('7-', '7 -'))    

procar_old.close()
procar_new.close()

os.remove("PROCAR_New8")

porc = (9/11)*100; porc = int(porc)
print(f'Aplicando Correcao ({porc}%)')

###################################################

procar_old = open("PROCAR_New9", "r")
procar_new = open("PROCAR_New10", "w")

for line in procar_old:
    # replacing the string and write to output file
    procar_new.write(line.replace('8-', '8 -'))    

procar_old.close()
procar_new.close()

os.remove("PROCAR_New9")

porc = (10/11)*100; porc = int(porc)
print(f'Aplicando Correcao ({porc}%)')

###################################################

procar_old = open("PROCAR_New10", "r")
procar_new = open("PROCAR_New11", "w")

for line in procar_old:
    # replacing the string and write to output file
    procar_new.write(line.replace('9-', '9 -'))    

procar_old.close()
procar_new.close()

os.remove("PROCAR_New10")

porc = (11/11)*100; porc = int(porc)
print(f'Aplicando Correcao ({porc}%)')

###################################################

os.rename('PROCAR', 'PROCAR.Original')
os.rename('PROCAR_New11', 'PROCAR')

print(" ")
print("==================== Concluido ====================")

###################################################
