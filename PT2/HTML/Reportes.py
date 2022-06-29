from os import startfile


class HTML():

    def createHTMLToken(self, name_html, lista):
        file = open('PT2/HTML/tabla_tokens/css-table-16/{}-tokens.html'.format(name_html),
                    'w+', encoding='utf-8')

        body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="fonts/icomoon/style.css">

    <link rel="stylesheet" href="css/owl.carousel.min.css">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/bootstrap.min.css">
    
    <!-- Style -->
    <link rel="stylesheet" href="css/style.css">
    <title>{name_html}</title>
</head>"""

        body = body + f"""
<body>
        """

        body = body + f"""
    <div class="content">
        <div class="container">
            <h2 class="mb-5">Tokens</h2>
            <div class="table-responsive">
        """
        
        body = body + f"""
                <table class="table table-striped custom-table">
                    <thead>
                        <tr>
                            <th scope="col">Identificador</th>
                            <th scope="col">Token</th>
                            <th scope="col">Descripcion</th>
                            <th scope="col">Fila</th>
                            <th scope="col">Columna</th>
                            <th scope="col">Patron</th>
                        </tr>
                    </thead>
                    <tbody>
        """


        # ? Contenido BODY HTML
        for elemento in lista:
            id = elemento.id
            lex = elemento.valor
            descripcion = lex.descripcion
            valor = lex.valor
            fila = lex.fila
            columna = lex.col
            patron = lex.patron
            body = body + f"""  
                        <tr scope="row">
                            <td><a href="#" class="more">{id}</a></td>
                            <td>{valor}</td>
                            <td>{descripcion}</td>
                            <td>{fila}</td>
                            <td>{columna}</td>
                            <td><a href="#" class="more">{patron}</a></td>
                        </tr>"""

        body = body + f"""
                    </tbody>
                </table>
            </div>
        </div>
    </div>"""


        body = body + f"""
    <script src="js/jquery-3.3.1.min.js"></script>
    <script src="js/popper.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/main.js"></script>
</body>
        """

        body = body + f"""
</html>"""

        file.write(body)
        file.close()

        index = 'PT2\\HTML\\tabla_tokens\\css-table-16\\{}-tokens.html'.format(
            name_html)
        startfile(index)

    def createHTMLError(self, name_html, lista):
        file = open('PT2/HTML/tabla_tokens/css-table-16/{}-errores.html'.format(name_html),
                    'w+', encoding='utf-8')

        body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="fonts/icomoon/style.css">

    <link rel="stylesheet" href="css/owl.carousel.min.css">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/bootstrap.min.css">
    
    <!-- Style -->
    <link rel="stylesheet" href="css/style.css">
    <title>{name_html}</title>
</head>"""

        body = body + f"""
<body>
        """

        body = body + f"""
    <div class="content">
        <div class="container">
            <h2 class="mb-5">Errores</h2>
            <div class="table-responsive">
        """

        body = body + f"""
                <table class="table table-striped custom-table">
                    <thead>
                        <tr>
                            <th scope="col">Fila</th>
                            <th scope="col">Columna</th>
                            <th scope="col">Tipo</th>
                            <th scope="col">Descripcion</th>
                        </tr>
                    </thead>
                    <tbody>
        """

        # ? Contenido BODY HTML
        for elemento in lista:
            fila = elemento.fila
            columna = elemento.col
            tipo = elemento.type
            descripcion = elemento.description
            body = body + f"""  
                        <tr scope="row">
                            <td>{fila}</td>
                            <td>{columna}</td>
                            <td>{tipo}</td>
                            <td><a href="#" class="more">{descripcion}</a></td>
                        </tr>"""

        body = body + f"""
                    </tbody>
                </table>
            </div>
        </div>
    </div>"""

        body = body + f"""
    <script src="js/jquery-3.3.1.min.js"></script>
    <script src="js/popper.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/main.js"></script>
</body>
        """

        body = body + f"""
</html>"""

        file.write(body)
        file.close()

        index = 'PT2\\HTML\\tabla_tokens\\css-table-16\\{}-errores.html'.format(
            name_html)
        startfile(index)
