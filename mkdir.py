import os 



array = ['Abhishek Bachchan','Aditya Roy Kapur','Akkineni Nagarjuna','Akshaye Khanna','Anil Kapoor','Anupam Kher','Arbaaz Khan','Arjun Kapoor','Arshad Warsi','Ayushman Khurrana','Anu Kapoor','Amrish Puri','Alok Nath','Bobby Deol','Dharam Singh Deol','Dilip Joshi','Emraan Hashmi','Himesh Reshammiya','Honey Singh','Jackie Shroff','John Abraham','Karan Johar','Kartik Aaryan','Kay Kay Menon','Nana Patekar','Naseeruddin Shah','Nawazuddin Siddiqui','Om Puri','Prabhas','Prabhu Deva','Rishi Kapoor','Rajinikanth','Rajpal Yadav','Riteish Deshmukh','Sonu Sood','Sunny Deol','Sushant Singh Rajput','Varun Dhawan','Vivek Oberoi','Sidharth Malhotra']
print(len(array))

for x in array:
  	# Directory 
	directory = x
	  
	# Parent Directory path 
	parent_dir = "./"
	  
	# Path 
	path = os.path.join(parent_dir, directory) 
	  
	# Create the directory 
	# 'GeeksForGeeks' in 
	# '/home / User / Documents' 
	os.mkdir(path) 
	print("Directory '% s' created" % directory) 
  
# Directory 
# directory = "Geeks"
  
# # Parent Directory path 
# parent_dir = "D:/Pycharm projects"
  
# # mode 
# mode = 0o666
  
# # Path 
# path = os.path.join(parent_dir, directory) 
  
# # Create the directory 
# # 'GeeksForGeeks' in 
# # '/home / User / Documents' 
# # with mode 0o666 
# os.mkdir(path, mode) 
# print("Directory '% s' created" % directory) 
