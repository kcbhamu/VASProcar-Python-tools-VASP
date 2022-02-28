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

#---------------------------------------------------------------------
# Verificando se a pasta "Orbitais" existe, se não existe ela é criada
#---------------------------------------------------------------------
if os.path.isdir("saida/DOS"):
   0 == 0
else:
   os.mkdir("saida/DOS")
#----------------------------

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================

#-----------------------------------------
executavel = Diretorio + '/informacoes.py'
exec(open(executavel).read())
#-----------------------------------------

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

if (escolha == 11):
   esc = 0

print ("##############################################################")
print ("################### Densidade de Estados: ####################")
print ("##############################################################") 
print (" ")

if (escolha == -11):
   esc = 1

   sim_nao = ["nao"]*(ni + 1)             # Inicialização do vetor sim_nao
      
   print ("##############################################################")
   print ("Especifique os ions selecionados em intervalos ===============")
   print ("Quantos intervalos de ions ira fornecer abaixo? ==============")
   print ("##############################################################")
   loop = input (" "); loop = int(loop)
   for i in range (1,(loop+1)):
       print (" ")
       print (f'{i} intervalo: ==============================================')
       print ("Digite o ion inicial do intervalo ============================")
       loop_i = input (" "); loop_i = int(loop_i)
       print ("Digite o ion final do intervalo ==============================")
       loop_f = input (" "); loop_f = int(loop_f)
       if (loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0):
          print (" ")
          print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
          print ("   ERRO: Os valores de ions informados estao incorretos   ")
          print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
          print (" ")
       for i in range(loop_i, (loop_f + 1)):
          sim_nao[i] = "sim"

   print (" ")

#----------------------------------------------------------------------
# Extraindo os resultados do arquivo DOSCAR ---------------------------
#----------------------------------------------------------------------

#---------------------------
doscar = open("DOSCAR", "r")
#---------------------------

for i in range(6):
    VTemp = doscar.readline().split()

E_max = float(VTemp[0]) - Efermi
E_min = float(VTemp[1]) - Efermi
NEDOS = int(VTemp[2])

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------

if (lorbit == 10): n_orb = 3
if (lorbit >= 11): n_orb = 9

energia   = [0]*(NEDOS+1)   # energia[NEDOS]
dos       = [0]*(NEDOS+1)   # dos[NEDOS]
dos_int   = [0]*(NEDOS+1)   # dos_int[NEDOS]
l_dos     = [0]*(NEDOS+1)   # l_dos[NEDOS]

pdos     = [[[0]*(NEDOS+1) for i in range(ni+1)] for j in range(n_orb+1)]   # pdos[9][ni][NEDOS]
pdos_tot = [[0]*(NEDOS+1) for i in range(n_orb+1)]                          # pdos_tot[9][NEDOS]

# pdos[1][ni][NEDOS] = Orbital S    //  pdos_tot[1][ni][NEDOS] = Orbital S total
# pdos[2][ni][NEDOS] = Orbital Py   //  pdos_tot[2][ni][NEDOS] = Orbital Py total
# pdos[3][ni][NEDOS] = Orbital Pz   //  pdos_tot[3][ni][NEDOS] = Orbital Pz total
# pdos[4][ni][NEDOS] = Orbital Px   //  pdos_tot[4][ni][NEDOS] = Orbital Px total
# pdos[5][ni][NEDOS] = Orbital Dxy  //  pdos_tot[5][ni][NEDOS] = Orbital Dxy total
# pdos[6][ni][NEDOS] = Orbital Dyz  //  pdos_tot[6][ni][NEDOS] = Orbital Dyz total
# pdos[7][ni][NEDOS] = Orbital Dz2  //  pdos_tot[7][ni][NEDOS] = Orbital Dz2 total
# pdos[8][ni][NEDOS] = Orbital Dxz  //  pdos_tot[8][ni][NEDOS] = Orbital Dxz total
# pdos[9][ni][NEDOS] = Orbital Dx2  //  pdos_tot[9][ni][NEDOS] = Orbital Dx2 total

