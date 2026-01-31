class Instructor:
    
    def __init__(self,name ,tecnology ,experience, feedback):
        
        self.name= name
        self.tecnology = tecnology
        self.experience = experience
        self.feedback = feedback
    def eligibility(self):
        
        if  self.experience>3 and self.feedback>=4.5:
            return True
        elif self.experience<=3 and self.feedback>=4:
            return True
        else:
            return False
        
    def allocate_course(self,tech):
        is_eligible = self.eligibility()
        if is_eligible:
            if tech in self.tecnology:
                return "Padha sakta hai"
            else:
                return 'ye to uska ata hi nehib hai'
        else:
            return 'achha teacher nehi hai'    
                    
I = Instructor('himu',['Python','c'],4,4.5)
I.allocate_course('Python')
                         