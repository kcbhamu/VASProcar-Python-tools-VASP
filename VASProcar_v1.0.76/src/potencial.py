
def execute_python_file(filename: str):
   return exec(open(main_dir + str(filename)).read(), globals())

#----------------------------------------------------------------------
# Verificando se a pasta "Potencial" existe, se não existe ela é criada
#----------------------------------------------------------------------
if os.path.isdir(dir_files + '\output\Potencial'):
   0 == 0
else:
   os.mkdir(dir_files + '\output\Potencial')
#-------------------------------------------

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================
execute_python_file(filename = 'informacoes.py')

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("############## Plot do Potencial Eletrostatico: ##############")
print ("##############################################################")
print (" ")

print ("##############################################################")
print ("## Dica: Para gerar um Plot 3D do Potencial Eletrostaico    ##")
print ("##       projetado sobre a rede cristalina, abra o arquivo  ##")
print ("##       LOCPOT pelo programa VESTA                         ##")
print ("## ======================================================== ##")
print ("## Link: http://jp-minerals.org/vesta/en/download.html      ##")
print ("##############################################################")
print (" ")

if (escolha == -7):
   print ("##############################################################")
   print ("Escolha a dimensao do eixo-x do Plot: ========================")
   print ("Utilize 1 para Angs. =========================================")
   print ("Utilize 2 para nm. ===========================================")
   print ("##############################################################") 
   Dimensao = input (" "); Dimensao = int(Dimensao)
   print (" ")

   print ("##############################################################")
   print ("Deseja destacar a coordenada dos ions no Plot? ===============")
   print ("[0] Nao ======================================================")
   print ("[1] Sim (Padrao) =============================================")
   print ("##############################################################") 
   destaque = input (" "); destaque = int(destaque)
   print (" ")   

if (escolha == 7):
   Dimensao = 1
   destaque = 1

#----------------------------------------------------------------------
# Extraindo os resultados do arquivo LOCPOT ---------------------------
#----------------------------------------------------------------------

print (".........................................................")
print ("................ Lendo o arquivo LOCPOT: ................")
print ("................... Espere um momento ...................")
print (".........................................................")
print (" ")

#---------------------------
locpot = open("LOCPOT", "r")
#---------------------------

for i in range (8): VTemp = locpot.readline()

# Resultado extraido do arquivo PROCAR (procar.py)
Ax = [A1x*Parametro, A2x*Parametro, A3x*Parametro]
Ay = [A1y*Parametro, A2y*Parametro, A3y*Parametro]
Az = [A1z*Parametro, A2z*Parametro, A3z*Parametro]

ion_x = [0]*(ni)
ion_y = [0]*(ni)
ion_z = [0]*(ni)

#--------------------------------------------------------------------------

for i in range (ni):
    VTemp = locpot.readline().split()
    #---------------------------------------------------------------
    m1 = float(VTemp[0]); m2 = float(VTemp[1]); m3 = float(VTemp[2])
    #--------------------------------------------------------------
    ion_x[i] = ((m1*A1x) + (m2*A2x) + (m3*A3x))*Parametro; ion_x[i] = ion_x[i] - min(Ax)
    ion_y[i] = ((m1*A1y) + (m2*A2y) + (m3*A3y))*Parametro; ion_y[i] = ion_y[i] - min(Ay)
    ion_z[i] = ((m1*A1z) + (m2*A2z) + (m3*A3z))*Parametro; ion_z[i] = ion_z[i] - min(Az)
    
VTemp = locpot.readline()
VTemp = locpot.readline().split()

Grid_x = int(VTemp[0])
Grid_y = int(VTemp[1])
Grid_z = int(VTemp[2])
GRID = Grid_x*Grid_y*Grid_z

V_local = [0]*(GRID)
coord = [0]*3

passo1 = (GRID/5)
resto = passo1 - int(passo1)
if (resto == 0): passo1 = int(passo1)
if (resto != 0): passo1 = int(passo1) + 1

