
from bottle import route, run, static_file
@route('/static/<nafn>')
def static(nafn):
    return static_file(nafn,root='./static')


#Dæmi 2:
@route('/')
def index():


    return """
    <body>
      <h1>halló heimur!</h1><img src='static/gandalfeinn.jpg'>
      <a href='https://is.wikipedia.org/wiki/Steve_Jobs'>Steve Jobs</a>
      <a href='/steve/1'>test<a/>
      <a href='/steve/2'>biography<a/>
      <a href='/steve/3'>Error<a/>
      <link rel="stylesheet" type="text/css" href="static/style.css">
    </body>
      """

@route('/steve/<nr>')
def steve(nr):
    if nr=='1':
        return """
          <h1>Wow Þetta er ekki sama mynd marr</h1>
          <h1>þetta er myndin :)</h1><img src='./static/gandalfeinn.jpg'>
        """
    if nr=='2':
        return """
          <h1>Undirsíða 2</h1>
          <h1>þetta er myndin :)</h1><img src='./static/gandalfeinn.jpg'>
        """
    if nr=='3':
        return """
          <h1>Error This site can’t be reached.</h1>

        """






run(host='localhost',port=8080,debug=True)
