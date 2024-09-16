from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse



class WebRequestHandler(BaseHTTPRequestHandler):

    contenido = {
        '/': """<!DOCTYPE html>
                <html lang="es">
                <head><title>Pagina de Inicio</title></head>
                <body>
                    <h1>Hola mundo versión web</h1>
                    <p>Esta es la pagina principal, seleccione una de los siguientes links</p>
                    <a href="/proyecto/web-uno">Proyecto Web Uno</a><br>
                    <a href="/proyecto/web-dos">Proyecto Web Dos</a><br>
                    <a href="/proyecto/web-tres">Proyecto Web Tres</a><br>
                </body>
                </html>""",
        '/proyecto/web-uno': """<!DOCTYPE html>
                                <html lang="es">
                                <head><title> Pagina 1:</title></head>
                                <body>
                                    <h1>Hola profe:D</h1>
                                    <p>Este es el contenido del proyecto Web Uno.</p>
                                </body>
                                </html>""",
        '/proyecto/web-dos': """<!DOCTYPE html>
                                <html lang="es">
                                <head><title>Pagina 2</title></head>
                                <body>
                                    <h1>Proyecto: Hola profe 2 la venganza</h1>
                                    <p>Este es el contenido del proyecto Web Dos.</p>
                                </body>
                                </html>""",
        '/proyecto/web-tres': """<!DOCTYPE html>
                                <html lang="es">
                                <head><title>Pagina 3 </title></head>
                                <body>
                                    <h1>Proyecto: Hola profe: la trilogia</h1>
                                    <p>Este es el contenido del proyecto Web Tres.</p>
                                </body>
                                </html>"""
    }
    
    def do_GET(self):
        # Obtener la ruta solicitada
        path = self.path

        # Verificar si la ruta solicitada existe en el diccionario
        if path in self.contenido:
            # Si la ruta existe, enviar respuesta con el contenido correspondiente
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(self.contenido[path].encode("utf-8"))
        else:
            # Si la ruta no existe, enviar un error 404
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write("<h1>Error 404: Página no encontrada</h1>")


if __name__ == "__main__":
    
    print("Iniciando server en el puerto 8000")
    server = HTTPServer(("0.0.0.0", 8000), WebRequestHandler) #Se cambia el 8080 por 8000
    server.serve_forever()

