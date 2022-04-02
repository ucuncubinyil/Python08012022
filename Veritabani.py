import sqlite3


# vt = sqlite3.connect("C:\DovizTakip\PyPara.db")
# cursor = vt.cursor()
#
# # komut = """
# #     create table tb_altin(
# #         id INTEGER NOT NULL  UNIQUE ,
# #         zaman NVARCHAR(250) NOT NULL ,
# #         kur   REAL NOT NULL,
# #         PRIMARY  KEY(id AUTOINCREMENT)
# #     )
# # """
#
#
#
# # komut = """
# #     create table tb_dolar(
# #         id INTEGER NOT NULL  UNIQUE ,
# #         zaman NVARCHAR(250) NOT NULL ,
# #         kur   REAL NOT NULL,
# #         PRIMARY  KEY(id AUTOINCREMENT)
# #     )
# # """
#
# komut = """
#     create table tb_euro(
#         id INTEGER NOT NULL  UNIQUE ,
#         zaman NVARCHAR(250) NOT NULL ,
#         kur   REAL NOT NULL,
#         PRIMARY  KEY(id AUTOINCREMENT)
#     )
# """
#
# cursor.execute(komut)
# vt.close()

class Veritabani:

    @staticmethod
    def kaydet(komut):
        vt = sqlite3.connect("C:\DovizTakip\PyPara.db")
        try:
            cursor = vt.cursor()
            cursor.execute(komut)
            vt.commit()
            print("Kayıt Başarılı")
        except:
            print("Kayıt esnasında bir hata oluştu !")
        vt.close()

    @staticmethod
    def kurGetir(komut):
        vt = sqlite3.connect("C:\DovizTakip\PyPara.db")

        try:
            cursor = vt.cursor()
            cursor.execute(komut)
            listeKur = cursor.fetchall()
            listeKur.reverse()
        except:
            print("Kurlar çekilirken bir  hata oluştu")
        return listeKur
        vt.close()
