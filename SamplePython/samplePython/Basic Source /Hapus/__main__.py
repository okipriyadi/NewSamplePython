import re
regex = re.compile(r"([a-z]*)(\d*)([a-z]*)", re.IGNORECASE)
kata = "test123hjh"
if regex.match(kata):
    print regex.match(kata).group(1)
#kata = regex.sub((r"\D*"),"", kata)
kata = regex.sub(r"\1", kata)
print kata
