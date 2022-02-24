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

#======================================================================
# Obtendo o nº pontos-k a serem destacados na estrutura de Bandas =====
#======================================================================

#------------------------------------------
inform = open("saida/informacoes.txt", "r")
#------------------------------------------

palavra = 'Pontos-k |'                          

for line in inform:   
    if palavra in line: 
       break

VTemp = inform.readline()
VTemp = inform.readline()
       
nk_total = nk*n_procar   # Nº total de pontos-k da banda
contador2 = 0
n_pk = []                # Vetor formado pelos indices dos pontos-k selecionados
dest_pk = []             # Vetor formado pelas coordenadas no eixo-x do plot dos pontos-k selecionados

dest_pk.append(0.0); n_pk.append(1)

for i in range (nk_total):
    VTemp = inform.readline().split()
    r1 = int(VTemp[0]); r2 = float(VTemp[1]); r3 = float(VTemp[2]); r4 = float(VTemp[3]); comprimento = float(VTemp[4])
    if (i != 0) and (i != (nk_total - 1)):  
       dif = comprimento - comprimento_old     
       if(dif == 0.0):
          contador2 += 1
          dest_pk.append(comprimento)
          n_pk.append(i+1)
    comprimento_old = comprimento

dest_pk.append(comprimento); n_pk.append(nk_total)
contador2 = contador2 + 2

#-------------
inform.close()
#-------------

#======================================================================
# Gerando o arquivo label.txt =========================================
#======================================================================

if (dest_k == 2):

   #-----------------------------
   label = open("label.txt", "w")
   #-----------------------------

   label.write(f'{contador2}                     ! Numero de pontos-k a serem rotulados \n')

# Criando uma lista com as letras de a-z ==============================

   lab = []

   for i in range(ord('a'), ord('z') + 1): # lista as letras de a-z
       lab.append(chr(i))

#======================================================================

   for i in range (contador2):
       label.write(f'{dest_pk[i]:<18,.14f} {lab[i]}  ! Point-k {n_pk[i]} \n')

#======================================================================

   label.write(f' \n')
   label.write(f'Na edicao deste arquivo, vc pode alterar o número de pontos-k a serem rotulados. \n')
   label.write(f'A coordenada de cada ponto-k pode ser encontrada no arquivo saida/informacoes.txt \n')
   label.write(f' \n')
   label.write(f'===================================================================================================== \n')
   label.write(f'Simbolos gregos: https://www.infoescola.com/wp-content/uploads/2012/05/alfabeto-grego_173660282-1.jpg \n')
   label.write(f'Para inserir simbolos gregos como rotulo dos pontos-k, utilize a nomenclatura/numeracao abaixo:       \n')
   label.write(f'===================================================================================================== \n')
   label.write(f' \n')
   label.write("Gamma   =   [1]  |  gamma   =   [2]  |  Delta =   [3]  |  delta =   [4] \n") 
   label.write("Lambda  =   [5]  |  lambda  =   [6]  |  Sigma =   [7]  |  sigma =   [8] \n") 
   label.write("Theta   =   [9]  |  tetha   =  [10]  |  Omega =  [11]  |  omega =  [12] \n") 
   label.write("Psi     =  [13]  |  psi     =  [14]  |  Phi   =  [15]  |  phi   =  [16]  |  varphi =  [17] \n") 
   label.write("alfa    =  [18]  |  beta    =  [19]  |  pi    =  [20]  |  rho   =  [21] \n") 
   label.write("tau     =  [22]  |  upsilon =  [23]  |  mu    =  [24]  |  nu    =  [25] \n") 
   label.write("epsilon =  [26]  |  eta     =  [27]  |  kappa =  [28]  |  xi    =  [29]  |  zeta   =  [30] \n")
   label.write(f' \n')

   #------------
   label.close()
   #------------

#======================================================================
# Mensagem de aviso para o usuario editar o arquivo label.txt =========
#======================================================================