pdos_P     = [[0]*(NEDOS+1) for i in range(ni+1)]   # pdos_P[ni][NEDOS]
pdos_D     = [[0]*(NEDOS+1) for i in range(ni+1)]   # pdos_D[ni][NEDOS]
pdos_P_tot = [0]*(NEDOS+1)                          # pdos_P_tot[NEDOS]
pdos_D_tot = [0]*(NEDOS+1)                          # pdos_D_tot[NEDOS]

x_inicial = +1000.0
x_final   = -1000.0

#-------------------------------------------------------------------------------------------------

for i in range (1,(NEDOS+1)):
      VTemp = doscar.readline().split()
      energia[i] = float(VTemp[0]); energia[i] = (energia[i] - Efermi)
      # dos[i] = float(VTemp[1])
      dos_int[i] = float(VTemp[2])

      # if (dos[i] <= x_inicial): x_inicial = dos[i]
      # if (dos[i] >= x_final): x_final = dos[i] 
      
for i in range (1,(ni+1)):
    if (esc == 1): temp_sn = sim_nao[i]
    #------------------------
    VTemp = doscar.readline()
    #----------------------------
    for j in range (1,(NEDOS+1)):
        VTemp = doscar.readline().split()
        for k in range(1,(n_orb+1)):
            passo = (4*k -3)
            if (esc == 0 or (esc == 1 and temp_sn == "sim")):
               pdos[k][i][j] = float(VTemp[passo])
           
            if (lorbit == 10 and k == 2): pdos_P[i][j] = pdos_P[i][j] + pdos[k][i][j]
            if (lorbit == 10 and k == 3): pdos_D[i][j] = pdos_D[i][j] + pdos[k][i][j]
            if (lorbit >= 11 and (k == 2 or k == 3 or k == 4)): pdos_P[i][j] = pdos_P[i][j] + pdos[k][i][j]
            if (lorbit >= 11 and (k == 5 or k == 6 or k == 7 or k == 8 or k == 9)): pdos_D[i][j] = pdos_D[i][j] + pdos[k][i][j]

            pdos_tot[k][j] = pdos_tot[k][j] + pdos[k][i][j]
            dos[j] = dos[j] + float(VTemp[passo])
            l_dos[j] = l_dos[j] + pdos[k][i][j]
            
        pdos_P_tot[j] = pdos_P_tot[j] + pdos_P[i][j]
        pdos_D_tot[j] = pdos_D_tot[j] + pdos_D[i][j]

        if (dos[j] <= x_inicial): x_inicial = dos[j]
        if (dos[j] >= x_final): x_final = dos[j]         
               
#-------------
doscar.close()
#-------------

#======================================================================
#======================================================================
# Plot da DOS e pDOS (GRACE)===========================================
#====================================================================== 
#======================================================================

#======================================================================
# Obtenção de alguns parâmetros de ajusto do Grafico (GRACE) ==========
#======================================================================    

y_inicial = E_min
y_final   = E_max
                          
# Rotulo dos Orbitais ================================================= 

r_pdos = [0]*(12)
r_pdos[1] = 'S'; r_pdos[2] = 'P'; r_pdos[3] = 'D'; r_pdos[4] = 'Px'; r_pdos[5] = 'Py'; r_pdos[6] = 'Pz'
r_pdos[7] = 'Dxy'; r_pdos[8] = 'Dyz'; r_pdos[9] = 'Dz2'; r_pdos[10] = 'Dxz'; r_pdos[11] = 'Dx2'

#======================================================================

if (lorbit == 10): loop = 1          
if (lorbit >= 11): loop = 3

for i in range (1,(loop+1)):     # Loop para a analise da DOS e pDOS
        
#-----------------------------------------------------------------------

    if (i == 1):
       #-----------------------------------------------
       dos_pdos = open("saida/DOS/DOS_PDOS.agr", "w")
       #-----------------------------------------------
       print ("=================================") 
       print ("Analisando a DOS e pDOS (S, P, D)")        
       s = 1; t = (3+1); r = 4
       
    if (i == 2):
       #---------------------------------------------
       dos_pdos = open("saida/DOS/PDOS_P.agr", "w")     
       #---------------------------------------------
       print ("Analisando a pDOS (Px, Py, Pz)") 
       s = 4; t = (6+1); r = 4
       
    if (i == 3):
       #---------------------------------------------
       dos_pdos = open("saida/DOS/PDOS_D.agr", "w")
       #---------------------------------------------
       print ("Analisando a pDOS (Dxy, Dyz, Dz2, Dxz, Dx2)") 
       s = 7; t = (11+1); r = 6   

