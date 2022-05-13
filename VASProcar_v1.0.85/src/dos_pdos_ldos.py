
def execute_python_file(filename: str):
   return exec(open(main_dir + str(filename)).read(), globals())

#---------------------------------------------------------------------
# Verificando se a pasta "DOS" existe, se não existe ela é criada ----
#---------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/DOS'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/DOS')
#-------------------------------------

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================
execute_python_file(filename = 'informacoes.py')

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("################### Densidade de Estados: ####################")
print ("##############################################################") 
print (" ")

if (escolha == -1):

   print ("##############################################################")
   print ("Quanto a energia, o que vc deseja? ===========================")
   print ("[0] Manter o valor padrao de saida do VASP ===================")
   print ("[1] Deslocar o nivel de Fermi para 0.0 eV ====================")
   print ("##############################################################") 
   esc_fermi = input (" "); esc_fermi = int(esc_fermi)
   print (" ")    

   print ("##############################################################")
   print ("O que vc deseja Plotar/Analisar? =============================")
   print ("Digite 0 para analisar todos os ions da rede =================")
   print ("Digite 1 para analisar ions selecionados =====================")
   print ("##############################################################")
   esc = input (" "); esc = int(esc)
   print(" ")

   if (esc == 1):
      
      sim_nao = ["nao"]*(ni + 1)  #  Inicialização do vetor sim_nao
      
      print ("##############################################################")
      print ("Os ions sao selecionados por meio de intervalos ============= ")
      print ("Quantos intervalos voce deseja fornecer? ==================== ")
      print ("##############################################################")
      loop = input (" "); loop = int(loop)
   
      print (" ")
      print ("##############################################################")
      print ("Para cada intervalo, informe os ions inicial e final: ======= ")
      print ("Digite como nos exemplos abaixo ============================= ")
      print ("--------------------------------------------------------------")
      print ("ion_inicial ion_final: 3 11                                   ")
      print ("ion_inicial ion_final: 9 9                                    ")
      print ("##############################################################")
      print (" ")
       
      for i in range (1,(loop+1)):
          print (f'{i} intervalo: ==============================================') 
          loop_i, loop_f = input ("ion_inicial ion_final: ").split()
          loop_i = int(loop_i)
          loop_f = int(loop_f)
          print (" ")
       
          if (loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0):
             print (" ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("   ERRO: Os valores de ions informados estao incorretos   ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             confirmacao = input (" ")
             exit()
          
          for i in range(loop_i, (loop_f + 1)):
             sim_nao[i] = "sim"

      print (" ")

if (escolha == 1):
   esc_fermi = 1  
   esc = 0

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0    

#----------------------------------------------------------------------
# Extraindo os resultados do arquivo DOSCAR ---------------------------
#----------------------------------------------------------------------

#---------------------------
doscar = open("DOSCAR", "r")
#---------------------------

for i in range(6):
    VTemp = doscar.readline().split()

E_max = float(VTemp[0])
E_min = float(VTemp[1])
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
      energia[i] = float(VTemp[0])
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
        if (dos[j] >= x_final):   x_final = dos[j]         
               
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
       #-------------------------------------------------------------------------------
       if (esc == 0): dos_pdos = open(dir_files + '/output/DOS/DOS_pDOS.agr', 'w')
       if (esc == 1): dos_pdos = open(dir_files + '/output/DOS/DOS_pDOS_lDOs.agr', 'w')
       #-------------------------------------------------------------------------------
       print ("=================================") 
       print ("Analisando a DOS e pDOS (S, P, D)")        
       s = 1; t = (3+1); r = 4
       
    if (i == 2):
       #-----------------------------------------------------------------------------
       if (esc == 0): dos_pdos = open(dir_files + '/output/DOS/pDOS_P.agr', 'w')
       if (esc == 1): dos_pdos = open(dir_files + '/output/DOS/pDOS_lDOS_P.agr', 'w') 
       #-----------------------------------------------------------------------------
       print ("Analisando a pDOS (Px, Py, Pz)") 
       s = 4; t = (6+1); r = 4
       
    if (i == 3):
       #-----------------------------------------------------------------------------
       if (esc == 0): dos_pdos = open(dir_files + '/output/DOS/pDOS_D.agr', 'w')
       if (esc == 1): dos_pdos = open(dir_files + '/output/DOS/pDOS_lDOS_D.agr', 'w')
       #-----------------------------------------------------------------------------
       print ("Analisando a pDOS (Dxy, Dyz, Dz2, Dxz, Dx2)") 
       s = 7; t = (11+1); r = 6   

# Escrita do arquivo ".agr" do GRACE ===================================

    dos_pdos.write("# Grace project file \n")
    dos_pdos.write("# written using VASProcar (https://github.com/Augusto-Dlelis/VASProcar-Tools-Python) \n") 
    dos_pdos.write("# \n")
    dos_pdos.write("@version 50122 \n")
    dos_pdos.write("@with g0 \n")
    dos_pdos.write(f'@    world {x_inicial}, {y_inicial + dE_fermi}, {x_final}, {y_final + dE_fermi} \n')
    dos_pdos.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

    escala_x = (x_final - x_inicial)/5
    escala_y = (y_final - y_inicial)/5

    dos_pdos.write(f'@    xaxis  tick major {escala_x:.2f} \n')
    dos_pdos.write(f'@    xaxis  label "Density of States" \n')    
    dos_pdos.write(f'@    yaxis  tick major {escala_y:.2f} \n')

    if (esc_fermi == 0):
       dos_pdos.write(f'@    yaxis  label "E (eV)" \n')
    if (esc_fermi == 1):
       dos_pdos.write(f'@    yaxis  label "E-Ef (eV)" \n')    

    dos_pdos.write(f'@    legend loctype world \n')
    dos_pdos.write(f'@    legend {x_inicial}, {y_final + dE_fermi} \n')
    dos_pdos.write(f'@    legend box fill pattern 4 \n')
    dos_pdos.write(f'@    legend length 1 \n')

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
    dos_pdos.write(f'@    s{r} line linestyle 3 \n')
    dos_pdos.write(f'@    s{r} line linewidth 2.0 \n')
    dos_pdos.write(f'@    s{r} line color 7 \n')

    dos_pdos.write("@type xy")
    dos_pdos.write(" \n")
      
# Plot da DOS e pDOS ======================================================

    for l in range(1,(6+1)):
        for k in range (1,(NEDOS+1)):
            #-------------------------------------------------------------------------------------
            if (i == 1 and l == 1): dos_pdos.write(f'{dos[k]} {energia[k] + dE_fermi} \n')
            if (esc == 1 and (i == 1 and l == 2)): dos_pdos.write(f'{l_dos[k]} {energia[k] + dE_fermi} \n')            
            if (i == 1 and l == 3): dos_pdos.write(f'{pdos_tot[1][k]} {energia[k] + dE_fermi} \n')
            if (i == 1 and l == 4): dos_pdos.write(f'{pdos_P_tot[k]} {energia[k] + dE_fermi} \n')
            if (i == 1 and l == 5): dos_pdos.write(f'{pdos_D_tot[k]} {energia[k] + dE_fermi} \n')
            #-------------------------------------------------------------------------------------
            if (i == 2 and l == 1): dos_pdos.write(f'{pdos_P_tot[k]} {energia[k] + dE_fermi} \n')
            if (i == 2 and l == 2): dos_pdos.write(f'{pdos_tot[4][k]} {energia[k] + dE_fermi} \n')
            if (i == 2 and l == 3): dos_pdos.write(f'{pdos_tot[2][k]} {energia[k] + dE_fermi} \n')
            if (i == 2 and l == 4): dos_pdos.write(f'{pdos_tot[3][k]} {energia[k] + dE_fermi} \n')
            #-------------------------------------------------------------------------------------
            if (i == 3 and l == 1): dos_pdos.write(f'{pdos_D_tot[k]} {energia[k] + dE_fermi} \n') 
            if (i == 3 and l == 2): dos_pdos.write(f'{pdos_tot[5][k]} {energia[k] + dE_fermi} \n')
            if (i == 3 and l == 3): dos_pdos.write(f'{pdos_tot[6][k]} {energia[k] + dE_fermi} \n')
            if (i == 3 and l == 4): dos_pdos.write(f'{pdos_tot[7][k]} {energia[k] + dE_fermi} \n')
            if (i == 3 and l == 5): dos_pdos.write(f'{pdos_tot[8][k]} {energia[k] + dE_fermi} \n')           
            if (i == 3 and l == 6): dos_pdos.write(f'{pdos_tot[9][k]} {energia[k] + dE_fermi} \n')
        dos_pdos.write(" \n")

# Destacando a energia de Fermi na estrutura de Bandas ================

    dos_pdos.write(" \n")
    dos_pdos.write(f'{x_inicial} {dest_fermi} \n')
    dos_pdos.write(f'{x_final} {dest_fermi} \n')
      
    #---------------
    dos_pdos.close()
    #--------------- 

#======================================================================
#======================================================================
# Plot da DOS, pDOS e lDOS ============================================
#====================================================================== 
#======================================================================

# Gravando as informações para o Plot da DOS, pDOS e lDOS =============

#---------------------------------------------------------------------
dos_pdos_ldos = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.dat', 'w')
#---------------------------------------------------------------------

for k in range (1,(NEDOS+1)):
    #---------------------------------------------------------------------------
    if (esc == 0): dos_pdos_ldos.write(f'{energia[k]} {dos[k]} 0.0')
    if (esc == 1): dos_pdos_ldos.write(f'{energia[k]} {dos[k]} {l_dos[k]}')
    dos_pdos_ldos.write(f' {pdos_tot[1][k]} {pdos_P_tot[k]} {pdos_D_tot[k]}')
    if (lorbit > 10): dos_pdos_ldos.write(f' {pdos_tot[4][k]} {pdos_tot[2][k]} {pdos_tot[3][k]} {pdos_tot[5][k]} {pdos_tot[6][k]} {pdos_tot[7][k]} {pdos_tot[8][k]} {pdos_tot[9][k]}')
    dos_pdos_ldos.write(f' \n')       

#--------------------
dos_pdos_ldos.close()
#--------------------

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Copiando o codigo DOS_pDOS_lDOS.py para o diretório de saida --------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

# Teste para saber se o arquivo DOS_pDOS_lDOS.py já se encontra no diretorio de saida
try: f = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py'); f.close(); os.remove(dir_files + '/output/DOS/DOS_pDOS_lDOS.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_dos_pdos_ldos.py'
destination = dir_files + '/output/DOS/DOS_pDOS_lDOS.py'
shutil.copyfile(source, destination)

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código DOS_pDOS_lDOS.py' possa ser executado isoladamente ---
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

file = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py', 'r')
lines = file.readlines()
file.close()

linha = 4

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '# Parâmetros para que o código possa ser executado isoladamente ====== \n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, f'n_procar = {n_procar}; nk  = {nk}; x_inicial = {x_inicial}; x_final = {x_final}; energ_min = {y_inicial}; energ_max = {y_final}; lorbit = {lorbit}; esc = {esc} \n')
linha += 1; lines.insert(linha, f'Efermi = {Efermi}  #  Valor da energia de Fermi obtida no arquivo OUTCAR \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Escolha quanto aos valores de energia. onde: [0] adotar a saida do VASP e [1] adotar o nivel de Fermi como 0.0eV \n')
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Formato em que o plot da projeção sera salvo, onde [0] = NAO e [1] = SIM \n')                       
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py', 'w')
file.writelines(lines)
file.close()

#------------------------------------------------------------
exec(open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py').read())
#------------------------------------------------------------
