# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, real_part: float, imaginary_part: float):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __str__(self):
        sign = '+' if self.imaginary_part >= 0 else '-'
        return f'{self.real_part} {sign} {abs(self.imaginary_part) if abs(self.imaginary_part) != 1 else ""}i'

    def __add__(self, other):
        return ComplexNumber(self.real_part + other.real_part, self.imaginary_part + other.imaginary_part)

    def __mul__(self, other):
        real_part = self.real_part * other.real_part - self.imaginary_part * other.imaginary_part
        imaginary_part = self.real_part * other.imaginary_part + other.real_part * self.imaginary_part
        return ComplexNumber(real_part, imaginary_part)


complex_number_1 = ComplexNumber(2, -1)
complex_number_2 = ComplexNumber(1, 3)
print(complex_number_1 + complex_number_2)
print(complex_number_1 * complex_number_2)
