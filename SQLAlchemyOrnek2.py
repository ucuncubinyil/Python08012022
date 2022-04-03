from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.sql import select

motor = create_engine("sqlite:///sqlornek2.db", echo=True)
meta = MetaData()

calisanlar = Table(
    "calisanlar", meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("adi", String),
    Column("soyadi", String)
)

adresler = Table(
    "adresler", meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("c_id", Integer, ForeignKey("calisanlar.id")),
    Column("il_adi", String),
    Column("ilce_adi", String),
    Column("acik_adres", String)
)

meta.create_all(motor)

baglanti = motor.connect()

#
# calisan1 = calisanlar.insert().values(adi="Mehmet Nuri", soyadi="Öztürk")
# baglanti.execute(calisan1)

# adres1 =  adresler.insert().values(c_id =1,il_adi="İstanbul", ilce_adi="Ataşehir", acik_adres="Kayışdağı Mah.")
# baglanti.execute(adres1)

# calisan1 = select([calisanlar, adresler]).where(calisanlar.c.id == adresler.c.c_id)
# cikti = baglanti.execute(calisan1)
# for i in cikti:
#     print(i)


# calisanA = calisanlar.select().where(calisanlar.adi.startswith('A%'))
# cikti = baglanti.execute(calisanA)
# print(cikti)

print(calisanlar.join(adresler))
#  CALISANLAR  JOIN ADRESLER ON CALISANLAR.ID = ADRESLER.C_ID

j = calisanlar.join(adresler, calisanlar.c.id == adresler.c.c_id)

sec = select([calisanlar]).select_from(j)
cikti = baglanti.execute(sec).fetchone()
print(cikti)