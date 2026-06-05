import nltk
from nltk import CFG, ChartParser

# CADENAS CORRECTAS
cadenas_correctas = {
    "Dia memasak makanan":
        "Él/Ella cocina comida",
    "Chef membakar rumah":
        "El chef incendia una casa",
    "Seorang wanita membeli sebuah mobil":
        "Una mujer compra un automóvil",
    "Anjing mengejar kucing":
        "El perro persigue al gato",
    "Seekor domba makan rumput":
        "Un cordero come hierba",
    "Dia akan membeli sebuah rumah":
        "Él/Ella comprará una casa",
    "Dia sudah memasak makanan":
        "Él/Ella ya cocinó comida",
    "Seorang anak berbagi pizza":
        "Un niño/una niña comparte pizza",
    "Siswa membeli workstation":
        "Un estudiante compra una workstation",
    "Chef gagal ujian":
        "El chef reprueba el examen",
    "Dia dan chef memasak makanan":
        "Él/Ella y el chef cocinan comida",
    "Seorang anak dan seorang wanita berbagi pizza":
        "Un niño y una mujer comparten pizza",
    "Anjing atau kucing mengejar domba":
        "El perro o el gato persigue un cordero",
    "Dia membakar sebuah rumah dan sebuah mobil":
        "Él/Ella incendia una casa y un automóvil",
    "Dia akan membeli sebuah rumah atau dua mobil":
        "Él/Ella comprará una casa o dos automóviles",
    "Seekor anjing atau seekor kucing atau seekor domba makan rumput"
        : "Un perro o un gato o un cordero come hierba",
    "Dia dan chef membeli sebuah rumah dan sebuah mobil":
        "Él/Ella y el chef compran una casa y un automóvil",
    "Seorang wanita dan seorang siswa sudah membeli workstation":
        "Una mujer y un estudiante ya compraron una workstation",
    "Chef berbagi pizza dan makanan":
        "El chef comparte pizza y comida",
    "Dia atau siswa akan membeli rumah":
        "Él/Ella o el estudiante comprará una casa",
}

# CADENAS INCORRECTAS
cadenas_incorrectas = {
    "Memasak dia makanan":
        "Cocina él/ella comida ",
    "Memasak makanan":
        "Cocina comida",
    "Dia akan sudah membeli rumah":
        "Él/Ella habrá ya comprado una casa",
    "Dia memasak":
        "Él/Ella cocina"
}


# IMPLEMENTACIÓN DE LA GRAMÁTICA LIBRE DE CONTEXTO
gramaticaIndonesio = CFG.fromstring("""
O -> STGMS STGMV STGMO

STGMS -> B E
STGMO -> B E

E -> C B E
E ->

B -> D N
B -> N

STGMV -> P V
STGMV -> V

C -> 'dan'
C -> 'atau'

D -> 'seorang'
D -> 'seekor'
D -> 'satu'
D -> 'dua'
D -> 'sembilan'
D -> 'sebuah'

N -> 'dia'
N -> 'anak'
N -> 'wanita'
N -> 'chef'
N -> 'anjing'
N -> 'kucing'
N -> 'domba'
N -> 'pizza'
N -> 'makanan'
N -> 'rumah'
N -> 'mobil'
N -> 'rumput'
N -> 'workstation'
N -> 'siswa'
N -> 'ujian'
N -> 'restoran'

P -> 'akan'
P -> 'sudah'

V -> 'memasak'
V -> 'berbagi'
V -> 'mengejar'
V -> 'makan'
V -> 'membakar'
V -> 'membeli'
V -> 'gagal'
""")

parser = ChartParser(gramaticaIndonesio)

# ANÁLISIS SINTÁCTICO DE CADENAS
def analiza_cadenas(cadenas: dict[str,str]):
    """
    Análisis sintáctico de las cadenas contenidas en un diccionario

    Args:
    cadenas: diccionario con cadenas en indonesio como clave \
    y cadenas en español como valor.
    """
    cnt = 1

    for cadena in cadenas:
        tokens = cadena.lower().split()

        parse_trees = list(parser.parse(tokens))

        print(f"CADENA {cnt}:\n")

        if parse_trees:
            print(f'ACEPTADA: "{cadena}" ({cadenas[cadena]})')

            # GRAFICAR ÁRBOL
            for pt in parse_trees:
                pt.pretty_print()

        else:
            print(f'RECHAZADA: "{cadena}" ({cadenas[cadena]})')
        
        cnt+=1
        print("---------------------------------------------\n")

def main():
    print("---------------------------------------------")
    print("ANÁLISIS DE CADENAS CORRECTAS")
    print("---------------------------------------------\n")
    
    analiza_cadenas(cadenas_correctas)

    print("---------------------------------------------")
    print("ANÁLISIS DE CADENAS INCORRECTAS")
    print("---------------------------------------------\n")
    
    analiza_cadenas(cadenas_incorrectas)

if __name__=="__main__":
    main()