# Gramáticas en lo general
Definen la sintaxis de distintos tipos de lenguajes (tienen variadas aplicaciones) a través de producciones que representan el reemplazo de una subcadena, por otra cadena, y esto se da a distintos niveles de complejidad.

Una gramática $G$ define a un lenguaje $L$, que opera sobre un alfabeto $Σ$. Esta es una tupla $G = (V,Σ,R,S)$ donde:

- $V$: conjunto finito de símbolos no terminales.
- $Σ$: conjunto finito de símbolos terminales.
- $S ∈ V$: símbolo inicial.
- $R$: conjunto finito de reglas o producciones.

$L$ es un lenguaje generado por $G$, toda vez que las producciones de $G$ le determinan al lenguaje toda cadena posible de derivar.

La idea es que toda cadena con un símbolo no terminal puede someterse a derivación, proceso que parte de $S$ y consiste en reemplazar cada no terminal (bajo un orden, conforme a la estrategia de análisis) por otra cadena siguiendo los criterios de $R$.

Se puede representar a este proceso como un árbol de análisis, donde las hojas representan símbolos terminales y los nodos internos, no-terminales.

Puede decirse que una cadena es elemento de $L$, siempre que esté compuesta exclusivamente por símbolos terminales y sea derivable desde $S$.

## Jerarquía de Chomsky y distintos tipos de restricciones en las producciones de gramáticas

<sub>Se asemeja a un núcleo: las capas posteriores al 0, son más "superficiales" en su complejidad y capacidad.</sub>

Tipo 0. Gramáticas Recursivamente Enumerables

Tipo 1. Gramáticas Sensibles al Contexto

Tipo 2. Gramáticas Libres de Contexto: reglas con la forma $A \to B$ con $A$ elemento de $V$, y $B$ elemento de todas las cadenas formadas por  $V$ y $Σ$

Tipo 3. Gramáticas Regulares

# Planteamiento
Se generó una gramática libre de contexto en torno al **lenguaje indonesio**. En primera instancia, fue planteada con recursión izquierda y ambigua para su posterior tratamiento y limpieza de recursión izquierda y ambigüedad.

# Características del lenguaje
- Estructura sintáctica SVO, para comunicar acción realizada por un sujeto sobre de un objeto.
- Carente de conjugaciones.
- Sin distinción hombre/mujer ni de pluralidad para adjetivos, pronombres y sustantivos.
- Aglutinación en torno a verbos raíz forma nuevas palabras, a través de afijos.
- Afijos activos y pasivos cambian el orden de la oración.
- Aspectos como la temporalidad se ven descritos a través de partículas.
- Objetos y sustantivos representan entidades nominales.

Dichas características fueron consideradas durante la elaboración de la gramática, para definir su alcance, descrito a continuación.

## Alcance
    Las oraciones aceptadas por la gramática representan un subconjunto del lenguaje indonesio, comprendido por oraciones simples, apegadas a la estructura SVO en su conjugación activa, libres de cualquier afijo que altere el orden sintáctico mencionado.

Cadenas que deberían aceptarse:

| Indonesio | Español |
|-|-|
| Dia memasak makanan| Él/Ella cocina comida |
| Chef membakar rumah| El chef incendia una casa|
| Seorang wanita membeli sebuah mobil| Una mujer compra un automóvil|
| Anjing mengejar kucing| El perro persigue al gato|
| Seekor domba makan rumput| Un cordero come hierba|
| Dia akan membeli sebuah rumah| Él/Ella comprará una casa|
| Dia sudah memasak makanan| Él/Ella ya cocinó comida|
| Seorang anak berbagi pizza| Un niño/una niña comparte pizza|
| Siswa membeli workstation| Un estudiante compra una workstation|
| Chef gagal ujian| El chef reprueba el examen|
| Dia dan chef memasak makanan| Él/Ella y el chef cocinan comida|
| Seorang anak dan seorang wanita berbagi pizza| Un niño y una mujer comparten pizza|
| Anjing atau kucing mengejar domba| El perro o el gato persigue un cordero|
| Dia membakar sebuah rumah dan sebuah mobil| Él/Ella incendia una casa y un automóvil|
| Dia akan membeli sebuah rumah atau dua mobil| Él/Ella comprará una casa o dos automóviles|
| Seekor anjing atau seekor kucing atau seekor domba makan rumput| Un perro o un gato o un cordero come hierba|
| Dia dan chef membeli sebuah rumah dan sebuah mobil| Él/Ella y el chef compran una casa y un automóvil|
| Seorang wanita dan seorang siswa sudah membeli workstation| Una mujer y un estudiante ya compraron una workstation|
| Chef berbagi pizza dan makanan| El chef comparte pizza y comida|
| Dia atau siswa akan membeli rumah| Él/Ella o el estudiante comprará una casa|


