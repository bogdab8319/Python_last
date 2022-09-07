



class Book :
    def __init__(self, name, year, pablisher, ganre, autor, price ):
        self.__name = name
        self.__year = year
        self.__pablisher = pablisher
        self.__ganre = ganre
        self.__autor = autor
        self.__price = price

    def set_name(self, name: str):
        self.__name=name.capitalize()

    def get_name(self,):
        return self.__name

    def set_year(self, year):
        if str(year).isdigit() and int(year) > 0:
            self.__year = year

    def get_year(self):
        return self.__year

    def set_pablisher(self, pablisher: str):
        self.__pablisher = pablisher.capitalize()

    def get_pablisher(self):
        return self.__pablisher

    def set_ganre(self, ganre: str):
        self.__ganre = ganre.capitalize() + "!!!!!!!!!!!!!!!!!!1"

    def get_ganre(self):
        return self.__ganre

    def set_autor(self, autor: str):
        self.__autor = autor.capitalize()

    def get_autor(self):
        return self.__autor

    def set_price(self, price: str):
        self.__price = price.capitalize()

    def get_price(self):
        return self.__price

    def __str__(self):
        return f" Ві ввели название книги: {self.__name}, Год віпуска:  {self.__year} \n" f"Издатель : {self.__pablisher}, Жанр книги : {self.__ganre} " f"Автор : {self.__autor}, Цена: {self.__price}"



    def show_Info_Book(self):
        return f" Ві ввели название книги: {self.__name}, Год віпуска:  {self.__year} \n" f"Издатель : {self.__pablisher}, Жанр книги : {self.__ganre} " f"Автор : {self.__autor}, Цена: {self.__price}  "



book3= Book( "Кобзар","1840 год","Киев"," Поєма","Шевченко","500 грн.")
book4= Book("Кобзар2","1839 год","Киев-Харьков"," Поєма- Стих","Шевченко","1500 грн.")

print(book3.show_Info_Book())
print("Новій вариант--",book4.show_Info_Book())

class Magazine(Book):
    def __init__(self, name, year, pablisher, ganre, autor, price,spec):
        self.spec= spec
        super().__init__(name, year, pablisher, ganre, autor, price)

    def __str__(self):
        self.__name=" "
        self.spec=" 92 - 93"

        return f" {super().__str__()}, Сезон : {self.spec}"
    def invest(self):
        self.spec="2022 "
        return f" {super().__str__()}, Сезон : {self.spec}"
print(" Класс Книга")
print("Класс Журнал")



magaz1= Magazine("Basket Tribute"," 1992" , "Колман i Ко", "sport"," Stolman", "10 Doll USA", "Сезон : 92 - 93")
magaz2 = Magazine("Инвестиционніе Фонді","27.06.2022","Alekont Groop","Финансі","Бертуолис","220 euro", "2022)")
print(magaz1.__str__())
print(magaz2.invest())


class Newspaper(Book):

    def __init__(self, name, year, pablisher, ganre, autor, price,spec):
        self.spec= spec
        super().__init__(name, year, pablisher, ganre, autor, price)

    def __str__(self):
        self.spec=" Смерть Москалям !!!"
        return f" {super().__str__()}, Сезон : {self.spec}"

    def gazeta_KH(self):
        self.spec= "- Утрений віпуск !"
        return f" {super().__str__()}, Сезон : {self.spec}!"

print("Класс газета")
paper1= Newspaper("Український вечір ","1.09.2022", "Долбня ", " Реалії", "Рука Народа","20 грн. ","Смерть Москалям !!!")
print(paper1.__str__())
paper2= Newspaper("- Харьковский ветер","- 1.09.2022","-  Карлуша С.А","-  Новостной","- Рімарская","- 29.90 грн","- Утрений віпуск")
print(paper2.gazeta_KH())