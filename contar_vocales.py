import unittest


def contar_vocales(palabra):
    contador_a= 0
    contador_e= 0
    contador_i= 0
    contador_o= 0
    contador_u= 0
    resultado = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    
    for i in palabra:
        if i == "a" or i == "A":
            contador_a = contador_a + 1
        elif i == "e" or i == "E":
            contador_e = contador_e + 1
     
        elif i == "i" or i == "I":
            contador_i = contador_i + 1
     
        elif i == "o" or i == "O":
            contador_o = contador_o + 1
            
        elif i == "u" or i == "U":
            contador_u = contador_u + 1


    
    
    resultado["a"] = contador_a
    resultado["e"] = contador_e
    resultado["i"] = contador_i
    resultado["o"] = contador_o
    resultado["u"] = contador_u
    
    if resultado["a"] == 0:
        del resultado["a"]
    if resultado["e"] == 0:
        del resultado["e"]
    if resultado["i"] == 0:
        del resultado["i"]
    if resultado["o"] == 0:
        del resultado["o"]
    if resultado["u"] == 0:
        del resultado["u"]    

    
    return resultado

class TestContarVocales(unittest.TestCase):
    def test_sin_vocales(self):
        palabra = "tryhgf"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {})

    def test_con_vocal_o(self):
        palabra = "sol"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"o": 1})

    def test_con_vocal_doble_o(self):
        palabra = "solo"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"o": 2})

    def test_con_dos_vocales(self):
        palabra = "sola"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"o": 1, "a": 1})

    def test_con_todas_las_vocales(self):
        palabra = "solamente quiero que gane Boca"
        resultado = contar_vocales(palabra)
        self.assertEqual(
            resultado,
            {"a": 3, "e": 5, "i": 1, "o": 3, "u": 2},
        )

    def test_con_vocales_en_mayuscula(self):
        palabra = "SOlAmente quIerO"
        resultado = contar_vocales(palabra)
        self.assertEqual(
            resultado,
            {"a": 1, "e": 3, "i": 1, "o": 2, "u": 1},
        )
        
unittest.main()