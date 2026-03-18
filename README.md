# Computando FIRST y FOLLOW

## Video de presentacion

[https://youtu.be/CSGtnBt8mwY](https://youtu.be/CSGtnBt8mwY)

## Descripcion

Se desarrollo un programa en Python que computa los conjuntos FIRST y FOLLOW de una gramatica libre de contexto. El programa recibe como entrada un archivo de texto con los terminales, no-terminales, simbolo inicial y las producciones de la gramatica, y devuelve los conjuntos FIRST y FOLLOW de cada no-terminal.

## Arquitectura y funcionamiento

El programa esta contenido en un unico archivo `first_follow.py` y se divide en cuatro funciones principales:

### 1. `parse_input()` — Lectura de la gramatica

Lee la gramatica desde stdin. Espera el siguiente formato:

1. Terminales separados por espacio
2. No-terminales separados por espacio
3. Simbolo inicial
4. Producciones en formato `A -> α | β` (se usa `epsilon` para la cadena vacia)

Retorna las listas de terminales, no-terminales, el simbolo inicial y un diccionario de producciones donde cada no-terminal mapea a una lista de alternativas (cada alternativa es una lista de simbolos).

### 2. `compute_first(terminals, non_terminals, productions)` — Calculo de FIRST

Implementa el algoritmo de punto fijo para calcular los conjuntos FIRST:

- Inicializa FIRST de cada terminal como el conjunto que solo lo contiene a si mismo.
- Itera sobre todas las producciones de cada no-terminal repetidamente hasta que no haya cambios:
  - Para una produccion `A -> X1 X2 ... Xn`, agrega a FIRST(A) los elementos de FIRST(X1) sin epsilon.
  - Si FIRST(X1) contiene epsilon, continua con X2, y asi sucesivamente.
  - Si todos los simbolos de la produccion pueden derivar epsilon, agrega epsilon a FIRST(A).

### 3. `compute_follow(non_terminals, start, productions, first)` — Calculo de FOLLOW

Implementa el algoritmo de punto fijo para calcular los conjuntos FOLLOW:

- Agrega `$` a FOLLOW del simbolo inicial.
- Itera repetidamente hasta que no haya cambios:
  - Para cada produccion `A -> α B β`:
    - Agrega FIRST(β) sin epsilon a FOLLOW(B).
    - Si β puede derivar epsilon (o no existe), agrega FOLLOW(A) a FOLLOW(B).

### 4. `main()` — Orquestacion y salida

Llama a las funciones anteriores en orden e imprime los resultados formateados.

### Flujo general

```
Archivo de texto (stdin)
        |
        v
  parse_input()  -->  terminales, no-terminales, inicio, producciones
        |
        v
  compute_first()  -->  conjuntos FIRST
        |
        v
  compute_follow()  -->  conjuntos FOLLOW
        |
        v
  Impresion de resultados
```

## Formato de entrada

El programa espera un archivo de texto con el siguiente formato:

```
a b c d
S A B C
S
S -> A B
A -> a | epsilon
B -> b C
C -> c | d
```

## Como ejecutar

Se requiere tener Python 3 instalado. Se ejecuta el programa pasando el archivo de entrada mediante redireccion de stdin:

```bash
python3 first_follow.py < ejemplo.txt
```

Se incluyeron dos archivos de prueba:

- `ejemplo.txt` — gramatica simple
- `ejemplo2.txt` — gramatica de expresiones aritmeticas (E, T, F con operadores + y *)

## Ejemplo de salida

Para `ejemplo.txt`:

```
========================================
FIRST sets:
========================================
  FIRST(S) = { a, b }
  FIRST(A) = { a, epsilon }
  FIRST(B) = { b }
  FIRST(C) = { c, d }

========================================
FOLLOW sets:
========================================
  FOLLOW(S) = { $ }
  FOLLOW(A) = { b }
  FOLLOW(B) = { $ }
  FOLLOW(C) = { $ }
```

## Autores

- Fernando Hernandez — 23645
- Fernando Rueda — 23748
- Jorge Aguilar — 23195
