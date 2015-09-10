"""
kesimpulan saya sementara, adalah
dekorator berfungsi memasukan fungsi dibawah @dekorator kedalam fungsi lainnya yang telah ditetapkan
"""

from _02_a_penggunaan_dekorator import my_decorator

@my_decorator
def just_some_function():
  print "Wheee!"

just_some_function()

"""
So, @my_decorator is just an easier way of saying just_some_function = my_decorator
(just_some_function).
"""