from livereload import Server

server = Server()

# Добавить файл для отслеживания изменений
server.watch('index.html')
server.watch('static/styles.css')
server.watch('static/player.js')

# Обслуживание текущего каталога (где должен находиться index.html)
server.serve(root='.')