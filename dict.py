meme_dict = {}
meme_dict["CRINGE"]="Algo excepcionalmente raro o embarazoso"
meme_dict["LOL"]="Una respuesta común a algo gracioso"
meme_dict["CREEPY"]="Algo aterrador, siniestro"

for i in range(3):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("¡Oops! Esa palabra aún no está registrada.")
