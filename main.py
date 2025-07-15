import  random 
nombres = ["Joan Garcia","Balde", "Cubarsi", "Iñigo", "Pedri", "De Jong", "Dani Olmo", "Lewandowski", "Raphinha", "Yamal", "Ferran", "Kounde", "Ter Stegen", "Araujo", "Ansu fati"];
razas = ["humano", "enano", "elfo", "semi dios", "muerto", "esqueleto", "cecaelia", "alienigena", "reptiliano", "lobizon", "vampiro", "viltrumita", "saijayin", "centauro", "hombre tiburon"];
clases = ["guerrero", "mago", "arquero", "lanzador", "ballestero", "pistolero", "super humano", "francotirador", "bombardero", "kamikase", "samurai", "asesino", "ninja", "boxeador", "tanque"];
num=random.randint(0,14);
vida = random.randint(50,100);
ataque = random.randint(10,50);
defensa = random.randint(5,30);
print("Su personaje es: ",nombres[num],  "\nraza:", razas[num], "\nclase: ", clases[num])
print("Sus estadisticas son: ")
print("vida: ",vida)
print("ataque: ",ataque)
print("defensa: ",defensa) 