# Escrita do arquivo ".agr" do GRACE ===================================

    dos_pdos.write("# Grace project file \n")
    dos_pdos.write("# written using VASProcar (https://github.com/Augusto-Dlelis/VASProcar-Tools-Python) \n") 
    dos_pdos.write("# \n")
    dos_pdos.write("@version 50122 \n")
    dos_pdos.write("@with g0 \n")
    dos_pdos.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
    dos_pdos.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

    escala_x = (x_final - x_inicial)/5
    escala_y = (y_final - y_inicial)/5

    dos_pdos.write(f'@    xaxis  tick major {escala_x:.2f} \n')
    dos_pdos.write(f'@    xaxis  label "Density of States" \n')    
    dos_pdos.write(f'@    yaxis  tick major {escala_y:.2f} \n')
    dos_pdos.write(f'@    yaxis  label "E(eV)" \n')       
    dos_pdos.write(f'@    legend {fig_xmax + leg_x}, {fig_ymax + leg_y} \n')

    dos_pdos.write(f'@    s0 type xy \n')
    dos_pdos.write(f'@    s0 line type 1 \n')
    dos_pdos.write(f'@    s0 line color 1 \n')
    dos_pdos.write(f'@    s0 line linewidth 1.5 \n')
    dos_pdos.write(f'@    s0 fill type 1 \n')
    dos_pdos.write(f'@    s0 fill color 1 \n')
    dos_pdos.write(f'@    s0 fill pattern 4 \n')

    if (i == 1): dos_pdos.write(f'@    s0 legend  "DOS" \n')
    if (i == 2): dos_pdos.write(f'@    s0 legend  "P" \n')
    if (i == 3): dos_pdos.write(f'@    s0 legend  "D" \n')

    number = 0
    
    if (i == 1 and esc == 1):
       number = 1; r = 5
       dos_pdos.write(f'@    s1 type xy \n')
       dos_pdos.write(f'@    s1 line type 1 \n')
       dos_pdos.write(f'@    s1 line color 10 \n')
       dos_pdos.write(f'@    s1 line linewidth 1.5 \n')
       dos_pdos.write(f'@    s1 fill type 1 \n')
       dos_pdos.write(f'@    s1 fill color 10 \n')
       dos_pdos.write(f'@    s1 fill pattern 4 \n')      
       dos_pdos.write(f'@    s1 legend  "l-DOS" \n')     
       
    for j in range (s,t):
        number += 1
          
        if (j == (s+0)): color = cor_orb[j]        # Cor dos Orbitais (S,Px,Dxy)
        if (j == (s+1)): color = cor_orb[j]        # Cor dos Orbitais (P,Py,Dyz)
        if (j == (s+2)): color = cor_orb[j]        # Cor dos Orbitais (D,Pz,Dz2)
        if (j == (s+3)): color = cor_orb[j]        # Cor do Orbital Dxz
        if (j == (s+4)): color = cor_orb[j]        # Cor do Orbital Dx2
           
        dos_pdos.write(f'@    s{number} type xy \n')
        dos_pdos.write(f'@    s{number} line type 1 \n')
        dos_pdos.write(f'@    s{number} line color {color} \n')
        dos_pdos.write(f'@    s{number} line linewidth 1.5 \n')
        dos_pdos.write(f'@    s{number} fill type 1 \n')
        dos_pdos.write(f'@    s{number} fill color {color} \n')
        dos_pdos.write(f'@    s{number} fill pattern 4 \n')      
        dos_pdos.write(f'@    s{number} legend  "{r_pdos[j]}" \n')  

    dos_pdos.write(f'@    s{r} type xy \n')
    dos_pdos.write(f'@    s{r} line type 1 \n')
    dos_pdos.write(f'@    s{r} line color 7 \n')

    dos_pdos.write("@type xy")
    dos_pdos.write(" \n")
      
