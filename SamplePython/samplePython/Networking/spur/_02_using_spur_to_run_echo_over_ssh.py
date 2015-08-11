import spur

shell= spur.SshShell(hostname='172.16.191.27', username='kyi', password='0608810', missing_host_key=spur.ssh.MissingHostKey.accept,)
with shell:
    result = shell.run(["echo", "-n", "hello"])
print "result =",result.output 