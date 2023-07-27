import pydicom
import os

info = {}
# 读取dicom文件
dcm = pydicom.read_file("test.dcm")
info["PatientID"] = dcm.PatientID               # 患者ID
info["PatientName"] = dcm.PatientName           # 患者姓名
info["PatientBirthData"] = dcm.PatientBirthData # 患者出生日期
info["PatientAge"] = dcm.PatientAge             # 患者年龄
info['PatientSex'] = dcm.PatientSex             # 患者性别
info['StudyID'] = dcm.StudyID                   # 检查ID
info['StudyDate'] = dcm.StudyDate               # 检查日期
info['StudyTime'] = dcm.StudyTime               # 检查时间
info['InstitutionName'] = dcm.InstitutionName   # 机构名称
info['Manufacturer'] = dcm.Manufacturer         # 设备制造商
info['StudyDescription']=dcm.StudyDescription   # 检查项目描述
print(info)