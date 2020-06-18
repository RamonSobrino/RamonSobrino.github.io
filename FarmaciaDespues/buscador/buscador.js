function doSearch(document) {
    var regExp1 = /field/;
    var regExp2 = /[(,),<,>,[,]]/;

    var s = document.getElementById('search');
    var str = s.value;
    if (str == "") {
        alert("El campo de búsqueda debe contener un valor.");
        s.focus();
    } else {
        if (typeof regExp1.source != 'undefined' &&
            (regExp1.test(str) || regExp2.test(str))) {
            s.focus();
            return alert("Algunos de los caracteres introducidos no están admitidos.");
        }

        addToDocument(document, str);
    }
}


function addToDocument(document, texto) {
    var paginas = indice[texto];
    if (typeof paginas != 'undefined') {
        var elementosEncontrados = "<p>Resultado de la búsqueda</p><ul>"
        for (var i = 0; i < paginas.length; i++) {
            elementosEncontrados += "<li><a href=\"" + paginas[i] + "\">" + paginas[i] + "</a></li>";
        }
        elementosEncontrados += "</ul>"
        document.getElementById("itemsSearch").innerHTML = elementosEncontrados;
    } else {
        document.getElementById("itemsSearch").innerHTML = "<p>Ningun elemento encontrado</p>";
    }
}