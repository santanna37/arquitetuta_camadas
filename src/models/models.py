"""_summary_ 
    Camada que tem as caracteristicas do banco de dados -  representam o negocio, elas reprensentam os atributos e relacionamentos entre os conceitos da area que esta sendo automatizada 
    """
from pydantic import BaseModel  
from typing import Optional, List

class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str 
    telefone: str
    meus_produtos: List[Produto]
    minhas_vendas: List[Pedido]
    meus_pedidos: List[Pedido]
    

class Produto(BaseModel):
    id: Optional[str] = None
    usuario:Usuario
    nome: str 
    detalhes: str 
    preco: float
    disponivel: bool = False

class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    