Cadenas que no deberían de aceptarse:

| Indonesio | Español | Motivo |
|-|-|-|
| Memasak dia makanan | Cocina él/ella comida | Viola el orden SVO activo, por empezar con el verbo |
| Memasak makanan | Cocina comida | Faltó el sujeto |
| Dia memasak cepat makanan | Él/Ella cocina rápidamente comida | Introduce un modificador adverbial, estructura no modelada |
| Dia untuk restoran | Él/Ella para el restaurante | No hay sintagma verbal |
| Dia akan sudah membeli rumah | Él/Ella habrá ya comprado una casa | La gramática sólo permite una partícula temporal antes del verbo. |
| Dia memasak | Él/Ella cocina | Falta el objeto |


# Modelando la gramática

Se considerarán los siguientes sintagmas:
- Sustancial, `STGMS`
- Verbal, `STGMV`
- Objetual, `STGMO`

Cada uno de ellos representa un símbolo no-terminal.

También se categorizaron símbolos terminales bajo las siguientes categorías:

<ul>
    <li><details><summary><code>c</code>, conjunciones:</summary>
        <ul>
            <li> Dan - Y
            <li> Atau - O
        </ul>
    </details>
    <li><details><summary><code>d</code>, determinantes:</summary>
        <ul>
            <li> Seorang - Un/Una (persona)
            <li> Seekor - Un/Una (animal)
            <li> Satu - Uno
            <li> Dua - Dos
            <li> Sembilan - Nueve
            <li> Sebuah - A
        </ul>
    </details>
    <li><details><summary><code>n</code>, sustantivos/pronombres:</summary>
        <ul>
            <li> Dia - Él/Ella
            <li> Anak - Niña/Niño
            <li> Wanita - Señora
            <li> Chef - Chef
            <li> Anjing - Perro
            <li> Kucing - Gato
            <li> Domba - Cordero
            <li> Pizza - Pizza
            <li> Makanan - Comida
            <li> Rumah - Casa
            <li> Mobil - Auto
            <li> Rumput - Hierba
            <li> Workstation - Workstation
            <li> Siswa - Alumno
            <li> Ujian - Examen
            <li> Restoran - Restaurante
        </ul>
        </details>
    <li><details><summary><code>p</code>, partículas temporales:</summary>
        <ul>
            <li> Akan - Futuro
            <li> Sudah - Pasado/Ya
        </ul>
    </details>
    <li><details><summary><code>v</code>, verbos:</summary>
        <ul>
            <li> Memasak - Cocinar
            <li> Berbagi - Compartir
            <li> Mengejar - Perseguir
            <li> Makan - Comer
            <li> Membakar - Incendiar
            <li> Membeli - Comprar
            <li> Gagal - Reprobar
        </ul>
    </details>
</ul>

# Gramática Base

1. Oración Principal:

$O \to STGMS \quad STGMV \quad STGMO$

2. Sintagma Sustancial/Objetual:

$STGMS \to STGMS \quad c \quad STGMS$

$STGMS \to d \quad n$

$STGMS \to n$

$STGMO \to STGMO \quad c \quad STGMO$

