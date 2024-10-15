import open3d as o3d
from o3d_tools.visualize import PointCloudProject

project2 = PointCloudProject(project='Project2')


attributes_and_methods = dir(project2)

# Print all attributes and methods
#print("All attributes and methods:", attributes_and_methods)
filtered_attributes_and_methods = [attr for attr in attributes_and_methods if not attr.startswith('__')]
print("Filtered attributes and methods:", filtered_attributes_and_methods)