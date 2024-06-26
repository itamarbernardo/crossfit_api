from crossfit_api.contrib.models import BaseModel
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

class AtletaModel(BaseModel):
    __tablename__ = 'atletas'

    #Temos essa pk_id que será o id incremental do banco, e o uuid herdado da classe basemodel que iremos expor ao usuário
    #esse pk_id a gente não expõe ao usuário
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    #lazy='selectin' é pra unir as tabelas das foreing keys e poder mostrar as informações
    categoria: Mapped['CategoriaModel'] = relationship(back_populates="atleta", lazy='selectin')
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.pk_id"))
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates="atleta", lazy='selectin')
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey("centros_treinamento.pk_id"))