$STGMO \to d \quad n$

$STGMO \to n$

3. Sintagma Verbal:

$STGMV \to p \quad v$

$STGMV \to v$

## Demostración de ambigüedad

La siguiente cadena  _"Anjing atau kucing atau domba makan rumput"_, servirá para demostrar la ambigüedad y recursión izquierda de la gramática base, pues siguiendo las producciones, hay dos árboles sintácticos distintos que permiten llegar a esta.
```text
                                         O                                        
                             ____________|____________________________________     
                          STGMS                                         |     |   
                       _____|_______________________________            |     |    
                    STGMS                      |            |           |     |   
          ____________|____________            |            |           |     |    
       STGMS          |          STGMS         |          STGMS       STGMV STGMO 
   ______|_____       |      ______|_____      |      ______|_____      |     |    
  D            N      C     D            N     C     D            N     V     N   
  |            |      |     |            |     |     |            |     |     |    
seekor       anjing  atau seekor       kucing atau seekor       domba makan rumput

                                        O                                         
                            ____________|_____________________________________     
                         STGMS                                          |     |   
          _________________|___________________                         |     |    
         |           |                       STGMS                      |     |   
         |           |             ____________|____________            |     |    
       STGMS         |          STGMS          |          STGMS       STGMV STGMO 
   ______|_____      |      ______|_____       |      ______|_____      |     |    
  D            N     C     D            N      C     D            N     V     N   
  |            |     |     |            |      |     |            |     |     |    
seekor       anjing atau seekor       kucing  atau seekor       domba makan rumput
```

Tal como menciona Møller et al. (2007) "$G$ is ambiguous if there exists a string $x$ in $L(G)$ with multiple derivation trees, and we then say that $x$ is ambiguous relative to $G$" (p.4)

En su estado actual, la gramática es ambigua y cuenta con recursión izquierda, por lo tanto, no puede ser analizada por LL(1).

## Eliminando ambigüedad

La ambigüedad de la gramática original proviene de:

$STGMS \to STGMS \quad c \quad STGMS$

$STGMO \to STGMO \quad c \quad STGMO$

Los sintagmas, puestos de esta manera, buscan agrupar conjunciones de distinta forma pero **lleva a que la misma cadena pueda obtenerse de dos árboles sintácticos diferentes**.

Para solucionar este problema, se creó una estructura común para las nominales `STGMS` y `STGMO`, que permite mediante los bloques `E` y `B` alcanzar las distintas combinaciones que la gramática ambigua.

## Eliminando recursividad izquierda

La solución recién descrita, también permite la extensión iterativa de sustantivos **sin que el símbolo que genera a las producciones sea su símbolo más a la izquierda (inicial)**.

Además, se conservó intacto el sintagma verbal, pues este no presentaba recursión izquierda, y se mantiene su estructura simple para asegurar la consistencia del lenguaje SVO.

# Gramática Final

La estructura final que acepta el subconjunto del indonesio planteado sin ambigüedad es:

$O \to STGMS \quad STGMV \quad STGMO$

$STGMS \to B \quad E$

$STGMO \to B \quad E$

$E \to c \quad B \quad E | ε$

$B \to d \quad n | n$

$STGMV \to p \quad v | v$

# Pruebas
## Puesta en marcha
    Ambiente: Python 3.13.15, NLTK 3.9.1-2

Consideraciones:
1. Instalar python (de no tenerlo)
2. Instalar la librería NLTK
    - En Debian 13, se utilizó `sudo apt install python3-nltk`, para instalar la versión 3.9.1-2.
    - Al parecer, en Windows el comando es `pip install nltk` y descargaría la versión más reciente.
3. Descargar este repositorio y navegar hasta su directorio

Con las consideraciones resueltas, es posible poner a prueba la gramática.

Para ello, ejecutar el script desde la terminal:
* En Debian 13, `python3 analizar_cadenas.py`.
* En Windows, `python analizar_cadenas.py`

