import re
import string

palabrasReservadas = ["DOCTYPE", "html", "lang", "head", "meta", "charset", "utf", "link", "rel", "stylesheet"
    ,"type", "text", "css", "href", "script", "javascript", "src", "body", "section", "header", "class", "active"
    ,"nav", "span", "div", "img", "resourse", "article", "section"]
mapPalabras = {}


def incluirPalabras (fichero):
    document_text = open(fichero, mode='r', encoding="utf-8")
    match_pattern = re.findall(r' [a-zA-Z]{3}\w*', document_text.read())
    for palabraEncontrada in match_pattern:
        palabraTrip = palabraEncontrada.strip()
        if palabrasReservadas.count(palabraTrip) == 0:
            pages = mapPalabras.get(palabraTrip, [])
            if pages.count(fichero) == 0:
                pages.append(fichero)
                mapPalabras[palabraTrip] = pages
    document_text.close()


incluirPalabras('index.html')
incluirPalabras('historia.html')
incluirPalabras('parafarmacia.html')
incluirPalabras('contacto.html')

indexSalida = open("buscador/indice.js", mode='w', encoding="utf-8")
indexSalida.write("var indice = " + str(mapPalabras))
indexSalida.close()

