Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Menyelesaikan Persamaan Kuadrat ax**2 + bx + c = 0

# Mengimpor Modul Cmath
import cmath

# Menginput Angka
a = int(input('Tulis a: '))
b = int(input('Tulis b: '))
c = int(input('Tulis c: '))

# Menghitung Diskriminan
d = (b**2) - (4*a*c)

# Menghitung x1 dan x2
x1 = (-b-cmath.sqrt(d))/(2*a)
x2 = (-b+cmath.sqrt(d))/(2*a)

#Menampilkan Hasil x1 dan x2
print('Hasil Persamaan Kuadrat adalah {0} dan {1}'.format(x1,x2))