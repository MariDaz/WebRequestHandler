from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    #def query_data(self):
     #   return dict(parse_qsl(self.url().query))

    def do_GET(self):
        if self.path=="/":
            self.send_response(200)
            self.send_header("Content-Type","text/html") #se indica que es html
            self.end_headers()

            try:
                with open("home.html", "r", encoding="utf-8") as file:
                    content = file.read()  # Leer el contenido del archivo
                    self.wfile.write(content.encode("utf-8"))  # Escribirlo en la respuesta
            except FileNotFoundError:
                # Si no encontramos el archivo home.html, devolvemos un error
                self.wfile.write(b"<h1>Error: Archivo home.html no encontrado</h1>")
        else:
            self.send_error(404,"Pagina no encontrada")

    def get_response(self):

        path=self.url().path #ruta URL
        query_data=self.query_data() # parametros de la query string

        proyecto=path.split("/")[-1]
        autor=query_data.get("autor")
        return f"""
    <h1>Proyecto:{proyecto} Autor: {autor} </h1>
    <p> URL Parse Result : {self.url()}         </p>
    <p> Path Original: {self.path}         </p>
    <p> Headers: {self.headers}      </p>
    <p> Query: {self.query_data()}   </p>
"""


if __name__ == "__main__":
    
    print("Iniciando server en el puerto 8000")
    server = HTTPServer(("localhost", 8000), WebRequestHandler) #Se cambia el 8080 por 8000
    server.serve_forever()

