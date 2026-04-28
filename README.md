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



# Description
Se generará, en torno al lenguaje indonesio, una gramática sujeta a contexto, misma que será limpiada y liberada de toda recursión izquierda. 

El indonesio es uno de los lenguajes que sigue la estructura SVO (Subject-Verb-Object), que maneja un orden específico de las palabras para comunicar una acción realizada por un sujeto, sobre un objeto.

Además, es un lenguaje aglutinante, lo que quiere decir que las palabras pueden formar nuevas palabras cuando se les añade afijos que tienen un valor gramatical concreto y así cambiar el significado de palabras a través de la concatenación y reduplicación. 

Este es el tipo de estructura que la gramática a desarrollar, debe analizar y verificar en toda oración que se le presente.

# Estructura y Léxico 
Seguirá la siguiente estructura y símbolos. En cuanto a los símbolos terminales, por el momento, no se especifican las palabras que comprendederán cada categoría porque hacerlo comprometería al lenguaje. Incluso, cabe resaltar que hasta ahora SVO no se ve denotado estrictamente porque falta restringir y quitar ambigüedad.

Orden base SVO: `Sujeto -> Verbo -> Objeto`
Modificadores:
- Los adjetivos suelen ir después del sustantivo
- Los adverbios tienden a ir después del verbo
Por ser lenguaje aglutinante, hay presencia de afijos (prefijos/sufijos)

Los símbolos que la constituyen:
  No terminales que representan sintagmas y cláusulas:
    -`S`: Símbolo inicial
    -`AdvP`: Sintagma Adverbial
    -`NP`: Sintagma nominal
    -`VP`: Sintagma verbal
    -`PP`: Sintagma preposicional
    -`AdjP`: Sintagma adjetival
    -`RelClause`: Cláusula relativa
  Terminales que representan conjuntos de palabras de distinto tipo:
    -`N`: sustantivos
    -`Pron`: pronombres
    -`Det`: determinantes:
    -`V`: verbos
    -`Adv`: adverbios
    -`Adj`: adjetivos
    -`Prep`: preposiciones
    -`RelMarker`: yang (cuál) 

`S -> S AdvP | NP VP | S PP` - Para las producciones de alto nivel, se introduce ambigüedad en la adjunción de adverbios y frases preposicionales.
`NP -> NP AdjP | NP PP | NP RelClause | N | Pron | Det NP` - Sintagma nominal con recursión izquierda, para encadenamiento de modificadores postnominales y ambigüedad en agrupación.
`VP -> VP AdvP | VP PP | V | V NP | V NP NP | V S` - Sintagma verbal con recursión izquierda, para ambigüedad en adjuntos (AdvP, PP) y estructura verbal.
`PP -> Prep NP` - Sintagma preposicional, para adjunción ambigua (puede modificar NP o VP).
`AdjP -> AdjP Adv | Adj` - Sintagma adjetival, puede escalar recursivamente.
`AdvP -> AdvP Adv | Adv` - Sintagma adverbial, ambigüedad por agrupación.
`RelClause -> RelMarker S | RelMarker VP` - Cláusula relativa, uso del marcador típico “yang”.
