'''
Created on 4 nov. 2014

@author: etudiant
'''
def creationFichier(nom, ext, result):
    fichier=open(nom + "." + ext,'w')
    #Si l'extension du fichier est le m3u
    if ext == "m3u":
        fichier.write(for row in result:
                        )

    #Si l'extension du fichier est le xspf
    fichier.write("test")

    #Si l'extension du fichier est le pls
    fichier.write("test")

    fichier.close()

creationFichier("test", "m3u")