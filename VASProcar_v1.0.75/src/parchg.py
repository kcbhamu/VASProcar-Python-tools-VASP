
#------------------------------------------------------------------------------------
# Verificando se a pasta "Densidade_Carga_Parcial" existe, se não existe ela é criada
#------------------------------------------------------------------------------------
if os.path.isdir(dir_files + '\output\Densidade_Carga_Parcial'):
   0 == 0
else:
   os.mkdir(dir_files + '\output\Densidade_Carga_Parcial')
#---------------------------------------------------------

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("############# Plot da Densidade de Carga Parcial #############")
print ("##############################################################")
print (" ")

print ("##############################################################")
print ("## Dica: Para gerar um Plot 3D da Densidade de Carga        ##")
print ("##       projetada sobre a rede cristalina, renomei o       ##")
print ("##       arquivo para PARCHG e abra pelo programa VESTA     ##")
print ("## ======================================================== ##")
print ("## Link: http://jp-minerals.org/vesta/en/download.html      ##")
print ("##############################################################")
print (" ")

print ("##############################################################")
print ("Insira o nome completo do arquivo que vc deseja analisar: ====")
print ("##############################################################") 
name = input (" "); name = str(name)
print (" ")

if (escolha == -8): 
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

if (escolha == 8):
   Dimensao = 1
   destaque = 1

#----------------------------------------------------------------------
# Extraindo os resultados do arquivo PARCHG ---------------------------
#----------------------------------------------------------------------

print (".........................................................")
print ("................ Lendo o arquivo PARCHG: ................")
print ("................... Espere um momento ...................")
print (".........................................................")
print (" ")

#-----------------------
parchg = open(name, 'r')
#-----------------------

for i in range (8): VTemp = parchg.readline()

# Resultado extraido do arquivo PROCAR (procar.py)
Ax = [A1x*Parametro, A2x*Parametro, A3x*Parametro]
Ay = [A1y*Parametro, A2y*Parametro, A3y*Parametro]
Az = [A1z*Parametro, A2z*Parametro, A3z*Parametro]

ion_x = [0]*(ni)
ion_y = [0]*(ni)
ion_z = [0]*(ni)

for i in range (ni):
    VTemp = parchg.readline().split()
    #---------------------------------------------------------------
    m1 = float(VTemp[0]); m2 = float(VTemp[1]); m3 = float(VTemp[2])
    #--------------------------------------------------------------
    ion_x[i] = ((m1*A1x) + (m2*A2x) + (m3*A3x))*Parametro; ion_x[i] = ion_x[i] - min(Ax)
    ion_y[i] = ((m1*A1y) + (m2*A2y) + (m3*A3y))*Parametro; ion_y[i] = ion_y[i] - min(Ay)
    ion_z[i] = ((m1*A1z) + (m2*A2z) + (m3*A3z))*Parametro; ion_z[i] = ion_z[i] - min(Az)
    
VTemp = parchg.readline()
VTemp = parchg.readline().split()

Grid_x = int(VTemp[0])
Grid_y = int(VTemp[1])
Grid_z = int(VTemp[2])
GRID = Grid_x*Grid_y*Grid_z

V_local = [0]*(GRID)
coord = [0]*3

passo1 = (GRID/10)
resto = passo1 - int(passo1)
if (resto == 0): passo1 = int(passo1)
if (resto != 0): passo1 = int(passo1) + 1

passo2 = 10 - ((passo1*10) -GRID)

for i in range (passo1):
    VTemp = parchg.readline().split()
    if (i < (passo1-1)):
       for j in range(10): V_local[((i)*10) + j] = float(VTemp[j])
    if (i == (passo1-1)):
       for j in range(passo2): V_local[((i)*10) + j] = float(VTemp[j])

#-------------
parchg.close()
#-------------
  
#--------------------------------------------------------------------------

fator_x = max(Ax) - min(Ax)
fator_y = max(Ay) - min(Ay)
fator_z = max(Az) - min(Az)

escala_x = 1.0/float(GRID/Grid_x); Vx = [0]*(Grid_x); X = [0]*(Grid_x)
escala_y = 1.0/float(GRID/Grid_y); Vy = [0]*(Grid_y); Y = [0]*(Grid_y)
escala_z = 1.0/float(GRID/Grid_z); Vz = [0]*(Grid_z); Z = [0]*(Grid_z)

#---------------------------------------------------------------------------------------------
# Analisando os dados: Obtendo o valor médio da Densidade de Carga Parcial em uma dada direção
#---------------------------------------------------------------------------------------------

for i in range (Grid_x):
    for j in range (Grid_y):  
        for k in range (Grid_z):                          
            indice = i + (j + k*Grid_y)*Grid_x
            Vx[i] = Vx[i] + V_local[indice]*escala_x
            Vy[j] = Vy[j] + V_local[indice]*escala_y
            Vz[k] = Vz[k] + V_local[indice]*escala_z

#======================================================================
# Plot 2D da Densidade de Carga Parcial em uma dada direção: ==========
#====================================================================== 

