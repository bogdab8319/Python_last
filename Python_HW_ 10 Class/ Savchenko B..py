# # Заданиу № 1

# class Auto:
#     def __init__(self, manufacturer,  model, year, engine, color ,price):
#         self.__model = model
#         self.__year = year
#         self.__manufacturer = manufacturer
#         self.__engine = engine
#         self.__color = color
#         self.price = price
#
#     def set_model(self, modele ):
#         self.__modele= modele.capitalise()
#
#     def get_modele(self, modele):
#         return self.__modele
#
#     def set_year(self, year):
#             if str(year).isdigit() and int(year) > 0:
#                 self.__year = year
#
#     def get_year(self):
#         return self.__year
#
#     def set_manufacturer(self, manufacturer):
#         self.__manufacturer= manufacturer
#
#     def get_manufacturer(self,manufacturer):
#         return self.__manufacturer
#
#     def set_engine(self,engine):
#         self.__engine = engine
#
#     def get_engine(self,engine):
#         return self.__engine
#
#     def set_color(self,color):
#         self.__color = color
#
#     def get_color(self, color):
#         self.__color = color
#
#
#     def set_price(self,price):
#         self.price = price
#
#     def get_price(self,price):
#         return self.price
#
#
#     def show_Info_Auto (self ):
#         return f"Avto : {self.__manufacturer};  model is: {self.__model};   year is: {self.__year};   engin is:  {self.__engine}: " \
#                f" color: {self.__color};    price is:  {self.price} "
#
#     def show_Txt(self):
#         return f' Марка :{self.__manufacturer}  отличній производитель !!!_____{self.__model} лучший вібор ! '
#
#     def show_price(self):
#         return f"  Стоимость авто всего : {self.price}", "отличній вариант"
#
#
#
#
# car1= Auto( "BMW", "X 3","2022","2.0","red", "40000")
# car2 =Auto( "Audi","А 8",2022, 3.0, "white", 60000)
# car3 = Auto("VW","Passat",2022,2.0,"green",38000)
# print(car1.show_Info_Auto())
# print(car2.show_Info_Auto())
# print(car3.show_Info_Auto())
# print(car1.get_manufacturer(""))
# print(car2.show_Txt())
# print(car3.show_price())



#
# # Задание № 2
#
#
# class Book :
#     def __init__(self, namebook, year, pablisher, ganre, autor, price ):
#         self.__namebook = namebook
#         self.__year = year
#         self.__pablisher = pablisher
#         self.__ganre = ganre
#         self.__autor = autor
#         self.__price = price
#
#     def  set_namebook(self , namebook: str):
#         self.__namebook=namebook.capitalize()
#
#     def get_namebook(self,):
#         return self.__namebook
#
#     def set_year(self, year):
#         if str(year).isdigit() and int(year) > 0:
#             self.__year = year
#
#     def get_year(self):
#         return self.__year
#
#     def set_pablisher(self, pablisher: str):
#         self.__pablisher = pablisher.capitalize()
#
#     def get_pablisher(self):
#         return self.__pablisher
#
#     def set_ganre(self, ganre: str):
#         self.__ganre = ganre.capitalize() + "!!!!!!!!!!!!!!!!!!1"
#
#     def get_ganre(self):
#         return self.__ganre
#
#     def set_autor(self, autor: str):
#         self.__autor = autor.capitalize()
#
#     def get_autor(self):
#         return self.__autor
#
#     def set_price(self, price: str):
#         self.__price = price.capitalize()
#
#     def get_price(self):
#         return self.__price
#
#     def get_info(self):
#         return f'"Название книги 5": {self.get_namebook}, "год випуска": {self.get_year}  , "Издатель":{self.get_pablisher},\n "ЖанрЖ": {self.get_ganre}, "АвторЖ": {self.get_autor}, "Цена": {self.get_price}'
#
#     def set_info(self):
#         return {f"Название книги": self.set_namebook, "год випуска": self.set_year, "Издатель": self.set_pablisher,
#                 "ЖанрЖ": self.set_ganre, "АвторЖ": self.set_autor, "Цена": self.set_price}
#
#
#
#     def res_Set_Data(self):
#         return f" Ві ввели название книги: {self.__namebook}, Год віпуска{self.__year} \n" f"Издатель : {self.__pablisher}, Жанр книги : {self.__pablisher}\n " f"Автор : {self.__autor}, Цена: {self.__price}  "
#
#     def res_Get_Data(self):
#         return f" Ві ввели название книги: {self.__namebook}, Год віпуска{self.__year} \n" f"Издатель : {self.__pablisher}, Жанр книги : {self.__pablisher}\n " f"Автор : {self.__autor}, Цена: {self.__price}  "
#
#
# book3= Book( "Кобзар","1840 год","Киев"," Поєма","Шевченко","500 грн.")
# book4= Book("Кобзар2","1839 год","Киев-Харьков"," Поєма- Стих","Шевченко","1500 грн.")
#
# print(book3.res_Set_Data())
# print(book4.res_Get_Data())


# Задание № 3



class Stadium:

    def __init__ (self, name_stadium, data,country, city, capacity ):
        self.__name_stadium = name_stadium
        self.__data = data
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def set_name_stad(self,name_stadium):
        self.__name_stadium = name_stadium.capitalize()
    def set_data(self,data):
        if str(data).isdigit() and int(data) > 0:
            self.__data = data.capitalize()

    def set_country(self, country):
        self.__country = country
    def set_city(self,  city):
        self.__city = city
    def set_capacity(self, capacity):
        self.__capacity = capacity


    def get_name_stad(self,name_stadium):
        return name_stadium
    def get_data(self, data):
        return data
    def get_country(self,country):
        return country
    def get_city(self,city):
        return city
    def get_capacity(self,capacity):
        return capacity


    def show_Info_Stadiums(self):
        return f" Стадион : {self.__name_stadium} .Дата мероприятия: {self.__data} . Страна проведения :  { self.__country }. Город :  {self.__city} . Вместительность стадиона : {self.__capacity} .  "

    def show_Info_Stadium(self):
        return f' Стадион__  {self.__name_stadium}  расположен в лучшей части города {self.__city}a '


obj_1 = Stadium("Металист","28.08.2022","Украина","Харьков","40 000 мест")
print(obj_1.show_Info_Stadiums())
print(obj_1.show_Info_Stadium())
obj_2 = Stadium("Сан-Сі́ро","1.09.2022","Италия","Милан"," 80 018 мест")
print(obj_2.show_Info_Stadiums())
print(obj_2.show_Info_Stadium())