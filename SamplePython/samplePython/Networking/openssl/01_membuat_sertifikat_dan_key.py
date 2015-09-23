"""
============================================================================
HOW DO I GENERETE A SELF-SIGNED CERTIFICATE?
============================================================================

You’ll first need to decide whether or not you want to encrypt your key. 
Doing so means that the key is protected by a passphrase.

On the plus side, adding a passphrase to a key makes it more secure, 
so the key is less likely to be useful to someone who steals it. 
The downside, however, is that you’ll have to either store the passphrase 
in a file or type it manually every time you want to start your web or ldap server.

It violates my normally paranoid nature to say it, but I prefer unencrypted keys, 
so I don’t have to manually type a passphrase each time a secure daemon is started. 
(It’s not terribly difficult to decrypt your key if you later tire of typing a passphrase.)

This example will produce a file called mycert.pem which will contain both the 
private key and the public certificate based on it. 
The certificate will be valid for 365 days, 
and the key (thanks to the -nodes option) is unencrypted.
langsung cobain di cmd:
""" 

openssl req x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem

"""
Using this command-line invocation, you’ll have to answer a lot of questions: 
Country Name, State, City, and so on. 
The tricky question is “Common Name.” You’ll want to answer with the hostname 
or CNAME by which people will address the server. 
This is very important. If your web server’s real hostname is mybox.mydomain.com 
but people will be using www.mydomain.com to address the box, then use 
the latter name to answer the “Common Name” question.

Once you’re comfortable with the answers you provide to those questions, 
you can script the whole thing by adding the -subj option. I’ve included some 
information about location into the example that follows, but the only thing 
you really need to include for the certificate to be useful is the hostname (CN).

"""

openssl req -x509 -nodes -days 365 -subj '/C=US/ST=Oregon/L=Portland/CN=www.madboa.com'  -newkey rsa:1024 -keyout mycert.pem -out mycert.pem

"""
============================================================================
HOW DO I GENERATE A CERTIFICATE REQUEST FOR VERIFYSIGN ?
============================================================================
Applying for a certificate signed by a recognized certificate authority 
like VeriSign is a complex bureaucratic process. You’ve got to perform all 
the requisite paperwork before creating a certificate request.

As in the recipe for creating a self-signed certificate, you’ll have to decide whether 
or not you want a passphrase on your private key. The recipe below assumes you don’t. 
You’ll end up with two files: 
1. a new private key called mykey.pem 
2. and a certificate request called myreq.pem.
"""

openssl req -new -newkey rsa:1024 -nodes -keyout mykey.pem -out myreq.pem

"""
If you’ve already got a key and would like to use it for generating the request, the syntax is a bit simpler.
"""
openssl req -new -key mykey.pem -out myreq.pem

"""
Similarly, you can also provide subject information on the command line.
"""
openssl req \
  -new -newkey rsa:1024 -nodes \
  -subj '/CN=www.mydom.com/O=My Dom, Inc./C=US/ST=Oregon/L=Portland' \
  -keyout mykey.pem -out myreq.pem
  
"""
When dealing with an institution like VeriSign, you need to take special care to make sure that the information you provide during the creation of the certificate request is exactly correct. I know from personal experience that even a difference as trivial as substituting “and” for “&” in the Organization Name will stall the process.

If you’d like, you can double check the signature and information provided in the certificate request.
"""
# verify signature
openssl req -in myreq.pem -noout -verify -key mykey.pem

# check info
openssl req -in myreq.pem -noout -text

"""
Save the key file in a secure location. You’ll need it in order to use the 
certificate VeriSign sends you. The certificate request will typically be pasted 
into VeriSign’s online application form.
"""

"""
============================================================================
How do I test a new certificate?
============================================================================
The s_server option provides a simple but effective testing method. 
The example below assumes you’ve combined your key and certificate into one 
file called mycert.pem.

First, launch the test server on the machine on which the certificate will be used. 
By default, the server will listen on port 4433; you can alter that using the 
-accept option.

"""
openssl s_server -cert mycert.pem -www

"""
If the server launches without complaint, then chances are good that the certificate 
is ready for production use.

You can also point your web browser at the test server, e.g., 
https://yourserver:4433/. (BUKA DI LOCALHOST:4433) 
Don’t forget to specify the “https” protocol; plain-old “http” won’t work. 
You should see a page listing the various ciphers available and some statistics 
about your connection. Most modern browsers allow you to examine the certificate as well.
"""

"""
============================================================================
How do I retrieve a remote certificate?
============================================================================
If you combine openssl and sed, you can retrieve remote certificates via a shell 
one-liner or a simple script.
"""
#!/bin/sh
#
# usage: retrieve-cert.sh remote.host.name [port]
#
REMHOST=$1
REMPORT=${2:-443}

echo |\
openssl s_client -connect ${REMHOST}:${REMPORT} 2>&1 |\
sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p'

