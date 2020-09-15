print('--- Kalkulator ---')
print('Pilih Menu\n 1 : + \n 2 : - \n 3 : * \n 4 : /')
class Calculator:
    @staticmethod
    def sum(a, b):
        return a + b
    def multi(a, b):
        return a * b
    def divide(a, b):
        return a - b
    def less(a, b):
        return a - b

pil = input('Pilih 1 - 4 : ')
a = input('Masukkan Angka Pertama : ')
b = input('Masukkan Angka Kedua : ')

if int(pil) == 1:
    print('Total dari '+ a +' + '+ b +' Adalah : ', Calculator.sum(int(a),int(b)))
elif int(pil) == 2:
    print('Total dari '+ a +' - '+ b +' Adalah : ', Calculator.less(int(a),int(b)))
elif int(pil) == 3:
    print('Total dari '+ a +' x '+ b +' Adalah : ', Calculator.multi(int(a),int(b)))
elif int(pil) == 4:
    print('Total dari '+ a +' / '+ b +' Adalah : ', Calculator.divide(int(a),int(b)))
else:
    print('Pilihan yang anda masukkan Salah!')