passo2 = 5 - ((passo1*5) -GRID)

for i in range (passo1):
    VTemp = locpot.readline().split()
    if (i < (passo1-1)):
       for j in range(5): V_local[((i)*5) + j] = float(VTemp[j])
    if (i == (passo1-1)):
       for j in range(passo2): V_local[((i)*5) + j] = float(VTemp[j])

#-------------
locpot.close()
#-------------
  
#--------------------------------------------------------------------------

fator_x = max(Ax) - min(Ax)
fator_y = max(Ay) - min(Ay)
fator_z = max(Az) - min(Az)

escala_x = 1.0/float(GRID/Grid_x); Vx = [0]*(Grid_x); X = [0]*(Grid_x)
escala_y = 1.0/float(GRID/Grid_y); Vy = [0]*(Grid_y); Y = [0]*(Grid_y)
escala_z = 1.0/float(GRID/Grid_z); Vz = [0]*(Grid_z); Z = [0]*(Grid_z)

#----------------------------------------------------------------------------
# Analisando os dados - Obtendo o valor médio do Potencial 3D em cada direção
#----------------------------------------------------------------------------

for i in range (Grid_x):
    for j in range (Grid_y):  
        for k in range (Grid_z):                          
            indice = i + (j + k*Grid_y)*Grid_x
            Vx[i] = Vx[i] + V_local[indice]*escala_x
            Vy[j] = Vy[j] + V_local[indice]*escala_y
            Vz[k] = Vz[k] + V_local[indice]*escala_z

#======================================================================
# Plot do Potencial médio em uma dada direção: ========================
#====================================================================== 

import matplotlib.pyplot as plt
import numpy as np

