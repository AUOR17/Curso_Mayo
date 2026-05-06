from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, select
from sqlalchemy.orm import declarative_base, relationship, Session

engine = create_engine("sqlite:///db_alchemy.db", echo=False)
Base = declarative_base()

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    industria = Column(String)

    leads = relationship("Lead", back_populates="empresa")

class Lead(Base):
    __tablename__ = 'leads'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    presupuesto = Column(Float)

    empresa_id = Column(Integer, ForeignKey("empresas.id"))

    empresa = relationship("Empresa", back_populates="leads")

Base.metadata.create_all(engine)

with Session(engine) as session:

    # empresa_tech = Empresa(nombre="TechCorp", industria="Software")
    # empresa_pyme = Empresa(nombre="PYMESQL", industria="Consultoria")

    # lead_1 = Lead(nombre="Ana", presupuesto=1000, empresa= empresa_tech)
    # lead_2 = Lead(nombre="Brian", presupuesto=2000, empresa= empresa_tech)
    # lead_3 = Lead(nombre="Belinda", presupuesto=10000, empresa= empresa_pyme)

    # session.add_all([empresa_tech, empresa_pyme, lead_1, lead_2, lead_3])
    # session.commit()

    query = select(Lead).where(Lead.presupuesto > 1200)
    # print(query)
    # resultados = session.execute(query).all()
    resultados = session.scalars(query).all()
    # print(resultados)

    for l in resultados: 
        print(f"{l.nombre} - ${l.presupuesto}")

    query_name = select(Lead).where(Lead.nombre == "Belinda")
    belinda = session.scalars(query_name).first()

    if belinda:
        belinda.presupuesto = 140000.0
        # session.commit()

    query_join = select(Lead.nombre, Empresa.nombre).join(Empresa)
    resultados = session.execute(query_join).all()

    for nombre_lead, nombre_empresa in resultados:
        print(f"{nombre_lead} trabaja en {nombre_empresa}")
    


