from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Personne(Base):
    __tablename__ = 'personne'
    id = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable=False)
    prenom = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)

    def __init__(self, pnom=None, pprenom=None, pemail=None):
        self.nom = pnom
        self.prenom = pprenom
        self.email = pemail

    def nom_str(self):
        nom = self.prenom + ' ' + self.nom
        return nom

    def __repr__(self):
       return '<Personne id={} nom={} prenom={} email={} nomprenom={}>'.format(self.id, self.nom, self.prenom, self.email, self.nom_str())

class Adresse(Base):
    __tablename__ = 'adresse'
    id = Column(Integer, primary_key=True)
    rue = Column(String(100), nullable=False)
    cp = Column(Integer, nullable=False)
    ville = Column(String(100), nullable=False)
    personne_id = Column(Integer, ForeignKey('personne.id'), nullable=False)
    type = Column(String(50), nullable=False)
#    type_id = Column(Integer, ForeignKey('type.id'), nullable=False)

    def __init__(self, arue=None, acp=None, aville=None, apersonne_id=None, atype=None):
        self.rue = arue
        self.cp = acp
        self.ville = aville
        self.personne_id = apersonne_id
        self.type = atype
#        self.type_id = atype_id

    def __repr__(self):
        return '<Adresse id={} rue={} cp={} ville={} personne={} type={}>'.format(self.id, self.rue, self.cp, self.ville, self.personne_id, self.type)

class Type(Base):
    __tablename__ = 'type'
    id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)

    def __init__(self, atype=None):
        self.type = atype

    def __repr__(self):
        return '<Type id={} type={}>'.format(self.id, self.type)