for l in range(1,(3+1)):

    #======================================================================
    #======================================================================
    # Plot 2D do Potencial médio em uma dada direção (GRACE) ==============
    #====================================================================== 
    #======================================================================   

    if (l == 1):      
       print ("Analisando a direcao-X ==================================")
       name = 'Potencial_x'; eixo = 'X '; t_grid = Grid_x; coord = ion_x
       dx = fator_x/20; x_inicial = (0.0 - dx); x_final = (fator_x + dx)
       dy = (max(Vx) - min(Vx))/20; y_inicial = (min(Vx) - dy); y_final = (max(Vx) + dy)    
       
    if (l == 2):
       print ("Analisando a direcao-Y ==================================")      
       name = 'Potencial_y'; eixo = 'Y '; t_grid = Grid_y; coord = ion_y
       dx = fator_y/20; x_inicial = (0.0 - dx); x_final = (fator_y + dx)
       dy = (max(Vy) - min(Vy))/20; y_inicial = (min(Vy) - dy); y_final = (max(Vy) + dy)
       
    if (l == 3):
       print ("Analisando a direcao-Z ==================================")      
       name = 'Potencial_z'; eixo = 'Z '; t_grid = Grid_z; coord = ion_z
       dx = fator_z/20; x_inicial = (0.0 - dx); x_final = (fator_z + dx)
       dy = (max(Vz) - min(Vz))/20; y_inicial = (min(Vz) - dy); y_final = (max(Vz) + dy)

    #-----------------------------------------------------------------------
    potencial = open(dir_files + '\output\Potencial\\' + name + '.agr', "w")
    #-----------------------------------------------------------------------

    potencial.write("# Grace project file \n")
    potencial.write("# written using VASProcar (https://github.com/Augusto-Dlelis/VASProcar-Tools-Python) \n")
    potencial.write("# \n")
    potencial.write("@version 50122 \n")
    potencial.write("@with g0 \n")
    potencial.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
    # potencial.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

    escala_x = (x_final - x_inicial)/5
    escala_y = (y_final - y_inicial)/5

    potencial.write(f'@    xaxis  tick major {escala_x:.2f} \n')
    if (Dimensao == 1):
       label1 = eixo + '(Angs.)'; label2 = eixo + '($\AA$)'
       potencial.write(f'@    xaxis  label "{label1}" \n') 
    if (Dimensao == 2):
       label1 = eixo + '(nm)'; label2 = eixo + '(nm)'
       potencial.write(f'@    xaxis  label "{label1}" \n') 
 
    potencial.write(f'@    yaxis  tick major {escala_y:.2f} \n')
    potencial.write(f'@    yaxis  label "Potencial Eletrostatico (V)" \n')

    #======================================================================

    if (destaque == 0): ni = 0
    if (destaque == 1): ni = ni

    for i in range(1,((ni+1)+1)):

        if (destaque == 1 and i <= ni): color = 7 # cor Cinza
        if (i > ni): color = 2  # cor Vermelha
   
        potencial.write(f'@    s{i-1} type xy \n')
        potencial.write(f'@    s{i-1} line type 1 \n')
        potencial.write(f'@    s{i-1} line color {color} \n')

        if (i <= ni):
           potencial.write(f'@    s{i-1} line linestyle 1 \n')        
           potencial.write(f'@    s{i-1} line linewidth 0.5 \n')
        if (i > ni):
           potencial.write(f'@    s{i-1} line linestyle 1 \n')        
           potencial.write(f'@    s{i-1} line linewidth 2.0 \n')

    potencial.write(f'@type xy \n')

    # Destacando as coordenadas dos ions da rede:
            
    if (destaque == 1): 
       for i in range (ni):
           potencial.write(f'{coord[i]} {y_inicial} \n')
           potencial.write(f'{coord[i]} {y_final} \n')     
           potencial.write(" \n")    
    
    # Plot do valor médio do potencial eletrostatico em uma dada direção:
    
    for i in range (t_grid):
       
        if (l == 1):
           X[i] = (float(i)/(float(Grid_x) - 1.0))*fator_x
           potencial.write(f'{X[i]} {Vx[i]} \n')

        if (l == 2):
           Y[i] = (float(i)/(float(Grid_y) - 1.0))*fator_y
           potencial.write(f'{Y[i]} {Vy[i]} \n')

        if (l == 3):
           Z[i] = (float(i)/(float(Grid_z) - 1.0))*fator_z
           potencial.write(f'{Z[i]} {Vz[i]} \n')           

    #----------------
    potencial.close()
    #----------------   

    #======================================================================
    #======================================================================
    # Plot 2D do Potencial médio em uma dada direção (Matplotlib) =========
    #====================================================================== 
    #======================================================================

    fig, ax = plt.subplots()

    # Destacando as coordenadas dos ions da rede:

    if (destaque == 1):
       for i in range(ni):
           plt.plot([coord[i], coord[i]], [y_inicial, y_final], color = 'gray', linestyle = '-', linewidth = 0.1, alpha = 0.5)

    # Plot do valor médio do potencial eletrostatico em uma dada direção:

    if (l == 1): plt.plot(X, Vx, color = 'red', linestyle = '-', linewidth = 1.0)
    if (l == 2): plt.plot(Y, Vy, color = 'red', linestyle = '-', linewidth = 1.0)
    if (l == 3): plt.plot(Z, Vz, color = 'red', linestyle = '-', linewidth = 1.0)
    
    #======================================================================

    plt.xlim((x_inicial, x_final))
    plt.ylim((y_inicial, y_final))

    plt.xlabel(label2)
    plt.ylabel('Potencial Eletrostatico (V)')

    # ax.set_box_aspect(1.25/1)  

    if (save_png == 1): plt.savefig(dir_files + '\output\Potencial\\' + name + '.png', dpi = 600)
    if (save_pdf == 1): plt.savefig(dir_files + '\output\Potencial\\' + name + '.pdf', dpi = 600)
    if (save_eps == 1): plt.savefig(dir_files + '\output\Potencial\\' + name + '.eps', dpi = 600)

    # plt.show()

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------
