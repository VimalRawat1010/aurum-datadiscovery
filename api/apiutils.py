from enum import Enum
import networkx as nx


class Edge(Enum):
    FIELD_OF = 0




class DRSMode(Enum):
    FIELDS = 0
    TABLE = 1


class Provenance:

    def __init__(self):
        self._pgraph = nx.MultiDiGraph()

    def add_node(self, a: str, relation: Edge):
        return


class DRS:

    def __init__(self, data):
        self._data = data
        self._table_view = []
        self._idx = 0
        self._idx_table = 0
        self._mode = DRSMode.FIELDS

    def __iter__(self):
        return self

    def __next__(self):
        # Iterating fields mode
        if self._mode == DRSMode.FIELDS:
            if self._idx < len(self._data):
                self._idx += 1
                return self._data[self._idx - 1]
            else:
                self._idx = 0
                raise StopIteration
        # Iterating in table mode
        elif self._mode == DRSMode.TABLE:
            #  Lazy initialization of table view
            if len(self._table_view) == 0:
                table_set = set()
                for h in self._data:
                    t = h.source_name
                    table_set.add(t)
                self._table_view = list(table_set)
            if self._idx_table < len(self._table_view):
                self._idx_table += 1
                return self._table_view[self._idx_table - 1]
            else:
                self._idx_table = 0
                raise StopIteration

    @property
    def data(self):
        return self._data

    @property
    def mode(self):
        return self._mode

    def size(self):
        return len(self.data)

    def absorb_provenance(self, drs):
        """
        Merge provenance of the input parameter into self, *not* the data.
        :param drs:
        :return:
        """
        return

    def extend_provenance(self, drs):
        """
        Check which elements of self are present in drs, and add provenance information from drs to self
        :param drs:
        :return:
        """
        return

    def absorb(self, drs):
        """
        Merge the input parameter DRS into self, by extending provenance appropriately and appending data
        :param drs:
        :return:
        """
        return

    def set_fields_mode(self):
        self._mode = DRSMode.FIELDS

    def set_table_mode(self):
        self._mode = DRSMode.TABLE

    def paths(self):
        return

    def path(self, a: str):
        return

    def why(self, a: str):
        return

    def how(self, a: str):
        return


if __name__ == "__main__":

    test = DRS([1, 2, 3])

    for el in test:
        print(str(el))

    print(test.mode)
    test.set_table_mode()
    print(test.mode)
