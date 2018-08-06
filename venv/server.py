from wsgiref.simple_server import make_server
from app import App


def error_handler(ex, req, resp, params):
    raise ex


if __name__ == '__main__':

    application = App()

    # TODO this is the place ehere you cna access all th registered routes
    # we can run a routine to check the uri_templates against our policies
    # wala = application._router._return_values

    application.add_error_handler(Exception, error_handler)
    port = 8181
    server = make_server('localhost', port, application)
    print('serving on {:d}'.format(port))
    server.serve_forever()
