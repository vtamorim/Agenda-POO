from abc import abstractmethod, ABC


class DAO(ABC):
    _objetos = []

    @classmethod
    def inserir(cls, obj):
        """
        Insere uma instância em memória e atribui um id numérico incremental.
        Compatível com objetos que implementam get_id()/set_id() ou atributo 'id'.
        """
        cls.abrir()

    
        max_id = 0
        for aux in cls._objetos:
            aux_id = None
            if hasattr(aux, "get_id"):
                try:
                    aux_id = int(aux.get_id())
                except Exception:
                    aux_id = None
            if aux_id is None:
                try:
                    aux_id = int(getattr(aux, "id", 0) or 0)
                except Exception:
                    aux_id = 0
            if aux_id > max_id:
                max_id = aux_id

        next_id = max_id + 1

       
        if hasattr(obj, "set_id"):
            try:
                obj.set_id(next_id)
            except Exception:
                setattr(obj, "id", next_id)
        else:
            try:
                setattr(obj, "id", next_id)
            except Exception:
                pass

        cls._objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls._objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls._objetos:
            try:
                if hasattr(obj, "get_id") and obj.get_id() == id:
                    return obj
                if getattr(obj, "id", None) == id:
                    return obj
            except Exception:
                continue
        return None

    @classmethod
    def excluir(cls, obj):

        cls.abrir()
        target = None
        if isinstance(obj, (int, str)):
            target = cls.listar_id(obj)
        else:
            try:
                obj_id = obj.get_id() if hasattr(obj, "get_id") else getattr(obj, "id", None)
            except Exception:
                obj_id = getattr(obj, "id", None)
            target = cls.listar_id(obj_id)

        if target is not None:
            cls._objetos.remove(target)
            cls.salvar()

    @classmethod
    @abstractmethod
    def abrir(cls):
        pass

    @classmethod
    @abstractmethod
    def salvar(cls):
        pass
    @classmethod
    def atualizar(cls, obj):
        """
        Atualiza um objeto existente (mesmo ID) na lista e salva.
        Compatível com objetos com get_id()/set_id() ou atributo 'id'.
        """
        cls.abrir()
        id_alvo = None

        
        if hasattr(obj, "get_id"):
            id_alvo = obj.get_id()
        else:
            id_alvo = getattr(obj, "id", None)

        if id_alvo is None:
            raise ValueError("Objeto sem ID definido; não é possível atualizar.")

     
        for i, existente in enumerate(cls._objetos):
            existente_id = None
            if hasattr(existente, "get_id"):
                existente_id = existente.get_id()
            else:
                existente_id = getattr(existente, "id", None)

            if existente_id == id_alvo:
                cls._objetos[i] = obj  # substitui
                cls.salvar()
                return

        raise ValueError(f"Objeto com id {id_alvo} não encontrado para atualização.")