for l in range(1,(3+1)):

    #=================================================================================
    #=================================================================================
    # Plot 2D da Densidade de Carga Parcial em uma dada direção (GRACE) ==============
    #================================================================================= 
    #=================================================================================   

    if (l == 1):      
       print ("Analisando a direcao-X ==================================")
       name = 'Densidade_x'; eixo = 'X '; t_grid = Grid_x; coord = ion_x
       dx = fator_x/20; x_inicial = (0.0 - dx); x_final = (fator_x + dx)
       dy = (max(Vx) - min(Vx))/20; y_inicial = (min(Vx) - dy); y_final = (max(Vx) + dy)      
       
    if (l == 2):
       print ("Analisando a direcao-Y ==================================")      
       name = 'Densidade_y'; eixo = 'Y '; t_grid = Grid_y; coord = ion_y
       dx = fator_y/20; x_inicial = (0.0 - dx); x_final = (fator_y + dx)
       dy = (max(Vy) - min(Vy))/20; y_inicial = (min(Vy) - dy); y_final = (max(Vy) + dy)
       
    if (l == 3):
       print ("Analisando a direcao-Z ==================================")      
       name = 'Densidade_z'; eixo = 'Z '; t_grid = Grid_z; coord = ion_z
       dx = fator_z/20; x_inicial = (0.0 - dx); x_final = (fator_z + dx)
       dy = (max(Vz) - min(Vz))/20; y_inicial = (min(Vz) - dy); y_final = (max(Vz) + dy)

    #-------------------------------------------------------------------------------------
    densidade = open(dir_files + '\output\Densidade_Carga_Parcial\\' + name + '.agr', "w")
    #-------------------------------------------------------------------------------------

    densidade.write("# Grace project file \n")
    densidade.write("# written using VASProcar (https://github.com/Augusto-Dlelis/VASProcar-Tools-Python) \n") 
    densidade.write("# \n")
    densidade.write("@version 50122 \n")
    densidade.write("@with g0 \n")
    densidade.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
    # densidade.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

    escala_x = (x_final - x_inicial)/5
    escala_y = (y_final - y_inicial)/5

    densidade.write(f'@    xaxis  tick major {escala_x:.2f} \n')
    if (Dimensao == 1):
       label1 = eixo + '(Angs.)'; label2 = eixo + '($\AA$)'
       densidade.write(f'@    xaxis  label "{label1}" \n') 
    if (Dimensao == 2):
       label1 = eixo + '(nm)'; label2 = eixo + '(nm)'
       densidade.write(f'@    xaxis  label "{label1}" \n') 
 
    densidade.write(f'@    yaxis  tick major {escala_y:.2f} \n')
    densidade.write(f'@    yaxis  label "Densidade de Carga Parcial" \n')

    #======================================================================

    if (destaque == 0): ni = 0
    if (destaque == 1): ni = ni
    
    for i in range(1,((ni+1)+1)):

        if (destaque == 1 and i <= ni): color = 7 # cor Cinza
        if (i > ni): color = 2  # cor Vermelha
   
        densidade.write(f'@    s{i-1} type xy \n')
        densidade.write(f'@    s{i-1} line type 1 \n')
        densidade.write(f'@    s{i-1} line color {color} \n')
        
        if (i <= ni):
           densidade.write(f'@    s{i-1} line linestyle 1 \n')        
           densidade.write(f'@    s{i-1} line linewidth 0.5 \n')
        if (i > ni):
           densidade.write(f'@    s{i-1} line linestyle 1 \n')        
           densidade.write(f'@    s{i-1} line linewidth 2.0 \n')
           
    densidade.write(f'@type xy \n')

    # Destacando as coordenadas dos ions da rede:
            
    if (destaque == 1): 
       for i in range (ni):
           densidade.write(f'{coord[i]} {y_inicial} \n')
           densidade.write(f'{coord[i]} {y_final} \n')     
           densidade.write(" \n")    
    
    # Plot do valor médio da densidade de carga parcial em uma dada direção:
    
    for i in range (t_grid):
       
        if (l == 1):
           X[i] = (float(i)/(float(Grid_x) - 1.0))*fator_x
           densidade.write(f'{X[i]} {Vx[i]} \n')

        if (l == 2):
           Y[i] = (float(i)/(float(Grid_y) - 1.0))*fator_y
           densidade.write(f'{Y[i]} {Vy[i]} \n')

        if (l == 3):
           Z[i] = (float(i)/(float(Grid_z) - 1.0))*fator_z
           densidade.write(f'{Z[i]} {Vz[i]} \n')           

    #----------------
    densidade.close()
    #----------------   

    #=================================================================================
    #=================================================================================
    # Plot 2D da Densidade de Carga Parcial em uma dada direção (Matplotlib) =========
    #================================================================================= 
    #=================================================================================

    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots()

    # Destacando as coordenadas dos ions da rede:

    if (destaque == 1):
       for i in range(ni):
           plt.plot([coord[i], coord[i]], [y_inicial, y_final], color = 'gray', linestyle = '-', linewidth = 0.1, alpha = 0.5)

    # Plot do valor médio da densidade de carga parcial em uma dada direção:

    if (l == 1): plt.plot(X, Vx, color = 'red', linestyle = '-', linewidth = 1.0)
    if (l == 2): plt.plot(Y, Vy, color = 'red', linestyle = '-', linewidth = 1.0)
    if (l == 3): plt.plot(Z, Vz, color = 'red', linestyle = '-', linewidth = 1.0)
    
    #======================================================================

    plt.xlim((x_inicial, x_final))
    plt.ylim((y_inicial, y_final))

    plt.xlabel(label2)
    plt.ylabel('Densidade de Carga Parcial')

    # ax.set_box_aspect(1.25/1)  

    if (save_png == 1): plt.savefig(dir_files + '\output\Densidade_Carga_Parcial\\' + name + '.png', dpi = 600)
    if (save_pdf == 1): plt.savefig(dir_files + '\output\Densidade_Carga_Parcial\\' + name + '.pdf', dpi = 600)
    if (save_eps == 1): plt.savefig(dir_files + '\output\Densidade_Carga_Parcial\\' + name + '.eps', dpi = 600)

    # plt.show()

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------
