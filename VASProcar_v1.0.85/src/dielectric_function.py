
#-----------------------------------------------------------------------
# Verificando se a pasta "BSE" existe, se não existe ela é criada -----
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/BSE'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/BSE')
#-------------------------------------

print ("##############################################################")
print ("################# Plot da Funcao Dieletrica: #################")
print ("##############################################################")
print (" ")

#======================================================================
# Verificando a presenca do arquivo vasprun.xml =======================
#======================================================================

try:
    f = open(dir_files + '/vasprun.xml')
    f.close()
except:
    print('----------------------------------------------------------------------------------------')
    print('Arquivo vasprun.xml ausente no diretorio, insira o arquivo e aperte ENTER para continuar')
    print('----------------------------------------------------------------------------------------')
    confirmacao = input (" "); confirmacao = str(confirmacao)   

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

if (escolha == -1):
   
   print ("##############################################################")
   print ("Deseja escolher o range de energia do Plot? ==================")
   print ("[0] NAO                                                       ")
   print ("[1] SIM                                                       ")
   print ("##############################################################") 
   esc_energ = input (" "); esc_energ = int(esc_energ)
   print (" ")
 
   if (esc_energ == 1):
      print ("##############################################################")
      print ("Informe os dois valores de energia do intervalo: =============")
      print ("Digite como nos exemplos abaixo ==============================")
      print ("--------------------------------------------------------------")
      print ("E_inicial E_final: -5.0 3.5                                   ")
      print ("E_inicial E_final:  1.0 9.8                                   ")
      print ("##############################################################") 
      print (" ")
      x_inicial, x_final = input ("E_inicial E_final: ").split()
      x_inicial = float(x_inicial)
      x_final   = float(x_final)
      print (" ") 
   
print ("##############################################################")
print ("Qual o valor da energia de Fermi? ============================")
print ("##############################################################") 
Efermi = input (" "); Efermi = float(Efermi)
print (" ")

if (escolha == -1):
   print ("##############################################################")
   print ("Quanto a energia, o que vc deseja? ===========================")
   print ("[0] Manter o valor padrao de saida do VASP ===================")
   print ("[1] Deslocar o nivel de Fermi para 0.0 eV ====================")
   print ("##############################################################") 
   esc_fermi = input (" "); esc_fermi = int(esc_fermi)
   print (" ")  

if (escolha == 1):
   esc_fermi = 1
   esc_energ = 0

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0

#----------------------------------------------------------------------
# Extraindo os resultados do arquivo vasprun.xml ----------------------
#----------------------------------------------------------------------

print (".........................................................")
print (".............. Lendo o arquivo vasprun.xml ..............")
print ("................... Espere um momento ...................")
print (".........................................................")

#----------------------------------------------
vasprun = open(dir_files + '/vasprun.xml', 'r')
#----------------------------------------------

palavra = '<imag>'  
for line in vasprun:   
    if palavra in line: 
       break

palavra = '<set>'
for line in vasprun:   
    if palavra in line: 
       break

passo = -1

palavra = '</set>'
for line in vasprun:
    passo += 1
    if palavra in line: 
       break

#--------------
vasprun.close()
#--------------

#==============================================

#----------------------------------------------
vasprun = open(dir_files + '/vasprun.xml', 'r')
#----------------------------------------------

palavra = '<imag>'  
for line in vasprun:   
    if palavra in line: 
       break

palavra = '<set>'
for line in vasprun:   
    if palavra in line: 
       break

#----------------------------------------------

energ = [0.0]*passo
X_i   = [0.0]*passo;  X_r  = [0.0]*passo
Y_i   = [0.0]*passo;  Y_r  = [0.0]*passo
Z_i   = [0.0]*passo;  Z_r  = [0.0]*passo
XY_i  = [0.0]*passo;  XY_r = [0.0]*passo
YZ_i  = [0.0]*passo;  YZ_r = [0.0]*passo
ZX_i  = [0.0]*passo;  ZX_r = [0.0]*passo
media_i  = [0.0]*passo;  media_r  = [0.0]*passo
modulo_i = [0.0]*passo;  modulo_r = [0.0]*passo

#----------------------------------------------

for i in range(passo):
    VTemp = vasprun.readline().split()
    energ[i] = float(VTemp[1])
    X_i[i]   = float(VTemp[2])
    Y_i[i]   = float(VTemp[3])
    Z_i[i]   = float(VTemp[4])
    media_i[i]  = (X_i[i] + Y_i[i] + Z_i[i])/3
    modulo_i[i] = ((X_i[i]**2) + (Y_i[i]**2) + (Z_i[i]**2))**0.5
    # XY_i[i]  = float(VTemp[5])
    # YZ_i[i]  = float(VTemp[6])
    # ZX_i[i]  = float(VTemp[7])

