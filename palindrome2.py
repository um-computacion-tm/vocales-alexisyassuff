import unittest

def obtener_cantidad_de_lista_palindrome(lista):
    resultado=0
    for palabras in lista:
        palabras = palabras.replace(",", "").replace(":", "").replace("-", "").replace(" ", "").lower()
        if palabras == palabras[::-1]:
            resultado = resultado + 1
        else: pass
    return resultado
            


class TestCantidadDelistaPalindromes(unittest.TestCase):
    def test_cantidad_de_lista_palindromes_simple(self):
        lista = ["ala"]
        resultado = obtener_cantidad_de_lista_palindrome(lista)
        self.assertEqual(resultado, 1)

    def test_cantidad_de_lista_palindromes_con_2(self):
        lista = ["ala", "neuquen"]
        resultado = obtener_cantidad_de_lista_palindrome(lista)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_lista_palindromes_con_3(self):
        lista = ["ala", "neuquen", "hola"]
        resultado = obtener_cantidad_de_lista_palindrome(lista)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_lista_palindromes_con_4(self):
        lista = ["ala", "neuquen", "hola", "programacion"]
        resultado = obtener_cantidad_de_lista_palindrome(lista)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_lista_palindromes_con_5(self):
        lista = ["ala", "neuquen", "hola", "programacion", "palap"]
        resultado = obtener_cantidad_de_lista_palindrome(lista)
        self.assertEqual(resultado, 3)

    def test_cantidad_de_lista_palindromes_complejo(self):
        lista = ["ala", "neuquen", "hola", "programacion", "palap", "neu  quen"]
        resultado = obtener_cantidad_de_lista_palindrome(lista)
        self.assertEqual(resultado, 4)

    def test_cantidad_de_lista_palindromes_complejo_2(self):
        lista = [
            "ala",
            "neuquen",
            "hola",
            "programacion",
            "palap",
            "neu  quen",
            "agita falsos usos la fatiga",
            "presidente de la camara de diputados: martin menem",
			"A man, a plan, a canal - Panama"
        ]
        resultado = obtener_cantidad_de_lista_palindrome(lista)
        self.assertEqual(resultado, 6)
unittest.main()