# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from netCDF4 import Dataset

nc_obj = Dataset('D:\\code\\ICM\\algorithms\\data\\had.nc')

# 查看nc文件有些啥东东
print(nc_obj)
print('---------------------------------------')

# 查看nc文件中的变量
print(nc_obj.variables.keys())
for i in nc_obj.variables.keys():
    print(i)
print('---------------------------------------')

# 查看每个变量的信息
print(nc_obj.variables['latitude'])
print(nc_obj.variables['longitude'])
print(nc_obj.variables['time'])
print(nc_obj.variables['temperature_anomaly'])
print(nc_obj.variables['field_status'])
print('---------------------------------------')

# 查看每个变量的属性
print(nc_obj.variables['latitude'].ncattrs())
print(nc_obj.variables['longitude'].ncattrs())
print(nc_obj.variables['time'].ncattrs())
print(nc_obj.variables['temperature_anomaly'].ncattrs())
print(nc_obj.variables['field_status'].ncattrs())

print('---------------------------------------')

# 读取数据值
print(nc_obj.variables['latitude'][:])
print(nc_obj.variables['longitude'][:])
print(nc_obj.variables['time'][:])
print(nc_obj.variables['temperature_anomaly'][:])
print(nc_obj.variables['field_status'][:])
lat = (nc_obj.variables['LAT'][:])
lon = (nc_obj.variables['LON'][:])
prcp = (nc_obj.variables['PRCP'][:])
print(lat)
print(lon)
print('---------------******-------------------')
print(prcp)
