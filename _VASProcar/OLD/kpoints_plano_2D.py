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
print("## Criacao do arquivo KPOINTS (Plano 2D na ZB): ==== ##")
print("#######################################################")
print(" ")

print("#######################################################")
print("## Pontos-k em Coord. Diretas k1, k2 e k3: ========= ##")
print("## K =  k1*B1 + k2*B2 + k3*B3 ====================== ##")
print("#######################################################")
print("## Vetores Primitivos da Rede Reciproca:")
print(f'## B1 = 2pi/Param.({B1x}, {B1y}, {B1z})')
print(f'## B2 = 2pi/Param.({B2x}, {B2y}, {B2z})')
print(f'## B3 = 2pi/Param.({B3x}, {B3y}, {B3z})')
print(f'## Param. = {Parametro} Angs.')
print("#######################################################")
print(" ")

print("#######################################################")
print("## Defina qual plano deseja varrer na ZB: ========== ##")
print("## [1] Plano k1k2 (k3 fixo) ======================== ##")
print("## [2] Plano k1k3 (k2 fixo) ======================== ##")
print("## [3] Plano k2k3 (k1 fixo) ======================== ##")
print("#######################################################")
esc = input (" "); esc = int(esc)
print(" ")

if (esc == 1):
   k_fixo = 'k3'; plano = "k1k2"; temp1 = 'k1'; temp2 = "k2"
if (esc == 2):
   k_fixo = 'k2'; plano = "k1k3"; temp1 = 'k1'; temp2 = "k3"
if (esc == 3):
   k_fixo = 'k1'; plano = "k2k3"; temp1 = 'k2'; temp2 = "k3"

print("#######################################################")
print(f'####### Digite o valor da coordenada fixa ({k_fixo}): #######')
print("#######################################################")
coord_fixa = input (" "); coord_fixa = float(coord_fixa)
print(" ")

print("#######################################################")
print(f'##### Quais coordenadas delimitam o plano ({plano})? #####')
print("#######################################################")
print(" ")

print("#######################################################")
print(f'## {temp1} inicial: ########################################')
print("#######################################################")
c1_i = input (" "); c1_i = float(c1_i)
print(" ")
print("#######################################################")
print(f'## {temp1} final: ##########################################')
print("#######################################################")
c1_f = input (" "); c1_f = float(c1_f)
print(" ")
print("#######################################################")
print(f'## {temp2} inicial: ########################################')
print("#######################################################")
c2_i = input (" "); c2_i = float(c2_i)
print(" ")
print("#######################################################")
print(f'## {temp2} final: ##########################################')
print("#######################################################")
c2_f = input (" "); c2_f = float(c2_f)
print(" ")
print("#######################################################")
print("######### Escolha o GRID da malha de pontos-K #########")
print(" Exemplo: Digite 31 para um GRID de 31x31 pontos na ZB ")
print("#######################################################")
GRID = input (" "); GRID = int(GRID)
print(" ")

#-----------------------------------------------------------------------
# Inicizalização dos vetores/matrizes k1, k2 e k3 ----------------------
#-----------------------------------------------------------------------

k1 = [[0]*(GRID+1) for k in range(2+1)]  # k1[2][GRID]
k2 = [[0]*(GRID+1) for k in range(2+1)]  # k2[2][GRID]
k3 = [[0]*(GRID+1) for k in range(2+1)]  # k3[2][GRID]

#-----------------------------------------------------------------------
# Armazenando o valor da coordenada fixa para todos os pontos-k --------
#-----------------------------------------------------------------------

if (esc == 1):                    # Plano k1k2 (k3 fixo)
   for i in range (1,(2+1)):      # No arquivo KPOINTS cada intervalo a ser varrido é definido por 2 pontos-k, uma inicial (i = 1) e outro final (i = 2). 
       for j in range (1,(GRID+1)):
           k3[i][j] = coord_fixa
  
if (esc == 2):                    # Plano k1k3 (k2 fixo)
   for i in range (1,(2+1)):      # No arquivo KPOINTS cada intervalo a ser varrido é definido por 2 pontos-k, uma inicial (i = 1) e outro final (i = 2).
       for j in range (1,(GRID+1)):
           k2[i][j] = coord_fixa

if (esc == 3):                    # Plano k2k3 (k1 fixo)
   for i in range (1,(2+1)):      # No arquivo KPOINTS cada intervalo a ser varrido é definido por 2 pontos-k, uma inicial (i = 1) e outro final (i = 2).
       for j in range (1,(GRID+1)):
           k1[i][j] = coord_fixa         