## Detalles
En el archivo `analizar_cadenas.py` se encuentran incluidas las oraciones anteriormente descritas como válidas e inválidas, bajo un diccionario donde la clave es una oración en indonesio y el valor la oración traducida al español.

El uso de NLTK fue conveniente pues, además de ser recomendada por el profesor, por ser un 'toolkit' para el procesamiento de lenguaje natural, facilitó la tarea de crear el parser necesario para determinar la validez de toda cadena compuesta por los símbolos terminales y la gramática en general.

En concreto, fue la clase `CFG` mediante la cual disponemos del método `fromstring` que nos permite instanciar un objeto `grammar` usando nuestra gramática como string. Dicha instancia fue necesaria para construir el analizador pasándola al `ChartParser` se encargará de analizar texto con la gramática que le fue dada utilizando, por defecto, una combinación de reglas que pretenden abarcar 

Aunque `ChartParser` utilice estrategias basadas en programación dinámica (NLTK :: nltk.parse.chart Module, s. f.), si la gramática es LL(1), el parser trabajará sin ambigüedad, pues eso es una propiedad de la gramática (compatible con LL(1)) y en la práctica el `ChartParse` encontrará una única derivación.

## Demostración de cadenas válidas

<details><summary>Desplegar</summary>

```text
---------------------------------------------
ANÁLISIS DE CADENAS CORRECTAS
---------------------------------------------

CADENA 1:

ACEPTADA: "Dia memasak makanan" (Él/Ella cocina comida)
---------------------------------------------

CADENA 2:

ACEPTADA: "Chef membakar rumah" (El chef incendia una casa)
---------------------------------------------

CADENA 3:

ACEPTADA: "Seorang wanita membeli sebuah mobil" (Una mujer compra un automóvil)
---------------------------------------------

CADENA 4:

ACEPTADA: "Anjing mengejar kucing" (El perro persigue al gato)
---------------------------------------------

CADENA 5:

ACEPTADA: "Seekor domba makan rumput" (Un cordero come hierba)
---------------------------------------------

CADENA 6:

ACEPTADA: "Dia akan membeli sebuah rumah" (Él/Ella comprará una casa)
---------------------------------------------

CADENA 7:

ACEPTADA: "Dia sudah memasak makanan" (Él/Ella ya cocinó comida)
---------------------------------------------

CADENA 8:

ACEPTADA: "Seorang anak berbagi pizza" (Un niño/una niña comparte pizza)
---------------------------------------------

CADENA 9:

ACEPTADA: "Siswa membeli workstation" (Un estudiante compra una workstation)
---------------------------------------------

CADENA 10:

ACEPTADA: "Chef gagal ujian" (El chef reprueba el examen)
---------------------------------------------

CADENA 11:

ACEPTADA: "Dia dan chef memasak makanan" (Él/Ella y el chef cocinan comida)
---------------------------------------------

CADENA 12:

ACEPTADA: "Seorang anak dan seorang wanita berbagi pizza" (Un niño y una mujer comparten pizza)
---------------------------------------------

CADENA 13:

ACEPTADA: "Anjing atau kucing mengejar domba" (El perro o el gato persigue un cordero)
---------------------------------------------

CADENA 14:

ACEPTADA: "Dia membakar sebuah rumah dan sebuah mobil" (Él/Ella incendia una casa y un automóvil)
---------------------------------------------

CADENA 15:

ACEPTADA: "Dia akan membeli sebuah rumah atau dua mobil" (Él/Ella comprará una casa o dos automóviles)
---------------------------------------------

CADENA 16:

ACEPTADA: "Seekor anjing atau seekor kucing atau seekor domba makan rumput" (Un perro o un gato o un cordero come hierba)
---------------------------------------------

CADENA 17:

ACEPTADA: "Dia dan chef membeli sebuah rumah dan sebuah mobil" (Él/Ella y el chef compran una casa y un automóvil)
---------------------------------------------

CADENA 18:

ACEPTADA: "Seorang wanita dan seorang siswa sudah membeli workstation" (Una mujer y un estudiante ya compraron una workstation)
---------------------------------------------

CADENA 19:

ACEPTADA: "Chef berbagi pizza dan makanan" (El chef comparte pizza y comida)
---------------------------------------------

CADENA 20:

ACEPTADA: "Dia atau siswa akan membeli rumah" (Él/Ella o el estudiante comprará una casa)
---------------------------------------------
```