palavra = '<set>'
for line in vasprun:   
    if palavra in line: 
       break

for i in range(passo):
    VTemp = vasprun.readline().split()
    X_r[i]   = float(VTemp[2])
    Y_r[i]   = float(VTemp[3])
    Z_r[i]   = float(VTemp[4])
    media_r[i]  = (X_r[i] + Y_r[i] + Z_r[i])/3
    modulo_r[i] = ((X_r[i]**2) + (Y_r[i]**2) + (Z_r[i]**2))**0.5
    # XY_r[i]  = float(VTemp[5])
    # YZ_r[i]  = float(VTemp[6])
    # ZX_r[i]  = float(VTemp[7])

#--------------
vasprun.close()
#--------------

#======================================================================
# Gravando dados para o Plot da Função Dieletrica: ====================
#======================================================================     

#-------------------------------------------------
BSE = open(dir_files + '/output/BSE/BSE.dat', 'w')
#-------------------------------------------------

for i in range (passo):
    BSE.write(f'{energ[i]}')
    BSE.write(f' {modulo_i[i]} {media_i[i]}')
    BSE.write(f' {X_i[i]} {Y_i[i]} {Z_i[i]}')
    # BSE.write(f' {XY_i[i]} {YZ_i[i]} {ZX_i[i]}')
    BSE.write(f' {media_r[i]} {modulo_r[i]}')
    BSE.write(f' {X_r[i]} {Y_r[i]} {Z_r[i]}')
    # BSE.write(f' {XY_r[i]} {YZ_r[i]} {ZX_r[i]}')
    BSE.write(f' \n')
    
#----------
BSE.close()
#----------



#======================================================================
#======================================================================
# Plot da Funcao Dieletrica (GRACE) ===================================
#====================================================================== 
#======================================================================

import numpy as np

# Rotulos ============================================================= 

rot = [0]*(8)
rot[0] = 'Mod'; rot[1] = 'Med'
rot[2] = 'X'; rot[3] = 'Y'; rot[4] = 'Z'
# rot[5] = 'XY';     rot[6] = 'YZ';    rot[7] = 'ZX'

# Cores ===============================================================

# Codigo de cores do GRACE
# Branco  = 0,  Preto = 1, Vermelho = 2,  Verde   = 3,  Azul   = 4,  Amarelo = 5,  Marrom   = 6, Cinza = 7
# Violeta = 8,  Cyan  = 9, Magenta  = 10, Laranja = 11, Indigo = 12, Marron  = 13, Turquesa = 14

color = [0]*(8)
color[0] = '1'; color[1] = '10';  
color[2] = '4'; color[3] = '2'; color[4] = '3'
# color[5] = '9'; color[6] = '12'; color[7] = '14'

# =====================================================================

func_dielet = np.loadtxt(dir_files + '/output/BSE/BSE.dat') 
func_dielet.shape

energ = func_dielet[:,0]

# =====================================================================

if (esc_energ == 0):
   x_inicial = min(energ)
   x_final   = max(energ)
 
# =====================================================================

