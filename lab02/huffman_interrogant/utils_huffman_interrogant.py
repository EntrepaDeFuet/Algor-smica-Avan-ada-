def gradable(func):
    def receiver(*args, **kwargs):
        if "grading" in kwargs:
            kwargs.pop("grading")
            counts, vocabulari, _, decodi = func(*args, **kwargs)
            if isinstance(vocabulari, dict):
                return [counts, sorted(list(vocabulari.keys())), decodi]
            else:
                print("vocabulari must be of type dict." )
                return False
        else:
            counts, vocabulari, codi, decodi = func(*args, **kwargs)
            print("Text amb el vocabulari a codificar:", args[0])
            print("Diccionari de freqüències:", counts)
            print("Diccionari de conversió:", vocabulari)
            print("Missatge a codificar:", args[1])
            print("Codificat:", codi)
            print("Decodificat:", decodi)
    return receiver