class DataScientist:
    def __init__(self):
        self.name = "Ariyan Hridoy"
        self.role = "Data Analyst → Data Scientist"
        self.location = "Dhaka, Bangladesh"
        self.interests = ["Machine Learning", "Deep Learning", "Data Visualization", "AI"]
    
    def current_focus(self):
        return [
            "Advanced Python & Statistical Analysis",
            "Machine Learning Algorithms",
            "Deep Learning & Neural Networks",
            "MLOps & Model Deployment",
            "Cloud Computing (AWS/Azure)"
        ]
    
    def say_hi(self):
        print("Let's build something amazing with data!")

me = DataScientist()
me.say_hi()