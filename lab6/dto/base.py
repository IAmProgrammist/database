from abc import ABC, abstractmethod

class BaseDTOGeneartor(ABC):
    @abstractmethod
    def translations(self) -> dict:
        """Возвращает переводы для полей DTO"""
        pass

    @abstractmethod
    def insert(self) -> dict:
        """Возвращает базовую DTO для вставки"""
        pass

    @abstractmethod
    def select(self) -> list[str]:
        """Возвращает базовую DTO для выборки данных"""
        pass

    @abstractmethod
    def update(self) -> dict:
        """Возвращает базовую DTO для обновления данных"""
        pass

    @abstractmethod
    def identifier(self) -> dict:
        """Возвращает совокупность полей, по которым можно идентифицировать объект"""
        pass