"""
Multiple commands can be connected into a pipeline, similar to the way the UNIX
shell works, by creating separate Popen instances and chaining their inputs and outputs
together. The stdout attribute of one Popen instance is used as the stdin argument
for the next in the pipeline, instead of the constant PIPE . The output is read from the
stdout handle for the final command in the pipeline.
"""
import subprocess
cat = subprocess.Popen(['cat', 'index.rst'], stdout=subprocess.PIPE,)
grep = subprocess.Popen(['grep', '.. include::'], stdin=cat.stdout, stdout=subprocess.PIPE,)
cut = subprocess.Popen(['cut', '-f', '3', '-d:'],
                        stdin=grep.stdout,
                        stdout=subprocess.PIPE,
                       )
end_of_pipe = cut.stdout
print 'Included files:'
for line in end_of_pipe:
    print '\t', line.strip()