# Función para inicializar el tablero estándar
def inicializar_tablero():
    tablero = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],  # fila 1: negras
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],  # fila 2: peones negros
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # fila 3: vacío
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # fila 4: vacío
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # fila 5: vacío
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # fila 6: vacío
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  # fila 7: peones blancos
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']   # fila 8: blancas
    ]
    return tablero

# Función para inicializar un tablero vacío
def inicializar_tablero_vacio():
    return [[' ' for _ in range(8)] for _ in range(8)]

# Función para mostrar el tablero con letras y números
def mostrar_tablero(tablero):
    letras_columnas = '  a  b  c  d  e  f  g  h'
    print(letras_columnas)
    for i, fila in enumerate(tablero):
        print(f"{8-i} {' '.join(fila)} {8-i}")
    print(letras_columnas)

# Función para convertir coordenadas de tipo 'e2' a índices de la matriz
def convertir_coordenadas(coordenada):
    letras = 'abcdefgh'
    columna = letras.index(coordenada[0])
    fila = 8 - int(coordenada[1])
    return fila, columna

# Función para validar si un movimiento de peón es válido
def validar_movimiento_peon(tablero, fila_origen, col_origen, fila_destino, col_destino):
    pieza = tablero[fila_origen][col_origen]
    
    # Movimiento de peón blanco
    if pieza == 'P':
        if fila_origen == 6 and fila_destino == 4 and col_origen == col_destino and tablero[5][col_origen] == ' ' and tablero[4][col_origen] == ' ':
            return True  # Primer movimiento: dos espacios adelante
        if fila_destino == fila_origen - 1 and col_origen == col_destino and tablero[fila_destino][col_destino] == ' ':
            return True  # Avanza una casilla hacia adelante
        if fila_destino == fila_origen - 1 and abs(col_origen - col_destino) == 1 and tablero[fila_destino][col_destino].islower():
            return True  # Captura pieza negra en diagonal
    
    # Movimiento de peón negro
    elif pieza == 'p':
        if fila_origen == 1 and fila_destino == 3 and col_origen == col_destino and tablero[2][col_origen] == ' ' and tablero[3][col_origen] == ' ':
            return True  # Primer movimiento: dos espacios adelante
        if fila_destino == fila_origen + 1 and col_origen == col_destino and tablero[fila_destino][col_destino] == ' ':
            return True  # Avanza una casilla hacia adelante
        if fila_destino == fila_origen + 1 and abs(col_origen - col_destino) == 1 and tablero[fila_destino][col_destino].isupper():
            return True  # Captura pieza blanca en diagonal
    
    return False  # Movimiento no válido

# Función para validar si un movimiento de caballo es válido
def validar_movimiento_caballo(tablero, fila_origen, col_origen, fila_destino, col_destino):
    pieza = tablero[fila_origen][col_origen]
    fila_diff = abs(fila_destino - fila_origen)
    col_diff = abs(col_destino - col_origen)
    
    # El caballo se mueve en "L" (dos casillas en una dirección y una en la otra)
    if (fila_diff == 2 and col_diff == 1) or (fila_diff == 1 and col_diff == 2):
        if pieza.isupper():  # Si es un caballo blanco
            return tablero[fila_destino][col_destino] == ' ' or tablero[fila_destino][col_destino].islower()
        elif pieza.islower():  # Si es un caballo negro
            return tablero[fila_destino][col_destino] == ' ' or tablero[fila_destino][col_destino].isupper()

    return False  # Movimiento no válido

# Función para validar si un movimiento de alfil es válido
def validar_movimiento_alfil(tablero, fila_origen, col_origen, fila_destino, col_destino):
    pieza = tablero[fila_origen][col_origen]
    if abs(fila_destino - fila_origen) != abs(col_destino - col_origen):
        return False  # No se mueve en diagonal
    
    paso_fila = 1 if fila_destino > fila_origen else -1
    paso_columna = 1 if col_destino > col_origen else -1
    fila_actual = fila_origen + paso_fila
    columna_actual = col_origen + paso_columna
    
    while fila_actual != fila_destino and columna_actual != col_destino:
        if tablero[fila_actual][columna_actual] != ' ':
            return False
        fila_actual += paso_fila
        columna_actual += paso_columna
    
    if pieza.isupper():
        return tablero[fila_destino][col_destino] == ' ' or tablero[fila_destino][col_destino].islower()
    else:
        return tablero[fila_destino][col_destino] == ' ' or tablero[fila_destino][col_destino].isupper()