# Plot da DOS e pDOS ======================================================

    for l in range(1,(6+1)):
        for k in range (1,(NEDOS+1)):
            #---------------------------------------------------------------------------
            if (i == 1 and l == 1): dos_pdos.write(f'{dos[k]} {energia[k]} \n')
            if (esc == 1 and (i == 1 and l == 2)): dos_pdos.write(f'{l_dos[k]} {energia[k]} \n')            
            if (i == 1 and l == 3): dos_pdos.write(f'{pdos_tot[1][k]} {energia[k]} \n')
            if (i == 1 and l == 4): dos_pdos.write(f'{pdos_P_tot[k]} {energia[k]} \n')
            if (i == 1 and l == 5): dos_pdos.write(f'{pdos_D_tot[k]} {energia[k]} \n')
            #---------------------------------------------------------------------------
            if (i == 2 and l == 1): dos_pdos.write(f'{pdos_P_tot[k]} {energia[k]} \n')
            if (i == 2 and l == 2): dos_pdos.write(f'{pdos_tot[4][k]} {energia[k]} \n')
            if (i == 2 and l == 3): dos_pdos.write(f'{pdos_tot[2][k]} {energia[k]} \n')
            if (i == 2 and l == 4): dos_pdos.write(f'{pdos_tot[3][k]} {energia[k]} \n')
            #---------------------------------------------------------------------------
            if (i == 3 and l == 1): dos_pdos.write(f'{pdos_D_tot[k]} {energia[k]} \n') 
            if (i == 3 and l == 2): dos_pdos.write(f'{pdos_tot[5][k]} {energia[k]} \n')
            if (i == 3 and l == 3): dos_pdos.write(f'{pdos_tot[6][k]} {energia[k]} \n')
            if (i == 3 and l == 4): dos_pdos.write(f'{pdos_tot[7][k]} {energia[k]} \n')
            if (i == 3 and l == 5): dos_pdos.write(f'{pdos_tot[8][k]} {energia[k]} \n')           
            if (i == 3 and l == 6): dos_pdos.write(f'{pdos_tot[9][k]} {energia[k]} \n')
        dos_pdos.write(" \n")

# Destacando a energia de Fermi na estrutura de Bandas ================

    dos_pdos.write(" \n")
    dos_pdos.write(f'{x_inicial} 0.0 \n')
    dos_pdos.write(f'{x_final} 0.0 \n')
      
    #-----------------
    dos_pdos.close()
    #-----------------

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")
print(".... Quase concluido ....")
print(".........................")    

#======================================================================
#======================================================================
# Plot das Projeções dos Orbitais (Matplotlib) ========================
#====================================================================== 
#======================================================================

import matplotlib.pyplot as plt
import numpy as np

if (lorbit == 10): loop = 1          
if (lorbit >= 11): loop = 3  

