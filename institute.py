class Student:
   def set_frollno(self,rollno): self.rollno=rollno
   def get_frollno(self): return self.rollno
   def set_name(self,name): self.name=name
   def get_name(self): return self.name
   def set_batch(self,batch): self.batch=batch
   def get_batch(self): return self.batch
   
############################################################################################################    
class Faculty:
    def set_rollno(self,rollno):
        self.rollno=rollno
    def get_rollno(self):
        return self.rollno
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def __eq__(self,other):
        return type(self)==type(other) and (self.name==other.name or self.rollno==other.rollno)
    
############################################################################################################
class Course:
    def set_id(self,id1):
        self.id1=id1
    def get_id(self):
        return self.id1
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def set_faculty(self,faculty):
        try :
            if self.faculty:
                self.faculty+=faculty
        except:
            self.faculty=faculty

    def get_faculty(self): return self.faculty
    def __eq__(self,other):return self.name==other
#####################################################################################################################
class Batch:
    def set_name(self,name): self.name=name
    def get_name(self): return self.name
    def set_course(self,course): self.course=course
    def get_course(self): return self.course
    def set_fname(self,fname):self.fname=fname
    def get_fname(self): return self.fname
    def __eq__(self,other): return self.name==other

