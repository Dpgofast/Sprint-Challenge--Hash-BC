from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for x in range(length):
        if tickets[x].source == "NONE":
            route[0] = tickets[x].destination
        hash_table_insert(hashtable, tickets[x].source, tickets[x].destination)

    for y in range(length):
        if route[y-1] is not None:
            route[y] = hash_table_retrieve(hashtable, route[y-1])

    return route