for l in range (1,(loop+1)):     # Loop para a analise das Projecoes

    fig, ax = plt.subplots() 

    # Plot das Projeções ===================================================

    transp = 0.25
    linew = 0.5

    if (l == 1):
       ax.plot(dos, energia, color = 'gray', linestyle = '-', linewidth = linew, label = 'DOS')
       ax.fill(dos, energia, color = 'gray', alpha = transp)
       if (esc == 1):
          ax.plot(l_dos, energia, color = 'magenta', linestyle = '-', linewidth = linew, label = 'l-DOS')
          ax.fill(l_dos, energia, color = 'magenta', alpha = transp)          
       ax.plot(pdos_tot[1], energia, color = 'blue', linestyle = '-', linewidth = linew, label = 'S')
       ax.fill(pdos_tot[1], energia, color = 'blue', alpha = transp)
       ax.plot(pdos_P_tot, energia, color = 'red', linestyle = '-', linewidth = linew, label = 'P')
       ax.fill(pdos_P_tot, energia, color = 'red', alpha = transp)
       ax.plot(pdos_D_tot, energia, color = 'limegreen', linestyle = '-', linewidth = linew, label = 'D')
       ax.fill(pdos_D_tot, energia, color = 'limegreen', alpha = transp)

    if (l == 2):
       ax.plot(pdos_P_tot, energia, color = 'gray', linestyle = '-', linewidth = linew, label = 'P')
       ax.fill(pdos_P_tot, energia, color = 'gray', alpha = transp)
       ax.plot(pdos_tot[4], energia, color = 'blue', linestyle = '-', linewidth = linew, label = r'${P}_{x}$')
       ax.fill(pdos_tot[4], energia, color = 'blue', alpha = transp)
       ax.plot(pdos_tot[2], energia, color = 'red', linestyle = '-', linewidth = linew, label = r'${P}_{y}$')
       ax.fill(pdos_tot[2], energia, color = 'red', alpha = transp)
       ax.plot(pdos_tot[3], energia, color = 'limegreen', linestyle = '-', linewidth = linew, label = r'${P}_{z}$')
       ax.fill(pdos_tot[3], energia, color = 'limegreen', alpha = transp)

    if (l == 3):
       ax.plot(pdos_D_tot, energia, color = 'gray', linestyle = '-', linewidth = linew, label = 'D')
       ax.fill(pdos_D_tot, energia, color = 'gray', alpha = transp)
       ax.plot(pdos_tot[5], energia, color = 'blue', linestyle = '-', linewidth = linew, label = r'${D}_{xy}$')
       ax.fill(pdos_tot[5], energia, color = 'blue', alpha = transp)
       ax.plot(pdos_tot[6], energia, color = 'red', linestyle = '-', linewidth = linew, label = r'${D}_{yz}$')
       ax.fill(pdos_tot[6], energia, color = 'red', alpha = transp)
       ax.plot(pdos_tot[7], energia, color = 'limegreen', linestyle = '-', linewidth = linew, label = r'${D}_{z^{2}}$')
       ax.fill(pdos_tot[7], energia, color = 'limegreen', alpha = transp)
       ax.plot(pdos_tot[8], energia, color = 'rosybrown', linestyle = '-', linewidth = linew, label = r'${D}_{xz}$')
       ax.fill(pdos_tot[8], energia, color = 'rosybrown', alpha = transp)
       ax.plot(pdos_tot[9], energia, color = 'magenta', linestyle = '-', linewidth = linew, label = r'${D}_{x^{2}}$')
       ax.fill(pdos_tot[9], energia, color = 'magenta', alpha = transp)

    # Destacando a energia de Fermi na estrutura de Bandas ================

    plt.plot([x_inicial, x_final], [0.0, 0.0], color = 'gray', linestyle = '-', linewidth = 0.1, alpha = 1.0)

    #======================================================================

    plt.xlim((x_inicial, x_final))
    plt.ylim((E_min, E_max))

    plt.xlabel("Density of States")
    plt.ylabel('$E-E_{f}$ (eV)')

    ax.set_box_aspect(1.25/1)
    ax.legend(loc="upper right", title="")
    # ax.legend(loc="best", title="")

    if (l == 1): 
       if (save_png == 1): plt.savefig('saida/DOS/DOS_PDOS.png', dpi = 300)
       if (save_pdf == 1): plt.savefig('saida/DOS/DOS_PDOS.pdf', dpi = 300)
       if (save_eps == 1): plt.savefig('saida/DOS/DOS_PDOS.eps', dpi = 300)

    if (l == 2): 
       if (save_png == 1): plt.savefig('saida/DOS/PDOS_P.png', dpi = 300)
       if (save_pdf == 1): plt.savefig('saida/DOS/PDOS_P.pdf', dpi = 300)
       if (save_eps == 1): plt.savefig('saida/DOS/PDOS_P.eps', dpi = 300)

    if (l == 3): 
       if (save_png == 1): plt.savefig('saida/DOS/PDOS_D.png', dpi = 300)
       if (save_pdf == 1): plt.savefig('saida/DOS/PDOS_D.pdf', dpi = 300)
       if (save_eps == 1): plt.savefig('saida/DOS/PDOS_D.eps', dpi = 300)

    # plt.show()  
   
#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------

#######################################################################
#######################################################################
#######
####### FIM DO CÓDIGO #################################################
#######
#######################################################################
#######################################################################
