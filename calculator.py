#!/usr/bin/python

body = None

def resolve_url(path):

    url = path

    operators = []


    path = filter(None, path)



    if url[1] == 'add':

        for i in url[2:]:
            try:

                i = int(i)
                operators.append(i)
            except ValueError:
                url.remove(i)

                raise ValueError
                #body = "It looks like you used an invalid input!"

                #return body

        #body = 'The list of operands is: {}, and the sum is: {}'.format(str(operators), str(sum(operators)))
        body = '<h1>The sum is: {}</h1>'.format(str(sum(operators)))

    elif url[1] == 'subtract':
        
        for i in url[2:]:

            try:

                i = int(i)
                operators.append(i)


                
                #print 'subtraction results: ', subtract_results

            except ValueError:
                raise NameError
                #url.remove(i)
                #body = "It looks like you used an invalid input!"

                #return body

        body = '<h1>The difference is: {}</h1>'.format(str(operators[0] - sum(operators[1:])))#, str(type(sum(operators[1:])))

    elif url[1] == 'multiply':
        
        for i in url[2:4]:

            try:

                i = int(i)
                operators.append(i)

            except ValueError:
                #url.remove(i)
                #body = "It looks like you used an invalid input!"

                #return body
                raise ValueError

        product = operators[0]*operators[1]

        product = str(product)

        body = '<h1>The product is: {</h1>}'.format(product)

    elif url[1] == 'divide':
        
        for i in url[2:4]:

            try:

                i = float(i)
                operators.append(i)

            except ValueError:
                #url.remove(i)
                raise ValueError

        try: 

            quotient = operators[0]/operators[1]

            body = '<h1>The quotient is: {}</h1>'.format(quotient)

        except ZeroDivisionError:
            
            #body = "It looks like you tried to divide by zero, now the world is ending. Nice job. I hope you're happy. "

            raise ValueError
                            

    elif str(path) == "['/']":
        index = open('index.html','rb')
        body = index.read()
        #body = 'bananas'

    else: 
        body = 'The URL is: {}'.format(url)

    print 'url is ', url
    return body

def application(environ, start_response):

    headers = [("Content-type", "text/html")]
    try:
        path = environ.get('PATH_INFO', None)
        if path is None:
            raise NameError
        #print 'path is: ', path
 
        
        path = list(path.split('/'))

        path[0] = '/'

        print 'path is: ', path
#        print 'path type is: ', type(path)

        body = resolve_url(path)
        print 'body is ', body

        #func, args = resolve_path(path)
        #body = func(*args)
        #body = "<h1>Testing Testing</h1>"
        status = "200 OK"

    except NameError:
        status = "404 Not Found"
        body = "<h1>Not Found</h1>"
    except ValueError:
        status = "400 Not Found"
        body = "<h1>Bad Request</h1><br / ><h2>Maybe you used an invalid input?</h2>"
    except Exception:
        status = "500 Internal Server Error"
        body = "<h1>Internal Server Error</h1>"
    finally:
        headers.append(('Content-length', str(len(body))))
        start_response(status, headers)
        #return [body] 
        return body 

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8000, application)
    srv.serve_forever()

