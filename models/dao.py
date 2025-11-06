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

        # calcula próximo id baseado no maior id já presente
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

        # atribui id ao objeto (preferindo set_id se disponível)
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
        # aceita tanto a instância quanto um id (int/str)
        cls.abrir()
        target = None
        if isinstance(obj, (int, str)):
            target = cls.listar_id(obj)
        else:
            # tenta obter id da instância fornecida
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