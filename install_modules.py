
import subprocess

#==========================================================

print(" ")
print("Instalação/Atualização dos Modulos")
print(" ")

#==========================================================

# package_list_to_instal ----------------------------------
packages = [
"pip",
"os", 
"sys",
"shutil",
"numpy", 
"scipy", 
"matplotlib", 
"plotly",
"moviepy"
]

for i in range(len(packages)):
	subprocess.run(["pip", "install", "--upgrade", packages[i]])
	print("[OK] " + packages[i])

#==========================================================

print(" ")
print("Instalação/Atualização dos Modulos concluida")
print(" ")

#==========================================================
