# Computando FIRST y FOLLOW

## Descripcion

Se desarrollo un programa en Python que computa los conjuntos FIRST y FOLLOW de una gramatica libre de contexto. El programa recibe como entrada los terminales, no-terminales, simbolo inicial y las producciones de la gramatica, y devuelve los conjuntos FIRST y FOLLOW de cada no-terminal.

## Formato de entrada

El programa espera un archivo de texto con el siguiente formato:

1. Terminales separados por espacio
2. No-terminales separados por espacio
3. Simbolo inicial
4. Producciones en formato `A -> α | β` (se usa `epsilon` para representar la cadena vacia)

### Ejemplo de entrada

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