for i in range(2):
   
    y_inicial = +1000.0
    y_final   = -1000.0
   
    #---------------------------------------------------------------------------------
    if (i == 0): BSE = open(dir_files + '/output/BSE/Funcao_Dieletrica_IMAG.agr', 'w')
    if (i == 1): BSE = open(dir_files + '/output/BSE/Funcao_Dieletrica_REAL.agr', 'w')
    #---------------------------------------------------------------------------------

    for j in range(5):
        if (i == 0): m = (j +1)         
        if (i == 1): m = (j +6) 
        temp_min = min(func_dielet[:,m])
        temp_max = max(func_dielet[:,m])
        if (temp_min < y_inicial): y_inicial = temp_min
        if (temp_max > y_final):   y_final   = temp_max
    

    # Escrita dos arquivos ".agr" do GRACE ============================

    BSE.write("# Grace project file \n")
    BSE.write("# written using VASProcar (https://github.com/Augusto-Dlelis/VASProcar-Tools-Python) \n") 
    BSE.write("# \n")
    BSE.write("@version 50122 \n")
    BSE.write("@with g0 \n")
    BSE.write(f'@    world {x_inicial + dE_fermi}, {y_inicial}, {x_final + dE_fermi}, {y_final} \n')
    BSE.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

    escala_x = (x_final - x_inicial)/5
    escala_y = (y_final - y_inicial)/5

    BSE.write(f'@    xaxis  tick major {escala_x:.2f} \n')
    
    if (esc_fermi == 0): BSE.write(f'@    xaxis  label "E (eV)" \n')
    if (esc_fermi == 1): BSE.write(f'@    xaxis  label "E-Ef (eV)" \n')
    
    BSE.write(f'@    yaxis  tick major {escala_y:.2f} \n')
    BSE.write(f'@    yaxis  label "Funcao Dieletrica (BSE)" \n')       

    BSE.write(f'@    legend loctype world \n')
    BSE.write(f'@    legend {x_inicial + dE_fermi}, {y_final} \n')
    BSE.write(f'@    legend box fill pattern 4 \n')
    BSE.write(f'@    legend length 1 \n')

    for j in range(5):
        BSE.write(f'@    s{j} type xy \n')
        BSE.write(f'@    s{j} line type 1 \n')
        BSE.write(f'@    s{j} line color {color[j]} \n')
        BSE.write(f'@    s{j} line linewidth 2.0 \n')
        # BSE.write(f'@    s{j} fill type 1 \n')
        # BSE.write(f'@    s{j} fill color {color[j]} \n')
        # BSE.write(f'@    s{j} fill pattern 4 \n')
        BSE.write(f'@    s{j} legend  "{rot[j]}" \n')

    BSE.write(f'@    s{j+1} type xy \n')
    BSE.write(f'@    s{j+1} line type 1 \n')
    BSE.write(f'@    s{j+1} line linestyle 3 \n')
    BSE.write(f'@    s{j+1} line linewidth 2.0 \n')
    BSE.write(f'@    s{j+1} line color 7 \n')
    
    BSE.write(f'@    s{j+2} type xy \n')
    BSE.write(f'@    s{j+2} line type 1 \n')
    BSE.write(f'@    s{j+2} line linestyle 3 \n')
    BSE.write(f'@    s{j+2} line linewidth 2.0 \n')
    BSE.write(f'@    s{j+2} line color 7 \n')
        
    BSE.write("@type xy")
    BSE.write(" \n")

    # Plot das componentes da Função Dielétrica =======================

    for j in range(5):
        #---------------------------------------
        if (i == 0): temp = func_dielet[:,(j+1)]
        if (i == 1): temp = func_dielet[:,(j+6)]
        #---------------------------------------
        for k in range (passo):
            BSE.write(f'{energ[k] + dE_fermi} {temp[k]} \n')
        BSE.write(" \n")

    # Destacando a energia de Fermi na estrutura de Bandas ============
   
    BSE.write(f'{dest_fermi} {y_inicial} \n')
    BSE.write(f'{dest_fermi} {y_final} \n')
    BSE.write(" \n")
    
    # Destacando o valor nulo da Função Dieletrica ====================

    BSE.write(f'{x_inicial + dE_fermi} 0.0 \n')
    BSE.write(f'{x_final + dE_fermi} 0.0 \n')          
    BSE.write(" \n")

    #----------
    BSE.close()
    #----------



#=================================================================================
#=================================================================================
# Plot 2D da Funcao Dieletrica (BSE) (Matplotlib) ================================
#================================================================================= 
#=================================================================================     

#------------------------------------------------------------------------
#------------------------------------------------------------------------
# Copiando o codigo Dielectric_Function.py para o diretório de output ---
#------------------------------------------------------------------------
#------------------------------------------------------------------------

# Teste para saber se o arquivo Densidade.py já se encontra no diretorio de output
try: f = open(dir_files + '/output/BSE/Dielectric_Function.py'); f.close(); os.remove(dir_files + '/output/BSE/Dielectric_Function.py')
except: 0 == 0
  
source = main_dir + '/plot/plot_dielectric_function.py'
destination = dir_files + '/output/BSE/Dielectric_Function.py'
shutil.copyfile(source, destination)

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código Densidade.py possa ser executado isoladamente ---
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

file = open(dir_files + '/output/BSE/Dielectric_Function.py', 'r')
lines = file.readlines()
file.close()

linha = 4

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '# Parâmetros para que o código possa ser executado isoladamente ====== \n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, f'Efermi = {Efermi}  #  Valor da energia de Fermi obtida no arquivo OUTCAR \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Escolha quanto aos valores de energia. onde: [0] adotar a saida do VASP e [1] adotar o nivel de Fermi como 0.0eV \n')
linha += 1; lines.insert(linha, f'esc_energ = {esc_energ}  #  Escolha quanto a opção de analisar ou não um determinado range de energia, onde: [0] NAO e [1] SIM \n')
linha += 1; lines.insert(linha, f'x_inicial = {x_inicial}; x_final = {x_final}  #  Valore inicial e final do range de energia, vinculada a opção acima \n')
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Formato em que o plot da banda sera salvo, onde [0] = NAO e [1] = SIM \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/BSE/Dielectric_Function.py', 'w')
file.writelines(lines)
file.close()

#------------------------------------------------------------------
exec(open(dir_files + '/output/BSE/Dielectric_Function.py').read())
#------------------------------------------------------------------
