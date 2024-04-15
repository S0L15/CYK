Implementación del algoritmo Cocke-Younger-Kasami

El formato de la entrada es:
    -Una línea con un número n que indica cuantos casos vienen (3 en el archivo 'test-cky.in')
    -Dos enteros, en la misma línea separados por un espacio en blanco, k y m, donde k es el número de no terminales y m es el número de cadenas que se van a analizar
    -Ahora, k líneas con las producciones, con el formato:
        <no terminal> <alternativas de derivación del símbolo no terminal separadas por espacios en blanco>
    -Luego, m líneas con las cadenas que se van a analizar

La salida es:
    -Se imprimen m líneas, cada una contiene una de dos opciones: 'yes', si la cadena puede ser generada por la gramática, o 'no', si no es así.

Se asume que 'S' es el símbolo inicial y que la gramática está en forma normal de Chomsky.

Encontrar una gramática en la forma normal de Chomsky para el conjunto de palabras 

{a^n b^2n c^k | n,k >= 1}

Seleccionar 3 palabras, 2 de ellas que sean sentencias y la tercera no, y agregarlos al archivo adjunto para ejecutarlos con el algoritmo inicial para validar funcionalidad.

Conversión del conjunto de palabras a una GLC:
    S -> aSbb | B
    B -> Bc | c

Conversión de la GLC a la forma normal de Chomsky (FNC):
    S -> EF|BC|c
    B -> BC|c
    A -> a
    C -> c
    D -> b
    E -> AS
    F -> DD