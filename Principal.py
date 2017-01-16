# =============================================================================
# Titre : Principal.py
# Description : Librairie permettant d'encoder et de décoder des chaines selon 
# divers types d'encodage.
# Auteur : Nicolas Bisson
# Date : 2015/02/23
# Version : 1.0
# Usage : python3 Principal.py
# Notes :
# python_version : 3.4.0
# =============================================================================

def encodeur(distance, chaine):
    ''' Fonction qui prends une chaine de caractère et l'encode selon
        la distance déterminée par l'usager. Elle retourne la chaine, encodée ou
        décodée, dans une liste.
    '''
    minuscule = "abcdefghijklmnopqrstuvwxyz"
    majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if isinstance(distance, str or float or list):
        raise ValueError("La distance doit être un entier positif")
    if isinstance(chaine, int or float):
        raise ValueError("Le message doit être une chaine de caractère")
    listeChaine = list(chaine)
    for lettre in range(len(listeChaine)):
        if listeChaine[lettre] in minuscule:
            positionLettre = minuscule.index(listeChaine[lettre])
            listeChaine[lettre] = minuscule[(positionLettre + distance)%26]
        elif listeChaine[lettre] in majuscule:
            positionLettre = majuscule.index(listeChaine[lettre])
            listeChaine[lettre] = majuscule[(positionLettre + distance)%26]
        else:
            pass
    chaine = "".join(listeChaine)
    return chaine
        
def creerEncodeurCesar(distance):
    ''' Fonction qui prends la distance d'encodage de César et qui retourne
        une fonction lambda permettant l'encodage de la chaine.
    '''
    if isinstance(distance, str or float or list):
        raise ValueError("La distance doit être un entier positif")
    elif distance < 0:
        raise ValueError("La distance doit être un entier positif")
    encodeurC = lambda chaine: encodeur(distance, chaine)
    return encodeurC
   
def creerDecodeurCesar(distance):
    ''' Fonction qui prends la distance d'encodage de César et qui retourne
        une fonction lambda permettant le décodage de la chaine encodée.
    '''
    if isinstance(distance, str or float or list):
        raise ValueError("La distance doit être un entier positif")
    elif distance < 0:
        raise ValueError("La distance doit être un entier positif")
    decodeurC =  lambda listeChaine: encodeur((distance*-1), listeChaine)
    return decodeurC

def creerRot13():
    ''' Fonction qui retourne une fonction lambda permettant l'encodage et
        le décodage à l'aide de la méthode de César, mais avec une distance de 13.
    '''
    encodeurDecodeurROT = lambda chaine: encodeur(13, chaine)
    return encodeurDecodeurROT

def substitutionneur(substitution, chaine, minuscule):
    ''' Fonction qui prends une chaine de caractère et l'encode selon
        la liste prédéterminée. Elle retourne la chaine, encodée, dans une liste.
    '''
    if len(substitution) < 26 or len(substitution) > 26:
        raise ValueError("La chaine de substitution doit avoir 26 caractères")
    if isinstance(substitution, int or float):
        raise ValueError("La chaine de substitution doit être un string")
    if isinstance(chaine, int or float):
        raise ValueError("Le message doit être une chaine de caractère")
    listeChaine = list(chaine)
    for lettre in range(len(listeChaine)):
        if listeChaine[lettre].lower() in substitution:
            positionLettre = minuscule.index(listeChaine[lettre].lower())
            if str.isupper(listeChaine[lettre]):
                listeChaine[lettre] = (substitution[positionLettre]).upper()
            elif str.islower(listeChaine[lettre]):
                listeChaine[lettre] = substitution[positionLettre]
        else:
            pass
    chaine = "".join(listeChaine)
    return chaine

def creerEncodeurSubstitution(substitution):
    ''' Fonction qui prends une liste prédéterminée et retourne une fonction
        lambda permettant d'encoder une chaine selon cette liste.
    '''
    if len(substitution) < 26 or len(substitution) > 26:
        raise ValueError("La chaine de substitution doit avoir 26 caractères")
    if isinstance(substitution, int or float):
        raise ValueError("La chaine de substitution doit être un string")
    minuscule = "abcdefghijklmnopqrstuvwxyz"
    encodeurS = lambda chaine: substitutionneur(substitution, chaine, minuscule)
    return encodeurS
    
def creerDecodeurSubstitution(encodeurS):
    ''' Fonction qui prends une liste prédéterminée et retourne une fonction
        lambda permettant de décoder une chaine selon cette liste.
    '''
    if callable(encodeurS):
        minuscule = "abcdefghijklmnopqrstuvwxyz"
        decodeurS = lambda chaineSub: substitutionneur(minuscule, chaineSub, \
                                                       encodeurS(minuscule))
    else:
        raise ValueError("L'argument doit être une fonction lambda")
    return decodeurS

def encrypterFichier(fichier):
    ligneStr = ""
    fichier = open(fichier, mode = "r")
    for ligne in fichier:
        ligneStr += ligne
    fichier.close()
    return ligneStr
    
def crypterFichiers(fonctionLambda, *fichiers):
    ''' Fonction qui permet d'encoder ou de décoder, selon le type
        d'encodage/décodage choisi, ce qu'il y a dans le fichier et de
        le remplacer par la chaine crypter ou décrypter.
    '''
    if fichiers == ():
        raise ValueError("Il doit y avoir au minimum un fichier")
    if callable(fonctionLambda):
        listeFichier = []
        for nbFichier in fichiers: 
            listeFichier.append(encrypterFichier(nbFichier))
        print(listeFichier)
    else:
        raise ValueError("L'argument doit être une fonction lambda") 
    for fichier in fichiers:
        nouvFichier = open(fichier, mode = "w", encoding = "UTF-8")
        nouvFichier.write(fonctionLambda(fichier))
        nouvFichier.close() 