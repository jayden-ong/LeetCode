class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imaginary1 = num1.split("+")
        real2, imaginary2 = num2.split("+")

        real1_num = int(real1)
        real2_num = int(real2)
        imaginary1_num = int(imaginary1[:-1])
        imaginary2_num = int(imaginary2[:-1])

        real = real1_num * real2_num
        if (imaginary1_num > 0 and imaginary2_num > 0) or (imaginary1_num < 0 and imaginary2_num < 0):
            real -= imaginary1_num * imaginary2_num
        else:
            real += abs(imaginary1_num * imaginary2_num)
        real = str(real)

        imaginary = real1_num * imaginary2_num + real2_num * imaginary1_num
        
        return real + "+" + str(imaginary) + "i"