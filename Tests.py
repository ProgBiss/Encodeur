# =============================================================================
# Titre : Principal.py
# Description : Jeux de tests pour vérifier la validité des entrées de la 
# librairie.
# Auteur : Nicolas Bisson
# Date : 2015/02/23
# Version : 1.0
# Usage : python3 Principal.py
# Notes :
# python_version : 3.4.0
# =============================================================================

from Principal import creerEncodeurCesar, creerDecodeurCesar,\
    creerEncodeurSubstitution, creerRot13, creerDecodeurSubstitution,\
    crypterFichiers

def testsCreerEncodeurCesar():
    ''' Jeux de tests pour la fonction "creerEncodeurCesar".
    '''
    isPassed = True
    try:
        creerEncodeurCesar("Bonjour")
        isPassed = False
        print("Échec du test creerEncodeurCesar: Type non valide")
    except:
        pass
    try:
        creerEncodeurCesar(-1)
        isPassed = False
        print("Échec du test creerEncodeurCesar: Valeur non valide")
    except:
        pass
    retour = creerEncodeurCesar(0)
    if not callable(retour):
        isPassed = False
        print("Échec du test creerEncodeurCesar: Type non valide")
    if isPassed:
        print("Test creerEncodeurCesar s'est correctement effectué")    
         
def testsCreerDecodeurCesar():
    ''' Jeux de tests pour la fonction "creerDecodeurCesar".
    '''
    isPassed = True
    try:
        creerDecodeurCesar("Bonjour")
        isPassed = False
        print("Échec du test creerDecodeurCesar: Type non valide")
    except:
        pass
    try:
        creerDecodeurCesar(-1)
        isPassed = False
        print("Échec du test creerDecodeurCesar: Valeur non valide")
    except:
        pass
    retour = creerDecodeurCesar(0)
    if not callable(retour):
        isPassed = False
        print("Échec du test creerDecodeurCesar: Type non valide")
    if isPassed:
        print("Test creerDecodeurCesar s'est correctement effectué")    
        
def testsCreerRot13():
    ''' Jeux de tests pour la fonction "creerRot13".
    '''
    isPassed = True
    retour = creerRot13()
    if not callable(retour):
        isPassed = False
        print("Échec du test creerRot13: Type non valide")
    if isPassed:
        print("Test creerRot13 s'est correctement effectué")

def testsCreerEncodeurSubstitution():
    ''' Jeux de tests pour la fonction "creerEncodeurSubstitution".
    '''
    isPassed = True
    try:
        creerEncodeurSubstitution(420)
        isPassed = False
        print("Échec du test creerEncodeurSubstitution: Type non valide")
    except:
        pass
    try:
        creerEncodeurSubstitution("abcdef")
        isPassed = False
        print("Échec du test creerEncodeurSubstitution: Valeur non valide")
    except:
        pass
    try:
        creerEncodeurSubstitution("abcdefghijklmnopqrstuvwxyzg")
        isPassed = False
        print("Échec du test creerEncodeurSubstitution: Valeur non valide")
    except:
        pass
    retour = creerEncodeurSubstitution("zmqpalxnwoskcbeidjvruhfgty")
    if not callable(retour):
        isPassed = False
        print("Échec du test creerEncodeurSubstitution: Type non valide")
    if isPassed:
        print("Test creerEncodeurSubstitution s'est correctement effectué")
        
def testsCreerDecodeurSubstitution():
    ''' Jeux de tests pour la fonction "creerDecodeurSubstitution".
    '''
    isPassed = True
    try:
        creerDecodeurSubstitution("Bonjour")
        isPassed = False
        print("Échec du test creerDecodeurSubstitution: Type non valide")
    except:
        pass
    try:
        creerDecodeurSubstitution(1337)
        isPassed = False
        print("Échec du test creerDecodeurSubstitution: Type non valide")
    except:
        pass
    retour = creerDecodeurSubstitution \
        (creerEncodeurSubstitution("zmqpalxnwoskcbeidjvruhfgty"))
    if not callable(retour):
        isPassed = False
        print("Échec du test creerDecodeurSubstitution: Type non valide")
    if isPassed:
        print("Test creerDecodeurSubstitution s'est correctement effectué")
    

def testsCrypterFichiers():
    ''' Jeux de tests pour la fonction "crypterFichiers".
    '''
    isPassed = True
    try:
        crypterFichiers("Salut", "fichier.txt")
        isPassed = False
        print("Échec du test creerCrypterFichiers: Type non valide")
    except:
        pass
    try:
        crypterFichiers(99, 35)
        isPassed = False
        print("Échec du test creerCrypterFichiers: Type non valide")
    except: 
        pass
    testLambda = crypterFichiers
    if not callable(testLambda):
        isPassed = False
        print("Échec du test crypterFichiers: Type non valide")
    if isPassed:
        print("Test crypterFichiers s'est correctement effectué")