from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Genre, Artist

engine = create_engine('sqlite:///music.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


genre1 = Genre(name="Alternative Music")

session.add(genre1)
session.commit()

genre1 = Genre(name="Blues")

session.add(genre1)
session.commit()

genre1 = Genre(name="Classical Music")

session.add(genre1)
session.commit()

genre1 = Genre(name="Country Music")

session.add(genre1)
session.commit()

genre1 = Genre(name="Dance Music")

session.add(genre1)
session.commit()

genre1 = Genre(name="Easy Listening")

session.add(genre1)
session.commit()

genre1 = Genre(name="Electronic Music")

session.add(genre1)
session.commit()

artist1 = Artist(name="Daft Punk", description="""
        Daft Punk is a French electronic music duo consisting of producers
        Guy-Manuel de Homem-Christo and Thomas Bangalter.
    """, genre=genre1)

session.add(artist1)
session.commit()


artist2 = Artist(name="Deadmau5", description="""
        Joel Thomas Zimmerman (a.k.a. deadmau5) is a Canadian DJ producer, formerly
        a web developer, who produces a wide variety of electronic musical genres,
        such as electro and dubstep, but is best known for pioneering work in the
        areas of progressive house and electrohouse.
    """, genre=genre1)

session.add(artist2)
session.commit()

artist3 = Artist(name="Aphex Twin", description="""
        Richard David James (born 18 August 1971), known by his stage name Aphex
        Twin, is an Irish-born English electronic musician and composer.
    """, genre=genre1)

session.add(artist3)
session.commit()

artist4 = Artist(name="Zedd", description="""
        Zedd is a Russian- German DJ known for his hits such as Clarity, Transmission,
        and Break Free. He is best known for his album True Colors, which has the
        highest debut on the Billboard 200 for an EDM album (tied with Skrillex's
        Recess). He is one the the richest EDM artists in the industry.
    """, genre=genre1)

session.add(artist4)
session.commit()

genre1 = Genre(name="Indie Pop")

session.add(genre1)
session.commit()

genre1 = Genre(name="Hip Hop / Rap")

session.add(genre1)
session.commit()

genre1 = Genre(name="Indie Pop")

session.add(genre1)
session.commit()

genre1 = Genre(name="Jazz")

session.add(genre1)
session.commit()

genre1 = Genre(name="New Age")

session.add(genre1)
session.commit()

genre1 = Genre(name="Pop (Popular music)")

session.add(genre1)
session.commit()

genre1 = Genre(name="R&B / Soul")

session.add(genre1)
session.commit()

genre1 = Genre(name="Rock")

session.add(genre1)
session.commit()

genre1 = Genre(name="World Music / Beats")

session.add(genre1)
session.commit()

print "Added genre"