#-----------------------------------------------------------------------
# Uma das coordenadas restantes foi tomada como sendo os pontos inicial
# e final da linha varrida na ZB durante o plot da estrutura de bandas,
# seguindo a construção padrão do arquivo KPOINTS.
#-----------------------------------------------------------------------

if (esc != 3):                #  k1k2 (k3 fixo)  ou  k1k3 (k2 fixo)
   for j in range (1,(GRID+1)):
       k1[1][j] = c1_i
       k1[2][j] = c1_f

if (esc == 3):                #  k2k3 (k1 fixo)
   for j in range (1,(GRID+1)):
       k2[1][j] = c1_i
       k2[2][j] = c1_f

#-----------------------------------------------------------------------
# Por fim, o valor da coordenada restante é variado entre os limites  
# inicial e final a fim de gerar os pontos restantes do plano 2D.
#------------------------------------------------------------------------

coord = c2_i

if (esc != 1):                             #  k1k3 (k2 fixo)  ou  Plano k2k3 (k1 fixo)
   for i in range (1,(2+1)):
       for j in range (1,(GRID+1)):
           k3[1][j] = coord + (j-1)*(c2_f - coord)/(GRID - 1)
           k3[2][j] = coord + (j-1)*(c2_f - coord)/(GRID - 1)

if (esc == 1):
   for i in range (1,(2+1)):               #  Plano k1k2 (k3 fixo)
       for j in range (1,(GRID+1)):
           k2[1][j] = coord + (j-1)*(c2_f - coord)/(GRID - 1)
           k2[2][j] = coord + (j-1)*(c2_f - coord)/(GRID - 1)         

#-----------------------------------------------------------------------
# Escrita do arquivo KPOINTS -------------------------------------------
#-----------------------------------------------------------------------

#---------------------------------
kpoints = open("saida/KPOINTS.txt", "w")
#---------------------------------

kpoints.write("Bandas_Plano_2D VASProcar \n")
kpoints.write(f'{GRID} \n')
kpoints.write("Line-mode \n")
kpoints.write("Reciprocal \n")
      
for j in range (1,(GRID+1)):
    kpoints.write(f'{k1[1][j]} {k2[1][j]} {k3[1][j]} \n')
    kpoints.write(f'{k1[2][j]} {k2[2][j]} {k3[2][j]} \n')
    kpoints.write(" \n")

#--------------
kpoints.close()
#--------------

#---------------------------------------------------------------
# Obtenção das coordenadas cartesianas (kx,ky,kz) dos pontos-k -
# gerados no arquivo KPOINTS -----------------------------------
#---------------------------------------------------------------

#-----------------------------------------------------------
pontos_k = open("saida/pontos_k_Coord_Cartesianas.txt", "w")
#-----------------------------------------------------------

pontos_k.write("Pontos-k do arquivo KPOINTS em Coordenadas Cartesianas (kx,ky,kz) \n")
pontos_k.write("em função de 2pi/Param. \n")
pontos_k.write(" \n")

for j in range (1,(GRID+1)):
   
    Coord_X = ((k1[1][j]*B1x) + (k2[1][j]*B2x) + (k3[1][j]*B3x))
    Coord_Y = ((k1[1][j]*B1y) + (k2[1][j]*B2y) + (k3[1][j]*B3y))
    Coord_Z = ((k1[1][j]*B1z) + (k2[1][j]*B2z) + (k3[1][j]*B3z))
    pontos_k.write(f'{Coord_X:.9f} {Coord_Y:.9f} {Coord_Z:.9f} \n')

    Coord_X = ((k1[2][j]*B1x) + (k2[2][j]*B2x) + (k3[2][j]*B3x))
    Coord_Y = ((k1[2][j]*B1y) + (k2[2][j]*B2y) + (k3[2][j]*B3y))
    Coord_Z = ((k1[2][j]*B1z) + (k2[2][j]*B2z) + (k3[2][j]*B3z))
    pontos_k.write(f'{Coord_X:.9f} {Coord_Y:.9f} {Coord_Z:.9f} \n')

    pontos_k.write(" \n")    

#---------------
pontos_k.close()
#---------------    

#-----------------------------------------------------------------        

number = GRID**2

print("#######################################################")

if (number < 1000):
   print(f'# O arquivo KPOINTS gerado fornece {number} pontos-k na ZB #')
if (number > 999):
   print(f'# O arquivo KPOINTS gerado fornece {number} pontos-k na ZB ')

print("#######################################################")
print("## Um arquivo com as coordenadas cartesianas dos === ##")
print("## pontos do arquivo KPOINTS esta na pasta saida === ##")
print("#######################################################")

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------

############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### FIM DO CÓDIGO ######################################################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################