if (dest_k == 2):
   print (" ")
   print ("##############################################################")
   print ("Atencao: O arquivo label.txt foi gerado com sucesso, edite o  ")
   print ("         arquivo e confirme com um [OK] ou ENTER.             ")
   print ("==============================================================")
   print ("Consulte a coordenada dos pontos-k no arquivo informacoes.txt ")   
   print ("##############################################################")
   confirmacao = input (" "); confirmacao = str(confirmacao)

#======================================================================
# Leitura do arquivo label.txt para a obtencao dos rotulos dos pontos-k
#======================================================================

   #-----------------------------
   label = open("label.txt", "r")
   #-----------------------------

   VTemp = label.readline().split()
   contador2 = int(VTemp[0])

   dest_pk = []
   label_pk = []

   for i in range(contador2):
       VTemp = label.readline().split()
       dest_pk.append(float(VTemp[0]))
       label_pk.append(str(VTemp[1]))

   #------------
   label.close()
   #------------

#======================================================================
# Definindo as correspondentes nomenclaturas para o GRACE e Matplotlib
#======================================================================

   r_grace = []

   r_grace.append('\\f{Symbol}G'); r_grace.append('\\f{Symbol}g'); r_grace.append('\\f{Symbol}D')
   r_grace.append('\\f{Symbol}d'); r_grace.append('\\f{Symbol}L'); r_grace.append('\\f{Symbol}l')
   r_grace.append('\\f{Symbol}S'); r_grace.append('\\f{Symbol}s'); r_grace.append('\\f{Symbol}Q')
   r_grace.append('\\f{Symbol}q'); r_grace.append('\\f{Symbol}W'); r_grace.append('\\f{Symbol}w') 
   r_grace.append('\\f{Symbol}Y'); r_grace.append('\\f{Symbol}y'); r_grace.append('\\f{Symbol}F')
   r_grace.append('\\f{Symbol}f'); r_grace.append('\\f{Symbol}j'); r_grace.append('\\f{Symbol}a')
   r_grace.append('\\f{Symbol}b'); r_grace.append('\\f{Symbol}p'); r_grace.append('\\f{Symbol}r') 
   r_grace.append('\\f{Symbol}t'); r_grace.append('\\f{Symbol}u'); r_grace.append('\\f{Symbol}m')
   r_grace.append('\\f{Symbol}n'); r_grace.append('\\f{Symbol}e'); r_grace.append('\\f{Symbol}h')
   r_grace.append('\\f{Symbol}k'); r_grace.append('\\f{Symbol}x'); r_grace.append('\\f{Symbol}z')

#======================================================================

   r_matplot = []

   r_matplot.append('${\\Gamma}$'); r_matplot.append('${\\gamma}$');   r_matplot.append('${\\Delta}$')
   r_matplot.append('${\\delta}$'); r_matplot.append('${\\Lambda}$');  r_matplot.append('${\\lambda}$')
   r_matplot.append('${\\Sigma}$'); r_matplot.append('${\\sigma}$');   r_matplot.append('${\\Theta}$')
   r_matplot.append('${\\theta}$'); r_matplot.append('${\\Omega}$');   r_matplot.append('${\\omega}$') 
   r_matplot.append('${\\Psi}$');   r_matplot.append('${\\psi}$');     r_matplot.append('${\\Phi}$')
   r_matplot.append('${\\phi}$');   r_matplot.append('${\\varphi}$');  r_matplot.append('${\\alpha}$')
   r_matplot.append('${\\beta}$');  r_matplot.append('${\\pi}$');      r_matplot.append('${\\rho}$') 
   r_matplot.append('${\\tau}$');   r_matplot.append('${\\upsilon}$'); r_matplot.append('${\\mu}$')
   r_matplot.append('${\\nu}$');    r_matplot.append('${\\epsilon}$'); r_matplot.append('${\\eta}$')
   r_matplot.append('${\\kappa}$'); r_matplot.append('${\\xi}$');      r_matplot.append('${\\zeta}$')

#######################################################################
#######################################################################
#######
####### FIM DO CÓDIGO #################################################
#######
#######################################################################
#######################################################################
               