</details>

## Demostración de cadenas inválidas

<details><summary>Desplegar</summary>


```text
---------------------------------------------
ANÁLISIS DE CADENAS INCORRECTAS
---------------------------------------------

CADENA 1:

RECHAZADA: "Memasak dia makanan" (Cocina él/ella comida )
---------------------------------------------

CADENA 2:

RECHAZADA: "Memasak makanan" (Cocina comida)
---------------------------------------------

CADENA 3:

RECHAZADA: "Dia akan sudah membeli rumah" (Él/Ella habrá ya comprado una casa)
---------------------------------------------

CADENA 4:

RECHAZADA: "Dia memasak" (Él/Ella cocina)
---------------------------------------------
```

</details>

# Análisis de las gramáticas

## Complejidad
Para la gramática base, dada la ambigüedad y la recursión izquierda, requiere del uso de algoritmos como Earley que suponen una complejidad de $O(n³)$ en el peor de los casos, debido al número de estados derivables (proporcional al tamaño de la cadena), y a las operaciones de escaneo, predicción y completado del algoritmo para cada estado,  (Earley, 1970, p.98)

En cuanto a la gramática final compatible para el análisis por LL(1), que sería determinístico, no supondría la necesidad de realizar búsquedas exhaustivas, al haber como máximo una regla aplicable por paso, manteniendo $O(n)$, considerando que "A parser is deterministic if at each step there is at most one rule that can successfully extend the current derivation" (Sudkamp, 2006, último párrafo de inicio de part V).

En LL(1), ello supone el consumo de un token, en cada paso, de la cadena dada para su análisis o el aplicar una regla de forma directa sin backtracking, y por ello el número total de operaciones es directamente proporcional a la longitud de la cadena de entrada (n).

## Estructura de las producciones
La estructura de las producciones de ambas gramáticas obedecen a la forma $A \to B$, donde $A$ es exclusivamente un símbolo no terminal y $B$ puede contener no terminales y terminales, sólo terminales o cadena vacía (GeeksforGeeks, 2026)

Lo que las diferencia es la cantidad de reglas para llegar a determinada cadena,  por tanto, el número de operaciones.

# Conclusión

Esta gramática final representa una solución al problema toda vez que se elimina la recursión izquierda y la ambigüedad, de manera que la gramática puede ser procesada por analizadores sintácticos descendentes como el LL(1), determinista, que lee y deriva de izquierda a derecha con un token de anticipación.

Y finalmente, porque mantiene el alcance de la primera gramática, pues acepta cadenas que se apegan a la estructura SVO requerida.

# Referencias
- Brabrand, C., Giegerich, R., Møller, A. (2007). Analyzing Ambiguity of Context-Free Grammars. In: Holub, J., Žďárek, J. (eds) Implementation and Application of Automata. CIAA 2007. Lecture Notes in Computer Science, vol 4783. Springer, Berlin, Heidelberg. https://doi.org/10.1007/978-3-540-76336-9_21

- Earley, J.(1970) (2) An efficient context-free parsing algorithm, Communications of the ACM 13 

- Sudkamp, T. A. (2006). Languages and Machines: An Introduction to the Theory of Computer Science. Addison-Wesley Longman.

- GeeksforGeeks. (2026a, febrero 12). Chomsky Hierarchy in Theory of Computation. GeeksforGeeks. https://www.geeksforgeeks.org/theory-of-computation/chomsky-hierarchy-in-theory-of-computation/

- NLTK :: nltk.parse.chart module. (s. f.). https://www.nltk.org/api/nltk.parse.chart.html
