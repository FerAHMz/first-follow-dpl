"""
Computar FIRST y FOLLOW de una gramática libre de contexto.

INPUT (por stdin):
  1. Línea con terminales separados por espacios
  2. Línea con no-terminales separados por espacios
  3. Símbolo inicial
  4. Líneas de producciones en formato:  A -> α | β
     Usar 'epsilon' para la cadena vacía (ε)

EJEMPLO de input:
  a b c d
  S A B C
  S
  S -> A B
  A -> a | epsilon
  B -> b C
  C -> c | d

OUTPUT:
  Conjuntos FIRST y FOLLOW de cada no-terminal.
"""

import sys


def parse_input():
    lines = [l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
    idx = 0

    terminals = lines[idx].split()
    idx += 1

    non_terminals = lines[idx].split()
    idx += 1

    start = lines[idx]
    idx += 1

    # Parsear producciones
    productions = {}  # dict: NT -> list of list of symbols
    for line in lines[idx:]:
        head, body = line.split("->")
        head = head.strip()
        alternatives = body.split("|")
        for alt in alternatives:
            symbols = alt.split()
            if not symbols:
                symbols = ["epsilon"]
            productions.setdefault(head, []).append(symbols)

    return terminals, non_terminals, start, productions


def compute_first(terminals, non_terminals, productions):
    first = {nt: set() for nt in non_terminals}
    # Terminales y epsilon tienen FIRST = {ellos mismos}
    for t in terminals:
        first[t] = {t}
    first["epsilon"] = {"epsilon"}

    changed = True
    while changed:
        changed = False
        for nt in non_terminals:
            for prod in productions.get(nt, []):
                # Calcular FIRST de esta producción
                for symbol in prod:
                    sym_first = first.get(symbol, {symbol})
                    before = len(first[nt])
                    first[nt] |= sym_first - {"epsilon"}
                    if len(first[nt]) != before:
                        changed = True
                    if "epsilon" not in sym_first:
                        break
                else:
                    # Todos los símbolos pueden derivar epsilon
                    before = len(first[nt])
                    first[nt].add("epsilon")
                    if len(first[nt]) != before:
                        changed = True

    return first


def compute_follow(non_terminals, start, productions, first):
    follow = {nt: set() for nt in non_terminals}
    follow[start].add("$")

    changed = True
    while changed:
        changed = False
        for nt in non_terminals:
            for prod in productions.get(nt, []):
                for i, symbol in enumerate(prod):
                    if symbol not in non_terminals:
                        continue
                    # FOLLOW del símbolo actual
                    rest = prod[i + 1:]
                    # Calcular FIRST del resto
                    first_rest = set()
                    if not rest:
                        all_epsilon = True
                    else:
                        all_epsilon = True
                        for s in rest:
                            s_first = first.get(s, {s})
                            first_rest |= s_first - {"epsilon"}
                            if "epsilon" not in s_first:
                                all_epsilon = False
                                break

                    before = len(follow[symbol])
                    follow[symbol] |= first_rest
                    if all_epsilon:
                        follow[symbol] |= follow[nt]
                    if len(follow[symbol]) != before:
                        changed = True

    return follow


def main():
    terminals, non_terminals, start, productions = parse_input()

    first = compute_first(terminals, non_terminals, productions)
    follow = compute_follow(non_terminals, start, productions, first)

    print("=" * 40)
    print("FIRST sets:")
    print("=" * 40)
    for nt in non_terminals:
        print(f"  FIRST({nt}) = {{ {', '.join(sorted(first[nt]))} }}")

    print()
    print("=" * 40)
    print("FOLLOW sets:")
    print("=" * 40)
    for nt in non_terminals:
        print(f"  FOLLOW({nt}) = {{ {', '.join(sorted(follow[nt]))} }}")


if __name__ == "__main__":
    main()
