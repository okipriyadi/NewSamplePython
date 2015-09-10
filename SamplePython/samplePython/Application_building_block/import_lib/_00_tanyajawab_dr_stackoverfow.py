"""
perbedaan antara import VS __import__() VS importlib.import_module()

PERTANYAAN :
I am starting to delve into deeper aspects of python by reading the source of major frameworks 
and encountered this immediately, where Flask was using Werkzeug to __import__ a module, and 
I was a little confused. I went and checked out the docs on it and saw that it seems 
to give you more control somehow in terms of where it looks for the module, 
but I'm not sure exactly how and I have zero idea how it's different 
from importlib.import_module.

The odd thing in the Werkzeug example is that it just says __import__(import_name), 
so I don't see how that's any different from just using the import statement, 
since it's ignoring the optional extra parameters.

Can anyone explain? I looked at other people having asked similar questions on 
SO previously but they weren't very clearly phrased questions and the answers didn't 
address this at all.


JAWABAN: 
__import__ is a low-level hook function that's used to import modules; 
it can be used to import a module dynamically by giving the module name to import as a 
variable, something the import statement won't let you do.

importlib.import_module() is a wrapper around that hook to produce a nice API 
for the functionality; it is a very recent addition to Python 2, and has been more 
fleshed out in Python 3. Codebases that use __import__ generally do so because they want 
to remain compatible with older Python 2 releases, e.g. anything before Python 2.7.

One side-effect of using __import__ can be that it returns the imported module and doesn't 
add anything to the namespace; you can import with it without having then to delete the 
new name if you didn't want that new name; using import "somename" will add "somename" 
to your namespace, but __import__('somename') instead returns the imported module, 
which you can then ignore. Werkzeug uses the hook for that reason in one location.

All other uses are to do with dynamic imports. Werkzeug supports Python 2.6 still 
so cannot use importlib.
"""