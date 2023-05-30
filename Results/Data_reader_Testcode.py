import pickle


def load_dumps(ff):
  obj = []
  while 1:
    try:
      obj.append(pickle.load(ff))
    except:
      break
  return obj



NoA=1 #input_subject_number
NoB=2
op="dataset1" #input_dataset_name


file=open(f'kekka_hon_No_{NoA}-{NoB}/hon_No_{NoA}-{NoB}_C_{op}_A.bin',"rb")
file2=open(f'kekka_hon_No_{NoA}-{NoB}/hon_No_{NoA}-{NoB}_AC_{op}_A.bin',"rb")
file3=open(f'kekka_hon_No_{NoA}-{NoB}/hon_No_{NoA}-{NoB}_C_{op}_B.bin',"rb")
file4=open(f'kekka_hon_No_{NoA}-{NoB}/hon_No_{NoA}-{NoB}_AC_{op}_B.bin',"rb")
C_A=load_dumps(file)
AC_A=load_dumps(file2)
C_B=load_dumps(file3)
AC_B=load_dumps(file4)
file.close()
file2.close()
file3.close()
file4.close()

print("C_A:",C_A)
print("AC_A:",AC_A)
print("C_B:",C_B)
print("AC_B:",AC_B)
