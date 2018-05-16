"""
Sample Test of searching through the dictionary/list structure with a
key path.

Adapted from:
https://www.haykranen.nl/2016/02/13/handling-complex-nested-dicts-in-python/
"""
import pprint

d = [
    {"name": "cookies",
     "id": 0,
     "children": [

         {"name": "chocolate",
          "id": 1,
          "children": [

              {"name": "chunk",
               "id": 2,
               "children": [

               ]}  # end chunk
          ]}  # end chocolate
     ]},  # end cookies
    {"name": "cupcake",
     "id:": 3,
     "children": [

         {"name": "raspberry",
          "id": 4,
          "children": [

          ]}  # end raspberry
     ]}  # end cupcake
]


class Query:

    def __init__(self, data):
        self.data = data
        self.splitter = "/"

    def get(self, path, pointer=None, c=0):
        print "---- {} -----".format(c)
        if c == 10:
            print "C stop"
            return

        if pointer is None:
            pointer = self.data

        if path.count(self.splitter):
            key, _next = path.split(self.splitter, 1)
        else:
            key = path
            _next = None

        for item in pointer:
            name = item.get("name", None)
            if name and name == key:
                if _next:
                    return self.get(_next, item["children"], c+1)
                else:
                    print "Returning:", item
                    return item

        # print "Path", path
        # if path.count("/"):
        #     k, n = path.split("/", 1)
        #     print k
        #     if pointer is None:
        #         pointer = self.data
        #
        #     # print pprint.pprint(pointer)
        #
        #     for item in pointer:
        #         pprint.pprint(item)
        #         m = item.get("name", None)
        #         print m
        #         if m == k:
        #             print "Have Item", item
        #             if n:
        #                 print "continuing..."
        #                 return self.get(n, item["children"], c + 1)
        #
        # else:
        #     for item in pointer:
        #         name = item.get("name", None)
        #         print name
        #         if name == path:
        #             print "Have last item", item
        #             return item


Query(d).get("cupcake/raspberry")

