import time

userid = str(input(" Hesap makinesine erişmek için kimliğini doğrulamamız gerek. Lütfen kullanıcı id ni gir : "))

if userid == "62442":
    print("ID doğrulandı... Hoşgeldin Serhat")
    time.sleep(1)
    print("Hesap makinesi başlatılıyor..")
    time.sleep(2)
    a = int(input("Bir sayı giriniz: "))
    b = int(input("Yeni bir sayı  giriniz: "))

    print(" / işaretiyle bölme \n * işaretiyle çarpma \n - işaretiyle çıkarma \n + işaretiyle toplama yapabilirsin.")
    time.sleep(2)
    islem = str(input("Yapmak istediğiniz işlemi seçin(/,*,-,+) : "))

    if islem == "/":
        print("Sonuç : ",a/b)

    elif islem == "*":
        print("Sonuç : ",a*b)

    elif islem == "-":
        print("Sonuç : ",a-b)

    elif islem == "+":
        print("Sonuç : ",a+b)

    else:
        print("Lütfen geçerli bir işlem yazınız.")

    print("Başka işlemlerde görüşmek üzere...")
    
else:
    print("Geçersiz ID...")
