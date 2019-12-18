from institute import *
facultylist=[]
courselist=[]
batchlist=[]
def add_faculty(rollno,name):
    f=Faculty()
    f.set_rollno(rollno)
    f.set_name(name)
    facultylist.append(f)
def show_faculty(fl=facultylist):
    for s in fl:
        print("faculity Id:- ",s.get_rollno(),"faculity name:- ",s.get_name())

def info_faculty(fname):
    for course in courselist:
        for c in course.get_faculty():
            if c.get_name()==fname:
                print("course assign : ",course.get_name())
##################################################################################
def find_faculty(facultyname):
    l=[]
    for x in facultyname:
        for f in facultylist:
            if f.get_name() ==x:
                l.append(f)
    return l

def add_course(id1,name,*facultyname):
    c=Course()
    c.set_id(id1)
    c.set_name(name)
    c.set_faculty(find_faculty(facultyname))
    courselist.append(c)

def add_ftoc(course_name,*facultyname):
    for cs in courselist:
        if cs.get_name()==course_name:
            cs.set_faculty(find_faculty(facultyname))

def show_cf(course_name):

        i=courselist.index(course_name)
        show_faculty(courselist[i].get_faculty())

       # print(f"course not found: '{course_name}'")

def show_courses(l=courselist):
    for x in l:
        print("course Id:- ",x.get_id(),"course name:-",x.get_name())
###################################################################################

def add_batch(name,course_name,fname):
    b=Batch()
    b.set_name(name)
    try:
        i=courselist.index(course_name)
        b.set_course(courselist[i])
       # batchlist.append(b)
    except:
        print(f"couse not found: '{course_name}'")
    for x in b.get_course().get_faculty():
        if x.get_name==fname:
            b.set_fname(fname)

def show_bc(batch_name):
    try:
        i=batchlist.index(batch_name)
        print("cousre name",batchlist[i].get_course().get_name())
    except:
        print(f"batch not found: '{batch_name}'")
def show_batchs(l=batchlist):
    for x in batchlist:
        print("Batch Name:- ",x.get_name())
#####################################################################################
def add_student(name,batch_name):
    s=Student()
    s.set_name(name)
    s.set_batch
