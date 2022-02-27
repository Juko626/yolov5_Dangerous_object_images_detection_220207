from sklearn.model_selection import train_test_split
import yaml



from glob import glob
img_list = glob('F:\JUNSU1\images\*.png')
train_img_list, val_img_list = train_test_split(img_list, test_size=0.2, random_state=2000)

print(len(train_img_list), len(val_img_list))


with open('F:\JUNSU1\yolov5\\train.txt', 'w') as f:
  f.write('\n'.join(train_img_list) + '\n')

with open('F:\JUNSU1\yolov5\\val.txt', 'w') as f:
  f.write('\n'.join(val_img_list) + '\n')





with open('F:\JUNSU1\junsu_data.yaml', 'r') as f:
  data = yaml.safe_load(f)

data['train'] ='F:\JUNSU1\yolov5\\train.txt'
data['val']='F:\JUNSU1\yolov5\\val.txt'
with open('F:\JUNSU1\junsu_data.yaml', 'w') as f:
  yaml.dump(data, f)

print(data)
