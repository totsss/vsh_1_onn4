
from bottle import route, run, static_file
import os
@route('/static/<nafn>')
def static(nafn):
    return static_file(nafn,root='./static')


#Dæmi 2:
@route('/')
def index():


    return """
    <body>
      <h1>halló heimur!</h1><img src='static/gandalfeinn.jpg'>
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
          <h1>test eitthvað :) nr.1</h1>
                
                <a href='/steve/1'>test<a/>
                <a href='/steve/2'>biography<a/>
                <a href='/steve/3'>Error<a/>
                <a href='/'>forsida<a/>
        """
    if nr=='2':
        return """
          <h1>Undirsíða biography</h1>
          <h1>nr.2</h1>>
                
                <a href='/steve/1'>test<a/>
                <a href='/steve/2'>biography<a/>
                <a href='/steve/3'>Error<a/>
                <a href='/'>forsida<a/>
        """
    if nr=='3':
        return """
          <h1>Error This site can’t be reached. Error síða gg</h1>
          <a href='/steve/1'>test<a/>
          <a href='/steve/2'>biography<a/>
          <a href='/steve/3'>Error<a/>
          <a href='/'>forsida<a/>
          <h1> :( </h1>

        """
    
#run(host='localhost',port=8080,debug=True)
run(host='0.0.0.0',port=os.environ.get('PORT'))
