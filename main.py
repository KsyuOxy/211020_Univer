from models import FacultyModel, GroupModel

if __name__ == '__main__':

    faculty_model = FacultyModel()
    facs = faculty_model.get_all_faculties()
    print(facs)

    g = GroupModel()
    grs = g.get_all_groups()
    print(grs)

    # new_fac = 'Рисование карандашами'
    # faculty_model.add_faculty(new_fac)
    # print(facs)

    # facs_del = faculty_model.delete_faculty('Рисование карандашами')
    # print(facs)

    # new_gr = 'Test_group'
    # g.add_group(new_gr, 'Рисование карандашами')
    # print(gr)

    gr_del = g.delete_group('Group_02_dgn', 'Design_09')
    print(grs)
