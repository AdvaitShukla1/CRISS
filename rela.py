from PIL import Image, ImageOps
import numpy as np
img = Image.open("img.JPG")
img_gray = ImageOps.grayscale(img)
img_as_array = np.asarray(img_gray)
data = img_as_array.flatten()
class Statistic_Data:
  def __init__(self,array):
    self.number_of_students =data.shape[0]
    self.name_of_teacher="Advait Shukla"
    self.data=data
    self.stats={'mean':0,'median':0,'maximum':0,'minimum':0,'Standard Deviation':0}
    self.summary =[]
    min,max=np.min(self.data),np.max(self.data)
    n_arr=[]

    for i in array:
      temp=((i-min)/(max-min))*100
      n_arr.append(temp)
    self.data=n_arr
  def set_num_students(self):
    self.number_of_students =len(self.data)
  def statistics_calculator(self):
    self.stats['mean']=np.mean(self.data)
    self.stats['median']=np.median(self.data)
    self.stats['maximum']=np.max(self.data)
    self.stats['minimum']=np.min(self.data)
    self.stats['Standard Deviation']=np.std(self.data)
  def organizer(self):
    self.summary=[self.name_of_teacher,self.number_of_students,self.stats]
    print(self.summary,sep='/n')
test=Statistic_Data(data)
test.statistics_calculator()
test.organizer()