from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker
 
class Bookmarks(object):
    pass
 
#----------------------------------------------------------------------
def loadSession():
    engine = create_engine('mysql+pymysql://root:Amber252556!@@localhost/imdb_final')
 
    metadata = MetaData(engine)
    moz_bookmarks = Table('imdb_final', metadata, autoload=True)
    mapper(Bookmarks, moz_bookmarks)
 
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
 
if __name__ == "__main__":
    session = loadSession()
    res = session.query(Bookmarks).all()
    res[1].title
