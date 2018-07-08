import pyscreenshot as ps 
import pytesseract
import re 
from google import google
import time

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def main():
	start_time=time.time()
	im=ps.grab(bbox=(70,250,600,1000))
	text = pytesseract.image_to_string(im)
	print(text)
	im.show()
	txt,ind=text.split("\n"),-1
	for l in range(len(txt)):
		txt[l].replace("u","")
		#print(1111)
		#print(line)
		kk=txt[l].split('?')
		#print(txt[l])
		if(len(kk)>1):
			ind=l 
			#break
	str1=''
	for i in range(ind+1):
		str1+=str(txt[i].encode('utf-8'))+" "
	print bcolors.OKBLUE+str1+bcolors.ENDC
	arr1,arr2,arr3=[],[],[]
	for j in range(ind+1,len(txt)):
		txt[j]=txt[j].encode('utf-8').lower()
		if len(txt[j])!=0:
			arr1.append((txt[j]))
			rr=txt[j].split(" ")
			if len(rr)>1:
				for i in rr:
					arr1.append(i)
	for l in range(len(arr1)):
		if l>0:
			tt=False
			for m in arr1[0:l]:
				if m==arr1[l]:
					tt=True
			if tt==False:
				arr1[l].replace("(","")
				arr1[l].replace(")","")
				arr3.append(arr1[l])
		else:
			arr1[l].replace("(","")
			arr1[l].replace(")","")
			arr3.append(arr1[l])
	#print arr1
	result=google.search(str1.decode('utf-8'))
	for j in arr3:
		count=0
		for i in result:
			count+=sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(j.decode('utf-8')), (i.description).lower()))
		if count !=0:
			arr2.append([j,count])
	arr2=sorted(arr2,key=lambda x:x[1],reverse=True)
	print bcolors.HEADER+"******ANSWERS*******"+bcolors.ENDC
	for t in arr2:
		print 'WORD:- '+bcolors.OKGREEN+t[0]+bcolors.ENDC+', OCCURENCE:- '+bcolors.OKGREEN+str(t[1])+bcolors.ENDC
	end_time=time.time()
	if len(arr2)==0:
		for i in result:
			print "*****************"
			print i.description
			print "*****************"
	print end_time-start_time

if __name__=='__main__':
	while(1):
		r=raw_input(bcolors.WARNING+'Press s followed by ENTER to capture and process screenshot'+bcolors.ENDC)
		print r
		if r.lower()=='s':
			main()
		else:
			break