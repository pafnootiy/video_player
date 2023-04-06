from livereload import Server

server = Server()
server.watch('index1.html')
server.serve(root='.')

