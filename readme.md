# Applicacion of Flask with SQLITE and Apicoin

The program is done in Python with Apicoin and the Flask framework and SQLite

# Instalacion
- create a virtual enviorenment in Python and insert the commands in your Terminal
```
pip install -r requirements.txt
```
The library used in Flask https://flask-wtf.readthedocs.io/en/1.2.x/

# Program execution
 - start the flask server
 - on mac: 
  ```export FLASK_APP=main.py```
 - on windows:
  ```set FLASK_APP=main.py```

# Another option to execute the program 
  - create an archive .env and inside what´s next:
  ``` FLASK_APP=main.py ```
  ``` FLASK_DEBUG=True ```
  - this is to be able to execute the program with:
  ``` flask run ```

# Command to execute the server
 ```flask --app main run```

# Command to execute the server in a different port for default different than 5000
```flask --app main run -p 5002```

# Command to execute the server in debug mode, to realize changes in real time
```flask --app main --debug run```