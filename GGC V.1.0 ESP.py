import math

def mostrar_firma():
    print("Genshin Gacha Calculator V.1.0")
    print("Desarrollado por Patontoo.")
    print("Este script calcula la probabilidad de obtener un objeto de 5 estrellas de un banner en Genshin Impact.")
    print("Puedes elegir entre un cálculo general basado en las tasas oficiales publicadas o un cálculo personalizado basado en tus propios datos.")
    print("Esta calculadora usa los conceptos conocidos de 'soft pity' y 'hard pity', donde los banners de personajes tienen aproximadamente un aumento del 6% en la probabilidad de obtener un item 5 estrellas por cada deseo desde el 74 al 89, y los banners de armas tienen conceptos similares entre los deseos 63 y 79 (algunas fuentes sugieren que el hard pity es en el 77, pero usamos 80 por precisión).")
    print('Créditos a "Slime Machine" en Hoyolab por la fórmula de distribución binomial compartida en los foros y usada en esta calculadora.')
    print()

# Función para calcular la probabilidad binomial
def probabilidad_binomial(n, x, P):
    nCx = math.comb(n, x)  # Coeficiente binomial
    return nCx * (P**x) * ((1 - P)**(n - x))

# Función para calcular la probabilidad de obtener al menos un objeto de 5 estrellas
def ajustar_probabilidad(pity_actual, deseos_futuros, probabilidad_base, tipo_banner):
    # Definir umbrales de pity según el tipo de banner
    if tipo_banner == "personaje":
        soft_pity = 74
        hard_pity = 90
        incremento_por_deseo = 0.06  # 6% de incremento por deseo
    elif tipo_banner == "arma":
        soft_pity = 63
        hard_pity = 80
        incremento_por_deseo = 0.06  # Ejemplo: 6% de incremento por deseo
    else:
        raise ValueError("Tipo de banner inválido")

    # Verificar si los deseos futuros llegarán a hard pity
    if pity_actual + deseos_futuros >= hard_pity:
        return 1.0  # 100% de probabilidad de obtener al menos un objeto de 5 estrellas
    
    # Determinar la probabilidad en el pity actual
    if pity_actual < soft_pity:
        probabilidad_en_pity = probabilidad_base
    elif soft_pity <= pity_actual < hard_pity:
        probabilidad_en_pity = min(probabilidad_base + incremento_por_deseo * (pity_actual - soft_pity), 1.0)
    else:
        probabilidad_en_pity = 1.0

    # Limitar la probabilidad al 100% si se alcanza el hard pity
    if pity_actual + deseos_futuros >= hard_pity:
        probabilidad_en_pity = 1.0

    # Calcular la probabilidad de no obtener un objeto de 5 estrellas en los deseos futuros
    probabilidad_no_obtener_5_estrellas = probabilidad_binomial(deseos_futuros, 0, probabilidad_en_pity)
    
    # La probabilidad total es 1 menos la probabilidad de no obtener ningún objeto de 5 estrellas
    return 1 - probabilidad_no_obtener_5_estrellas

# Función principal para calcular la probabilidad con entradas
def calcular_probabilidad():
    mostrar_firma()  # Mostrar firma
    
    # Elegir tipo de cálculo
    tipo_calculo = input("Elige el tipo de cálculo: (1) General basado en tasas publicadas o (2) Personalizado basado en tus datos: ")
    
    if tipo_calculo == "1":
        # Cálculo general
        tipo_banner = input("Introduce el tipo de banner: (1) Personaje o (2) Arma: ")
        if tipo_banner == "1":
            probabilidad_base = 0.006  # Probabilidad base del 0.6% para personajes
            tipo_banner = "personaje"
        elif tipo_banner == "2":
            probabilidad_base = 0.006  # Ajustar según sea necesario para armas
            tipo_banner = "arma"
        else:
            print("Elección inválida. Saliendo.")
            return
        print("Usando tasas generales basadas en los datos publicados del sistema gacha.")
    elif tipo_calculo == "2":
        # Cálculo personalizado
        cinco_estrellas = int(input("¿Cuántos objetos de 5 estrellas has obtenido en deseos recientes? "))
        deseos_totales = int(input("¿Cuántos deseos has realizado en total? "))
        probabilidad_base = cinco_estrellas / deseos_totales  # Probabilidad ajustada según los deseos anteriores
        tipo_banner = input("Introduce el tipo de banner: (1) Personaje o (2) Arma: ")
        if tipo_banner == "1":
            tipo_banner = "personaje"
        elif tipo_banner == "2":
            tipo_banner = "arma"
        else:
            print("Elección inválida. Saliendo.")
            return
    else:
        print("Elección inválida. Saliendo.")
        return

    # Introducir el pity actual y el número de deseos futuros
    pity_actual = int(input("Introduce tu pity actual: "))
    deseos_futuros = int(input("Introduce el número de deseos futuros: "))
    
    # Ajustar la probabilidad según el pity actual, los deseos futuros y el tipo de banner
    probabilidad_ajustada = ajustar_probabilidad(pity_actual, deseos_futuros, probabilidad_base, tipo_banner)
    
    # Mostrar el resultado
    print(f"La probabilidad de obtener al menos un objeto de 5 estrellas en {deseos_futuros} deseos es aproximadamente del {probabilidad_ajustada * 100:.2f}%")

    # Pausa para ver el resultado
    input("Presiona Enter para salir...")

# Ejecutar la función principal
calcular_probabilidad()
