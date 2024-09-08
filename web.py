from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(self.get_response().encode("utf-8"))

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

