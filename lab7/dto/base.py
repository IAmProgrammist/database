from abc import ABC, abstractmethod
from typing import Type

from schemas.base import TunedModel


class BaseDTOGeneartor(ABC):
    @abstractmethod
    def translations(self) -> dict:
        """Возвращает переводы для полей DTO"""
        pass

    @abstractmethod
    def insert(self) -> Type[TunedModel] | None:
        """Возвращает базовую DTO для вставки"""
        pass

    @abstractmethod
    def select(self) -> Type[TunedModel] | None:
        """Возвращает базовую DTO для выборки данных"""
        pass

    @abstractmethod
    def update(self) -> Type[TunedModel] | None:
        """Возвращает базовую DTO для обновления данных"""
        pass

    @abstractmethod
    def identifier(self) -> Type[TunedModel] | None:
        """Возвращает совокупность полей, по которым можно идентифицировать объект"""
        pass
