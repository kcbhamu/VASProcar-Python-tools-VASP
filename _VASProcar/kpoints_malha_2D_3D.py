#########################################################################################
## VASProcar -- https://github.com/Augusto-Dlelis/VASProcar-Tools-Python ################
## Autores: #############################################################################
## =================================================================================== ##
## Augusto de Lelis Araujo - Federal University of Uberlandia (Uberlândia/MG - Brazil) ##
## e-mail: augusto-lelis@outlook.com                                                   ##
## =================================================================================== ##
## Renan da Paixão Maciel - Uppsala University (Uppsala/Sweden) #########################
## e-mail: renan.maciel@physics.uu.se                           #########################
#########################################################################################

print("#######################################################")
print("## Gerador de arquivo KPOINTS (Plano 2D ou Malha 3D) ##")
print("#######################################################")
print(" ")

print("#######################################################")
print("## Que tipo de KPOINTS deseja gerar? ==============  ##")
print("#######################################################")
print("## [1] Plano 2D na Zona de Brolluin                  ##")
print("## [2] Malha 3D na Zona de Brolluin                  ##")
print("#######################################################")
tipo = input (" "); tipo = int(tipo)
print(" ")

print("#######################################################")
print("## Qual sistema de coordenadas quer adotar? =======  ##")
print("#######################################################")
print("## [1] Coordenadas Diretas (k1,k2,k3):               ##")
print("##     K =  k1*B1 + k2*B2 + k3*B3                    ##")
print("## [2] Coordenadas Cartesianas (kx,ky,kz)            ##")
print("##     K =  2pi/Param.(kx, ky, kz)                   ##")
print("#######################################################")
coord = input (" "); coord = int(coord)
print(" ")

if (coord == 1):
   ch1 = 'k1'; ch2 = 'k2'; ch3 = 'k3'
if (coord == 2):
   ch1 = 'kx'; ch2 = 'ky'; ch3 = 'kz'

print("#######################################################")
print("## Vetores Primitivos da Rede Reciproca:")
print(f'## B1 = 2pi/Param.({B1x}, {B1y}, {B1z})')
print(f'## B2 = 2pi/Param.({B2x}, {B2y}, {B2z})')
print(f'## B3 = 2pi/Param.({B3x}, {B3y}, {B3z})')
print(f'## Param. = {Parametro} Angs.')
print("#######################################################")
print(" ")   

if (tipo == 1):
   print("#######################################################")
   print("## Defina qual plano deseja varrer na ZB: ========== ##")
   print(f'## [1] Plano {ch1}{ch2} ({ch3} fixo) ======================== ##')
   print(f'## [2] Plano {ch1}{ch3} ({ch2} fixo) ======================== ##')
   print(f'## [3] Plano {ch2}{ch3} ({ch1} fixo) ======================== ##')
   print("#######################################################")
   esc = input (" "); esc = int(esc)
   print(" ")

print("#######################################################")
print("###### Defina as coordenadas a serem utilizadas: ######")
print("#######################################################")
print(" ")

if ((tipo == 1 and esc != 3) or (tipo == 2)):
   print(f'Valor inicial da coordenada {ch1}: ######################')
   c1_i = input (" "); c1_i = float(c1_i)
   print(f'Valor final da coordenada {ch1}: ########################')
   c1_f = input (" "); c1_f = float(c1_f)
   print(f'Qual e o Grid de pontos no eixo-{ch1}:###################')
   grid_1 = input (" "); grid_1 = int(grid_1)   
if (tipo == 1 and esc == 3):
   print(f'Valor da coordenada fixa {ch1}: #########################')
   c1_i = input (" "); c1_i = float(c1_i); c1_f = c1_i
   grid_1 = 1
print(" ")

if ((tipo == 1 and esc != 2) or (tipo == 2)):
   print(f'Valor inicial da coordenada {ch2}: ######################')
   c2_i = input (" "); c2_i = float(c2_i)
   print(f'Valor final da coordenada {ch2}: ########################')
   c2_f = input (" "); c2_f = float(c2_f)
   print(f'Qual e o Grid de pontos no eixo-{ch2}:###################')
   grid_2 = input (" "); grid_2 = int(grid_2)   
if (tipo == 1 and esc == 2):
   print(f'Valor da coordenada fixa {ch2}: #########################')
   c2_i = input (" "); c2_i = float(c2_i); c2_f = c2_i
   grid_2 = 1
print(" ")