# Función para validar si un movimiento de torre es válido
def validar_movimiento_torre(tablero, fila_origen, col_origen, fila_destino, col_destino):
    pieza = tablero[fila_origen][col_origen]
    if fila_origen != fila_destino and col_origen != col_destino:
        return False
    
    if fila_origen == fila_destino:  # Movimiento horizontal
        paso_columna = 1 if col_destino > col_origen else -1
        columna_actual = col_origen + paso_columna
        while columna_actual != col_destino:
            if tablero[fila_origen][columna_actual] != ' ':
                return False
            columna_actual += paso_columna
    else:  # Movimiento vertical
        paso_fila = 1 if fila_destino > fila_origen else -1
        fila_actual = fila_origen + paso_fila
        while fila_actual != fila_destino:
            if tablero[fila_actual][col_origen] != ' ':
                return False
            fila_actual += paso_fila
    
    if pieza.isupper():
        return tablero[fila_destino][col_destino] == ' ' or tablero[fila_destino][col_destino].islower()
    else:
        return tablero[fila_destino][col_destino] == ' ' or tablero[fila_destino][col_destino].isupper()

# Función para validar si un movimiento de reina es válido
def validar_movimiento_reina(tablero, fila_origen, col_origen, fila_destino, col_destino):
    return validar_movimiento_torre(tablero, fila_origen, col_origen, fila_destino, col_destino) or \
           validar_movimiento_alfil(tablero, fila_origen, col_origen, fila_destino, col_destino)

# Función para realizar el enroque
def realizar_enroque(tablero, origen, destino):
    fila_origen, col_origen = convertir_coordenadas(origen)
    fila_destino, col_destino = convertir_coordenadas(destino)

    if col_origen == 4 and col_destino == 6:  # Enroque corto
        if tablero[fila_origen][col_origen] == 'K':
            tablero[fila_origen][6] = 'K'
            tablero[fila_origen][5] = 'R'
            tablero[fila_origen][4] = ' '
            tablero[fila_origen][7] = ' '
        elif tablero[fila_origen][col_origen] == 'k':
            tablero[fila_origen][6] = 'k'
            tablero[fila_origen][5] = 'r'
            tablero[fila_origen][4] = ' '
            tablero[fila_origen][7] = ' '
        return True

    if col_origen == 4 and col_destino == 2:  # Enroque largo
        if tablero[fila_origen][col_origen] == 'K':
            tablero[fila_origen][2] = 'K'
            tablero[fila_origen][3] = 'R'
            tablero[fila_origen][4] = ' '
            tablero[fila_origen][0] = ' '
        elif tablero[fila_origen][col_origen] == 'k':
            tablero[fila_origen][2] = 'k'
            tablero[fila_origen][3] = 'r'
            tablero[fila_origen][4] = ' '
            tablero[fila_origen][0] = ' '
        return True

    return False

# Función para validar si un movimiento de rey es válido
def validar_movimiento_rey(tablero, fila_origen, col_origen, fila_destino, col_destino):
    if max(abs(fila_destino - fila_origen), abs(col_destino - col_origen)) == 1:
        pieza = tablero[fila_origen][col_origen]
        if pieza.isupper():
            return tablero[fila_destino][col_destino] == ' ' or tablero[fila_destino][col_destino].islower()
        else:
            return tablero[fila_destino][col_destino] == ' ' or tablero[fila_destino][col_destino].isupper()

    if col_origen == 4 and (col_destino == 6 or col_destino == 2):  # Enroque corto o largo
        return True

    return False

