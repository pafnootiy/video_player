from livereload import Server

server = Server()
# server.watch('sample.html')
server.watch('index1.html')
server.serve(root='.')
