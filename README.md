# Gramáticas en lo general
Las gramáticas definen la sintaxis de distintos tipos de lenguajes. Hacen esto a través de sus producciones y a distintos niveles de complejidad en su estructura.

Una gramática `G` define a un lenguaje `L`, que opera sobre un alfabeto `Σ`. Esta es una tupla `G = (V,Σ,R,S)` donde:

- `V`: conjunto finito de símbolos no terminales.
- `Σ`: conjunto finito de símbolos terminales (`Σ ∩ V = ∅`, representan el alfabeto de un lenguaje)
- `S ∈ V`: símbolo inicial.
- `R`: conjunto finito de reglas o producciones de la forma `α → β`, con "`α, β ∈ (V ∪ Σ)*`".

## Producciones
Las producciones adquieren la forma **ψ → ω**, que representa el reemplazo de una subcadena (denotada del lado izquierdo de la expresión), por otra cadena (denotada del lado derecho), todo esto dentro de una cadena mayor. 

## Proceso de derivación
Entonces puede decirse que `L` es un lenguaje generado por `G`, toda vez que las producciones de `G` le determinan al lenguaje toda cadena posible de obtener.

Esa relación se ve plasmada por la derivación: `G: L(G) = { w ∈ Σ* | S ⇒* w }`, donde `⇒*` es el proceso de derivación en cero o más pasos.

La idea es que toda cadena conformada por al menos un símbolo no terminal puede someterse a **derivación**, misma que parte de `S` (*`ψ`*) y consiste en **reemplazar de manera secuencial y recursiva, cada símbolo no terminal por otra cadena `ω`, según los criterios de las producciones** (una ocurrencia de un no terminal en cada paso).

Se puede representar a este proceso como un árbol (parse tree), donde las hojas representan símbolos terminales y los nodos internos, no-terminales.

Puede decirse que `w ∈ L`, siempre que esté compuesta exclusivamente por símbolos terminales y sea derivable desde `S`.

## Jerarquía de Chomsky y distintos tipos de restricciones en las producciones de gramáticas
<sub>Se asemeja a un núcleo: las capas posteriores al 0, son más "superficiales" en su complejidad y capacidad.</sub>

0. Gramáticas Recursivamente Enumerables: reglas sin restricciones formales; es más conceptual (Máquina de Turing con memoria infinita). 
1. Gramáticas Sensibles al Contexto: reglas `αAβ → αγβ` con `γ ≠ ε`
2. Gramáticas Libres de Contexto: reglas `A → γ` con `A ∈ V, γ ∈ (V ∪ Σ)*`
3. Gramáticas Regulares: reglas de la forma `A → aB` o `A → a` (derechas o izquierdas), con `a ∈ Σ, B ∈ V`
