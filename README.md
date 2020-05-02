## Obstagoon
A general purpose blog generator.
Python 3.6+

## Guide
Env setup:
```
python3 -m venv venv
source venv/bin/activate
```
Generates a markdown file in /content/posts. You have to manually change the filename for now
```
python3 main.py newpost
```
Generates a build folder and fills in templates
```
python3 main.py build
```
cd into /build and run the following to host locally
```
cd build
python3 -m http.server
```