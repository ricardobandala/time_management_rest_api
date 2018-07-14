from wsgiref.simple_server import make_server
from app import App


def error_handler(ex, req, resp, params):
    raise ex


if __name__ == '__main__':

    application = App()
    application.add_error_handler(Exception, error_handler)

    server = make_server('localhost', 8181, application)
    print('serving on 8181')
    server.serve_forever()
