'''Aucun module n'est appelé dans ce code là'''
#### Fonction secondaire


def ispalindrome(p):
    '''Fonction prenant en entrée un mot ou phrase et dit si c'est un palindrome ou non'''
    table = str.maketrans(
        'éèàçôêë',    # Caractères à traduire
        'eeacoee',    # Caractères de remplacement
        "&(-_)=+}]@^`[{#~,!:;'?./ "  # Caractères à supprimer
    )
    translated_text = p.lower().translate(table)

    return translated_text == translated_text[::-1]


#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))



if __name__ == "__main__":
    main()
