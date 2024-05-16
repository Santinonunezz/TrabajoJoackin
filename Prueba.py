import random
#PERSONAJE
nombre = ""
vida = 100
ataque = 5
secuenciaAtaque = 99999
curacion = 20
mana = 100
costeCuracion = 20
estadisticas = vida, mana
evasion = 5
escudo = 0

#ENEMIGO 1
nombreEnemigo1 = "Goblin"
vidaEnemigo1 = 100
ataqueEnemigo1 = 15
curacionEnemigo1 = 10

nombre = input("¿Como te llamas jugador?:")
print("Encantado de conocerte " + nombre)
print("Demostrame tu potencial en combate, pelea y venceras.")
print("-------------------------------------")

#COMBATE
print("Te topaste con un " + nombreEnemigo1)
print("-------------------------------------")



while vida >0 and vidaEnemigo1 >0:
    respuesta = ""
    print("Tus estadisticas: ")
    print("Vida: " + str(vida))
    print("Mana: " + str(mana))
    if escudo > 0:
        print("Escudo: " + str(escudo))
    print("-------------------------------------")
    respuesta = input("¿Como deseas responder? a-Atacar (" + str(ataque) + ") / c-Curar: (" + str(costeCuracion) + "): ")
    print("-------------------------------------")

    if evasion == 5:
            numerosEvasion = list(range(1, 100))
            numero_elegido = random.choice(numerosEvasion)
            if numero_elegido <= 25:
                ataque = 0
                print("Te tropesaste y desviaste la espada!")
    if respuesta == "a":
        print("Has decidido atacar ")
        vidaEnemigo1 -= ataque
        print("Has hecho: " + str(ataque) + " de daño")
        print("El enemigo ahora tiene: " + str(vidaEnemigo1) + " puntos de vida")
        print("-------------------------------------")


    if respuesta == "c" and mana >= costeCuracion and vida < 100:
        print("Has decidido curarte")
        mana -= costeCuracion
        vida += curacion
        print("Te has curado: " + str(curacion) + " puntos de vida")
        print("-------------------------------------")

        respuesta = input("¿Como deseas responder? a-Atacar (" + str(ataque) + ") / c-Curar: (" + str(costeCuracion) + "): ")
        if respuesta == "a":
            print("Has decidido atacar ")
            vidaEnemigo1 -= ataque
            print("Has hecho: " + str(ataque) + " de daño")
            print("El enemigo ahora tiene: " + str(vidaEnemigo1) + " puntos de vida")
            print("-------------------------------------")

    elif respuesta == "c" and mana >= costeCuracion and vida == 100:
        print("¡No puedes curarte mas que tu cantidad de vida maxima!")
        respuesta = input("¿Quieres crear un escudo con tu curacion? a-Si / x-No")
        if respuesta == "a" and mana >= costeCuracion and vida == 100:
            print("Te has curado, la curacion se añadio como escudo ")
            mana -= costeCuracion
            escudo += curacion
            print("-------------------------------------")
        elif respuesta == "x":
            print("Te mantienes neutral")
    #TURNO ENEMIGO 1
    print("El " + nombreEnemigo1 + " se abalanza con su espada y te inflige " + str(ataqueEnemigo1) + " de daño")
    vida -= ataqueEnemigo1
    print("Vida: " + str(vida))
    print("-------------------------------------")

    if vidaEnemigo1 <=50:
        numeros = list(range(1, 6))
        numero_elegido = random.choice(numeros)
        if numero_elegido % 2 == 0:
            vidaEnemigo1 + curacionEnemigo1
            print("El enemigo se ha curado " + str(curacionEnemigo1) + " puntos de vida")
            print("El enemigo tiene " + str(vidaEnemigo1) + " puntos de vida")
    

    if vida <25:
        print("Supongo que voy a tener que darte una mano....")
        print("- " + str(secuenciaAtaque))
        vidaEnemigo1 -= secuenciaAtaque
        print("El " + nombreEnemigo1 + " se desintegra y se hace uno con el viento.")

        print("Si no eres capaz de matar a un simple Goblin, no eres merecedor de mi poder.")
        print("Vuelvete mas poderoso y buscame....")

print("Caes inconsciente en el suelo, ahora depende de ti sobrevivir")



