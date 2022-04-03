from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

from sqlalchemy.sql import text

# dialect[+driver]://user:password@host/dbname
engine = create_engine("sqlite:///demo.db", echo=True)

meta = MetaData()

ogrenciler = Table(
    "ogrenciler", meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('adi', String),
    Column('soyadi', String)
)

meta.create_all(engine)
baglanti = engine.connect()
# def ogrenciEkle(engine, ad, soyad):
#     baglanti = engine.connect()
#     ins = ogrenciler.insert().values(adi=ad, soyadi=soyad)
#     cikti = baglanti.execute(ins)
#
#
# ogrenciEkle(engine, "Veli", "Keman")

# Birden fazla kayıt ekleme
# baglanti.execute(ogrenciler.insert(),[
#     {"adi": "Burak", "soyadi": "Şahin"},
#     {"adi": "Berat", "soyadi": "Ural"}
# ])


# Seçme işlemi
# s = ogrenciler.select()
# cikti =  baglanti.execute(s)
#
# cikti = list(cikti)
# print(cikti)

# Querty yazma
# s = text("select ogrenciler.adi, ogrenciler.soyadi from ogrenciler where id = :id ")
# n = baglanti.execute(s, id=3).fetchall()
# print(n)

# aralik =  text("SELECT ogrenciler.id, ogrenciler.adi, ogrenciler.soyadi FROM ogrenciler Where ogrenciler.adi BETWEEN  :x AND :y")
# aa = baglanti.execute(aralik, x='mehmet', y='mehmet').fetchall()
# print(aa)

# # Update
# guncellenecek = ogrenciler.update().where(ogrenciler.c.id == 3).values(adi='Can')
# baglanti.execute(guncellenecek)
#
#
# #delete
#
# silinecek =  ogrenciler.delete().where(ogrenciler.c.id ==3)
# baglanti.execute(silinecek)

# Toplu Silme

topluSil = ogrenciler.delete().where(ogrenciler.c.id > 3)
baglanti.execute(topluSil)
