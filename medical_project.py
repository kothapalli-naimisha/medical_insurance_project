class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    # add more parameters here
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker
  
  #created estimated_insurance_cost method to calculate expected yearly medical fees of patients
  def estimated_insurance_cost(self):
    estimated_cost= 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    print("{name}'s estimated insurance cost is {cost} dollars.".format(name = self.name , cost = estimated_cost) )
  
  #created update_age method for updating the patients age and calling estimated_insurance_cost method so that once after updating the age patients can see the expected medical fee.
  def update_age(self, new_age):
    self.age = new_age
    print("{Name} is now {Age} years old.".format(Name = self.name, Age = self.age))
    self.estimated_insurance_cost()
  
  #created update_num_children method for updating the patients childrens and calling estimated_insurance_cost method so that once after updating, patients can see the expected medical fee.
  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children == 1:
      print("{Name} has {children} child.".format(Name = self.name, children = self.num_of_children))
    else:
      print("{Name} has {children} children.".format(Name = self.name, children = self.num_of_children))
    self.estimated_insurance_cost()
  
  #created patient_profile to store patients information in one convenient variable, here dictonary is used since it has key and value pairs and can easily readable.
  def patient_profile(self):
    patient_information = {}
    patient_information["Name"] = self.name
    patient_information["Age"] = self.age
    patient_information["Sex"] = self.sex
    patient_information["BMI"] = self.bmi
    patient_information["Number of Children"] = self.num_of_children
    patient_information["Smoker"] = self.smoker
    return patient_information


patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
#print(patient1.sex)
#patient1.estimated_insurance_cost()
#patient1.update_age(26)
#patient1.update_num_children(1)
print(patient1.patient_profile())


