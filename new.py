import SimpleITK as sitk 
fileName = '/Users/ryan/ACL Rupture/001'
dicom = sitk.ReadImage(fileName)
print(dicom.GetMetaData('0010|0020')) # patient ID
print(dicom.GetMetaData('0008|0020')) # study date
print(dicom.GetMetaData('0020|1041')) # slice location