from drivers import DbDriver


class FacultyModel(DbDriver):
    def __init__(self):
        super().__init__()

    def get_all_faculties(self) -> list:
        query = 'SELECT * FROM Faculties'
        params = tuple()
        faculties = self.execute_select(query, params)
        return faculties

    def add_faculty(self, faculty_name: str) -> None:
        query = 'INSERT INTO Faculties (name) VALUES (?)'
        params = (faculty_name, )
        self.execute_dml(query, params)

    def delete_faculty(self, faculty_name: str):  # -> удаляет факультет
        fac_mod = FacultyModel()
        for f in fac_mod.get_all_faculties():  # -> итерируется по факультетам
            if faculty_name in f:  # -> если имя факультета найдено - удаляет факультет
                query = 'DELETE FROM Faculties WHERE name=(?)'
                params = (faculty_name,)
                self.execute_dml(query, params)
            else:
                print('Нет такого факультета')


class GroupModel(DbDriver):
    def __init__(self):
        super().__init__()

    def get_all_groups(self) -> list:  # -> получает список групп
        query = 'SELECT * FROM Groups'
        params = tuple()
        groups = self.execute_select(query, params)
        return groups

    def add_group(self, group_name: str, faculty_name: str) -> None:  # -> добавляет группу в нужный факультет
        faculties = FacultyModel()
        for f in faculties.get_all_faculties():  # -> итерация по факультетам
            if faculty_name in f:  # -> если найдено совпадение названия факультета, добавляет группу
                query = 'INSERT INTO Groups (name, faculty_id) VALUES (?, ?)'
                params = (group_name, f[0])  # -> f[0] - id факультета
                self.execute_dml(query, params)
        else:
            print('Нет такого факультета')

    def delete_group(self, group_name: str, faculty_name: str):  # -> удаляет группу из заданного факультета
        faculties = FacultyModel()
        for f in faculties.get_all_faculties():  # -> итерируется по факультетам
            if faculty_name in f:  # -> если совпадение по названию найдено
                gr_mod = GroupModel()
                for g in gr_mod.get_all_groups():  # -> итерируется по группам
                    if group_name in g:  # -> если совпадение найдено, удаляет группу с заданными назв. и факультетом
                        query = 'DELETE FROM Groups WHERE name=(?) and faculty_id=(?)'
                        params = (group_name, g[2])  # -> g[2] - id факультета группы
                        self.execute_dml(query, params)
                else:
                    print('Нет такой группы')
                    break
        else:
            print('Нет такого факультета')
