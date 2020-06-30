from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = 'restapi'

    def ready(self):
        Student = self.get_model('Student')
        Student.objects.all().delete()
        user1 = Student(name="student_1", email="student_1@gmail.com", password="student_1@123")
        user1.save()
        user2 = Student(name="student_2", email="student_2@gmail.com", password="student_2@123")
        user2.save()
        user3 = Student(name="student_3", email="student_3@gmail.com", password="student_3@123")
        user3.save()
        user4 = Student(name="student_4", email="student_4@gmail.com", password="student_4@123")
        user4.save()
        user5 = Student(name="student_5", email="student_5@gmail.com", password="student_5@123")
        user5.save()
        user6 = Student(name="student_6", email="student_6@gmail.com", password="student_6@123")
        user6.save()
        user7 = Student(name="student_7", email="student_7@gmail.com", password="student_7@123")
        user7.save()
        user8 = Student(name="student_8", email="student_8@gmail.com", password="student_8@123")
        user8.save()
        user9 = Student(name="student_9", email="student_9@gmail.com", password="student_9@123")
        user9.save()
        user10 = Student(name="student_10", email="student_10@gmail.com", password="student_10@123")
        user10.save()
        user11 = Student(name="student_11", email="student_11@gmail.com", password="student_11@123")
        user11.save()
        user12 = Student(name="student_12", email="student_12@gmail.com", password="student_12@123")
        user12.save()
        user13 = Student(name="student_13", email="student_13@gmail.com", password="student_13@123")
        user13.save()
        user14 = Student(name="student_14", email="student_14@gmail.com", password="student_14@123")
        user14.save()
        user15 = Student(name="student_15", email="student_15@gmail.com", password="student_15@123")
        user15.save()
        user16 = Student(name="student_16", email="student_16@gmail.com", password="student_16@123")
        user16.save()
        user17 = Student(name="student_17", email="student_17@gmail.com", password="student_17@123")
        user17.save()
        user18 = Student(name="student_18", email="student_18@gmail.com", password="student_18@123")
        user18.save()
        user19 = Student(name="student_19", email="student_19@gmail.com", password="student_19@123")
        user19.save()
        user20 = Student(name="student_20", email="student_20@gmail.com", password="student_20@123")
        user20.save()

        Subject = self.get_model('Subject')
        Subject.objects.all().delete()

        sub1 = Subject(name='subject_1')
        sub1.save()
        sub2 = Subject(name='subject_2')
        sub2.save()
        sub3 = Subject(name='subject_3')
        sub3.save()
        sub4 = Subject(name='subject_4')
        sub4.save()
        sub5 = Subject(name='subject_5')
        sub5.save()

        Student_subject_mapping = self.get_model('Student_subject_mapping')
        Student_subject_mapping.objects.all().delete()

        stu_sub_map1 = Student_subject_mapping(student=user1, subject=sub1)
        stu_sub_map1.save()

        stu_sub_map2 = Student_subject_mapping(student=user1, subject=sub2)
        stu_sub_map2.save()

        stu_sub_map3 = Student_subject_mapping(student=user1, subject=sub3)
        stu_sub_map3.save()

        stu_sub_map4 = Student_subject_mapping(student=user1, subject=sub4)
        stu_sub_map4.save()

        stu_sub_map5 = Student_subject_mapping(student=user1, subject=sub5)
        stu_sub_map5.save()

        stu_sub_map6 = Student_subject_mapping(student=user2, subject=sub2)
        stu_sub_map6.save()

        stu_sub_map7 = Student_subject_mapping(student=user2, subject=sub4)
        stu_sub_map7.save()

        stu_sub_map8 = Student_subject_mapping(student=user2, subject=sub5)
        stu_sub_map8.save()

        stu_sub_map9 = Student_subject_mapping(student=user3, subject=sub2)
        stu_sub_map9.save()

        stu_sub_map10 = Student_subject_mapping(student=user3, subject=sub3)
        stu_sub_map10.save()

        stu_sub_map11 = Student_subject_mapping(student=user3, subject=sub4)
        stu_sub_map11.save()

        stu_sub_map12 = Student_subject_mapping(student=user3, subject=sub5)
        stu_sub_map12.save()

        stu_sub_map13 = Student_subject_mapping(student=user4, subject=sub1)
        stu_sub_map13.save()

        stu_sub_map14 = Student_subject_mapping(student=user4, subject=sub2)
        stu_sub_map14.save()

        stu_sub_map15 = Student_subject_mapping(student=user5, subject=sub1)
        stu_sub_map15.save()

        stu_sub_map16 = Student_subject_mapping(student=user5, subject=sub3)
        stu_sub_map16.save()

        stu_sub_map17 = Student_subject_mapping(student=user6, subject=sub4)
        stu_sub_map17.save()

        stu_sub_map18 = Student_subject_mapping(student=user6, subject=sub5)
        stu_sub_map18.save()

        stu_sub_map19 = Student_subject_mapping(student=user7, subject=sub1)
        stu_sub_map19.save()

        stu_sub_map20 = Student_subject_mapping(student=user7, subject=sub3)
        stu_sub_map20.save()

        stu_sub_map21 = Student_subject_mapping(student=user8, subject=sub2)
        stu_sub_map21.save()

        stu_sub_map22 = Student_subject_mapping(student=user8, subject=sub4)
        stu_sub_map22.save()

        stu_sub_map23 = Student_subject_mapping(student=user9, subject=sub3)
        stu_sub_map23.save()

        stu_sub_map24 = Student_subject_mapping(student=user9, subject=sub5)
        stu_sub_map24.save()

        stu_sub_map25 = Student_subject_mapping(student=user10, subject=sub2)
        stu_sub_map25.save()

        stu_sub_map26 = Student_subject_mapping(student=user10, subject=sub1)
        stu_sub_map26.save()

        stu_sub_map27 = Student_subject_mapping(student=user11, subject=sub5)
        stu_sub_map27.save()

        stu_sub_map28 = Student_subject_mapping(student=user12, subject=sub2)
        stu_sub_map28.save()

        stu_sub_map29 = Student_subject_mapping(student=user13, subject=sub1)
        stu_sub_map29.save()

        stu_sub_map30 = Student_subject_mapping(student=user14, subject=sub2)
        stu_sub_map30.save()

        stu_sub_map31 = Student_subject_mapping(student=user15, subject=sub3)
        stu_sub_map31.save()

        stu_sub_map32 = Student_subject_mapping(student=user16, subject=sub4)
        stu_sub_map32.save()

        stu_sub_map33 = Student_subject_mapping(student=user16, subject=sub5)
        stu_sub_map33.save()

        stu_sub_map34 = Student_subject_mapping(student=user17, subject=sub1)
        stu_sub_map34.save()

        stu_sub_map35 = Student_subject_mapping(student=user17, subject=sub3)
        stu_sub_map35.save()

        stu_sub_map36 = Student_subject_mapping(student=user18, subject=sub3)
        stu_sub_map36.save()

        stu_sub_map37 = Student_subject_mapping(student=user19, subject=sub4)
        stu_sub_map37.save()

        stu_sub_map38 = Student_subject_mapping(student=user20, subject=sub5)
        stu_sub_map38.save()
