from http.server import BaseHTTPRequestHandler, HTTPServer
import loadenv
import serv.serv as serv

hostName = "0.0.0.0"
serverPort = 80

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), serv.MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
