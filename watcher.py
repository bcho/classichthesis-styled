from livereload import Server, shell

server = Server()


def compile_scss():
    shell('sass -t compressed --scss %s %s' % (
        'scss/style.scss', 'css/style.css'
    ))()
    shell('sass -t compressed --scss %s %s' % (
        'scss/print.scss', 'css/print.css'
    ))()


server.watch('./scss/', compile_scss)
server.watch('./*.html')

server.serve()
