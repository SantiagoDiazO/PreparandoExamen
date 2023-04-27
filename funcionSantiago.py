def clasificarCandidato(numeroCarreras, numeroVictorias):
    if numeroCarreras >= 100:
        if numeroVictorias >= 10:
            return True
        else:
            return False
    else:
        return False