system_subscriber = {"test":"asydh", "hakshd":"djais"}
system_subscriber.pop("test", None)
system_subscriber[1] = (2,3)
a , b = system_subscriber.pop(1, (None, None))
print system_subscriber
print a 
print b