# Función para mover una pieza en el tablero
def mover_pieza(tablero, origen, destino):
    fila_origen, col_origen = convertir_coordenadas(origen)
    fila_destino, col_destino = convertir_coordenadas(destino)
    
    if tablero[fila_origen][col_origen] == ' ':
        print(f"No hay ninguna pieza en {origen} para mover.")
        return
    
    pieza = tablero[fila_origen][col_origen].lower()

    if pieza == 'k':
        if realizar_enroque(tablero, origen, destino):
            mostrar_tablero(tablero)
            return
        if not validar_movimiento_rey(tablero, fila_origen, col_origen, fila_destino, col_destino):
            print(f"Movimiento de rey desde {origen} hasta {destino} no es válido.")
            return
    
    if pieza == 'p':
        if not validar_movimiento_peon(tablero, fila_origen, col_origen, fila_destino, col_destino):
            print(f"Movimiento de peón desde {origen} hasta {destino} no es válido.")
            return
    elif pieza == 'n':
        if not validar_movimiento_caballo(tablero, fila_origen, col_origen, fila_destino, col_destino):
            print(f"Movimiento de caballo desde {origen} hasta {destino} no es válido.")
            return
    elif pieza == 'b':
        if not validar_movimiento_alfil(tablero, fila_origen, col_origen, fila_destino, col_destino):
            print(f"Movimiento de alfil desde {origen} hasta {destino} no es válido.")
            return
    elif pieza == 'r':
        if not validar_movimiento_torre(tablero, fila_origen, col_origen, fila_destino, col_destino):
            print(f"Movimiento de torre desde {origen} hasta {destino} no es válido.")
            return
    elif pieza == 'q':
        if not validar_movimiento_reina(tablero, fila_origen, col_origen, fila_destino, col_destino):
            print(f"Movimiento de reina desde {origen} hasta {destino} no es válido.")
            return

    tablero[fila_destino][col_destino] = tablero[fila_origen][col_origen]
    tablero[fila_origen][col_origen] = ' '

    mostrar_tablero(tablero)

# Función para manejar el ciclo de movimientos
def ciclo_de_movimientos(tablero):
    while True:
        print("\nIntroduce el movimiento o escribe 'salir' para terminar.")
        origen = input("Desde (ej: e2): ").lower()
        if origen == 'salir':
            break
        destino = input("Hasta (ej: e4): ").lower()
        if destino == 'salir':
            break
        
        mover_pieza(tablero, origen, destino)

# Función para que el usuario coloque manualmente las piezas
def colocar_piezas_manual(tablero):
    while True:
        mostrar_tablero(tablero)
        print("Introduce una pieza y su posición (ej: Pe4) o escribe 'fin' para terminar:")
        entrada = input("Pieza y casilla: ")  # Mantener el input tal como lo ingresa el usuario
        if entrada.lower() == 'fin':
            break
        if len(entrada) < 3 or entrada[1] not in 'abcdefgh':
            print("Entrada inválida. Intenta de nuevo.")
            continue
        pieza = entrada[0]  # La primera letra es la pieza
        coordenada = entrada[1:]  # Las siguientes son las coordenadas
        fila, columna = convertir_coordenadas(coordenada)
        
        # Validar y colocar la pieza según sea blanca (mayúsculas) o negra (minúsculas)
        if pieza in ['P', 'N', 'B', 'R', 'Q', 'K']:  # Piezas blancas (mayúsculas)
            tablero[fila][columna] = pieza
        elif pieza in ['p', 'n', 'b', 'r', 'q', 'k']:  # Piezas negras (minúsculas)
            tablero[fila][columna] = pieza
        else:
            print("Pieza inválida. Usa P,N,B,R,Q,K para blancas y p,n,b,r,q,k para negras.")

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Empezar con tablero estándar")
    print("2. Colocar las piezas manualmente")
    print("3. Salir")
    opcion = input("Elige una opción: ")
    return opcion

# Función principal para ejecutar el menú
def menu_principal():
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            tablero = inicializar_tablero()
            mostrar_tablero(tablero)
            ciclo_de_movimientos(tablero)
        elif opcion == '2':
            tablero = inicializar_tablero_vacio()
            colocar_piezas_manual(tablero)
            ciclo_de_movimientos(tablero)
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el programa
menu_principal()