if ((tipo == 1 and esc != 1) or (tipo == 2)):
   print(f'Valor inicial da coordenada {ch3}: ######################')
   c3_i = input (" "); c3_i = float(c3_i)
   print(f'Valor final da coordenada {ch3}: ########################')
   c3_f = input (" "); c3_f = float(c3_f)
   print(f'Qual e o Grid de pontos no eixo-{ch3}:###################')
   grid_3 = input (" "); grid_3 = int(grid_3)   
if (tipo == 1 and esc == 1):
   print(f'Valor da coordenada fixa {ch3}: #########################')
   c3_i = input (" "); c3_i = float(c3_i); c3_f = c3_i
   grid_3 = 1
print(" ")

#---------------------------------------------------------------
# Inicialização dos vetores k1, k2 e k3 ------------------------
#---------------------------------------------------------------

c1 = [0]*(grid_1 + 1)
c2 = [0]*(grid_2 + 1)
c3 = [0]*(grid_3 + 1)

#---------------------------------------------------------------
# Escrita do arquivo KPOINTS -----------------------------------
#---------------------------------------------------------------

#---------------------------------
kpoints = open("saida/KPOINTS", "w")
#---------------------------------

if (tipo == 1):
   kpoints.write("Bandas_Plano_3D VASProcar \n")
if (tipo == 2):
   kpoints.write("Bandas_Malha_3D VASProcar \n")

kpoints.write(f'1 \n')
kpoints.write("Line-mode \n")

if (coord == 1):
   kpoints.write("Reciprocal \n")
if (coord == 2):
   kpoints.write("Cartesian \n")

for i in range (1,(grid_1+1)):
    if (grid_1 > 1):
       c1[i] = c1_i + (i-1)*(c1_f - c1_i)/(grid_1 - 1)
    if (grid_1 == 1):
       c1[i] = c1_i
       
    for j in range (1,(grid_2+1)):
        if (grid_2 > 1):
           c2[j] = c2_i + (j-1)*(c2_f - c2_i)/(grid_2 - 1)
        if (grid_2 == 1):
           c2[j] = c2_i    
        
        for k in range (1,(grid_3+1)):
            if (grid_3 > 1):
               c3[k] = c3_i + (k-1)*(c3_f - c3_i)/(grid_3 - 1)
            if (grid_3 == 1):
               c3[k] = c3_i   
            
            kpoints.write(f'{c1[i]} {c2[j]} {c3[k]} \n')

#--------------
kpoints.close()
#--------------

#---------------------------------------------------------------
# Obtenção das coordenadas cartesianas (kx,ky,kz) dos pontos-k -
# gerados no arquivo KPOINTS -----------------------------------
#---------------------------------------------------------------

if (coord == 1):
   #-----------------------------------------------------------
   pontos_k = open("saida/pontos_k_Coord_Cartesianas.txt", "w")
   #-----------------------------------------------------------

   pontos_k.write("Pontos-k do arquivo KPOINTS em Coordenadas Cartesianas (kx,ky,kz) \n")
   pontos_k.write("em função de 2pi/Param. \n")
   pontos_k.write(" \n")

   for i in range (1,(grid_1+1)):
       for j in range (1,(grid_2+1)):
           for k in range (1,(grid_3+1)):
               Coord_X = ((c1[1]*B1x) + (c2[j]*B2x) + (c3[k]*B3x))
               Coord_Y = ((c1[1]*B1y) + (c2[j]*B2y) + (c3[k]*B3y))
               Coord_Z = ((c1[1]*B1z) + (c2[j]*B2z) + (c3[k]*B3z))
               pontos_k.write(f'{Coord_X:.9f} {Coord_Y:.9f} {Coord_Z:.9f} \n')  

   #---------------
   pontos_k.close()
   #---------------

#-----------------------------------------------------------------       

number = grid_1*grid_2*grid_3

print("#######################################################")

if (number < 1000):
   print(f'# O arquivo KPOINTS gerado fornece {number} pontos-k na ZB #')
if (number > 999):
   print(f'# O arquivo KPOINTS gerado fornece {number} pontos-k na ZB ')

print("#######################################################")   

if (coord == 1):
   print("## Um arquivo com as coordenadas cartesianas dos === ##")
   print("## pontos do arquivo KPOINTS esta na pasta saida === ##")
   print("#######################################################")

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =====================")
#-----------------------------------------------------------------

############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### FIM DO CÓDIGO ######################################################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################
