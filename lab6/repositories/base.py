from tabulate import tabulate
from typing import Any

from lab6.dto.base import BaseDTOGeneartor


class Repository:
    def __init__(self, connection, table, generator: BaseDTOGeneartor):
        self._table = table
        self.generator = generator
        self.connection = connection

    def get_dto_generator(self):
        return self.generator

    @classmethod
    def _get_where_identifier(cls, value: tuple[str, Any]) -> str:
        result = f"{value[0]}"
        if type(value[1]) is None:
            result += " IS NULL"
        elif type(value[1]) in (int, float):
            result += f"={value[1]}"
        else:
            result += f"='{value[1]}'"

        return result

    @classmethod
    def _get_set_identifier(cls, value: tuple[str, Any]) -> str:
        result = f"{value[0]}="
        if type(value[1]) is None:
            result += "NULL"
        elif type(value[1]) in (int, float):
            result += f"{value[1]}"
        else:
            result += f"'{value[1]}'"

        return result

    def select(self, keys: list[str]) -> list[dict]:
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT {','.join(keys)} FROM {self._table};")

                result = []

                for row in cursor.fetchall():
                    i = 0
                    new_element = dict()
                    for key in keys:
                        new_element[key] = row[i]
                        i += 1

                    result.append(new_element)
                self.connection.commit()
                return result
            except Exception as e:
                self.connection.rollback()
                raise e

    def insert(self, data: dict) -> None:
        with self.connection.cursor() as cursor:
            try:
                values = map(lambda x: 'NULL' if x is None else f"'{x}'", data.values())
                cursor.execute(f"INSERT INTO {self._table} "
                                     f" ({', '.join(data.keys())})"
                                     f" VALUES ({', '.join(values)});")
                self.connection.commit()
            except Exception as e:
                self.connection.rollback()
                raise e

    def update(self, data: dict, identifier: dict) -> None:
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(f"UPDATE {self._table} "
                                     f"SET {', '.join(map(Repository._get_set_identifier, data.items()))}"
                                     f"WHERE {' AND '.join(map(Repository._get_where_identifier, identifier.items()))};")
                self.connection.commit()
            except Exception as e:
                self.connection.rollback()
                raise e

    def delete(self, identifier: dict) -> None:
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(f"DELETE FROM {self._table} "
                               f"WHERE {' AND '.join(map(Repository._get_where_identifier, identifier.items()))};")
                self.connection.commit()
            except Exception as e:
                self.connection.rollback()
                raise e
