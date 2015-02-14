#!/usr/bin/python

body = None

def resolve_url(path):
    url = path
    url = list(url.split('/'))

    operators = []
    if url[1] == 'add':

        #output = int(url[2]) + int(url)

        for i in range(2,-1):
            operators.append(i)
        body = operators

    print 'url is ', url
    return body

def application(environ, start_response):

    headers = [("Content-type", "text/html")]
    try:
        path = environ.get('PATH_INFO', None)
        if path is None:
            raise NameError
        print 'path is: ', path
        
        path = list(path.split('/'))

        print 'path is: ', path

        body = resolve_url(path)
        print 'body is ', body

        #func, args = resolve_path(path)
        #body = func(*args)
        #body = "<h1>Testing Testing</h1>"
        status = "200 OK"

    except NameError:
        status = "404 Not Found"
        body = "<h1>Not Found</h1>"
    #except Exception:
    #    status = "500 Internal Server Error"
    #    body = "<h1>Internal Server Error</h1>"
    finally:
        headers.append(('Content-length', str(len(body))))
        start_response(status, headers)
        #return [body] 
        return body 

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8000, application)
    srv.serve_forever()

