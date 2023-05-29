from functools import lru_cache

students = [{"first_name": "str",
         "last_name": "str"
         }]

marks = [{"id": "int",
         "mark": "float"
         }]


@lru_cache()
def get_students_list():
    return students