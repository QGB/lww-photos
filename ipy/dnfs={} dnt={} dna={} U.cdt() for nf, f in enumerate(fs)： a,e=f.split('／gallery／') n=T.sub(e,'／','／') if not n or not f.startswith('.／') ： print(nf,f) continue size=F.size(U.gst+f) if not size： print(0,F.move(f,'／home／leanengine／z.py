#coding=utf-8
import sys;'qgb.U' in sys.modules or sys.path.append('/home/leanengine/');from qgb import *

#_1=get_ipython().run_line_magic('pwd', '')                             # 1 
U.gst                                                                   # 2 
#get_ipython().run_line_magic('cd', '..')                               # 3 
#from qgb import *                                                      # 4 
_5=U.cdt()                                                              # 5 
#get_ipython().run_line_magic('ls', '')                                 # 6 
_7=F.ls()                                                               # 7 
fs=F.ls('./img.xiublog.com__85/',r=1)                                   # 8 
_9=fs                                                                   # 9 
fs=F.ls('./img.xiublog.com__85/',r=1)                                   # 10 
_11=fs                                                                  # 11 
_12=F.ls('./img.xiublog.com__85/',r=1)                                  # 12 
F.ls('./img.xiublog.com__85/',1)                                        # 13 
_14=F.ls('./img.xiublog.com__85/',t='a')                                # 14 
_15=F.ls('./img.xiublog.com__85/',)                                     # 15 
_16=F.ls('./img.xiublog.com__85/',)                                     # 16 
#_17=get_ipython().run_line_magic('pwd', '')                            # 17 
_18=F.ls('./img.xiublog.com：85/gallery/27715/')                         # 18 
_19=F.ls('./img.xiublog.com：85/')                                       # 19 
_20=F.ls('./img.xiublog.com：85/',r=1)                                   # 20 
fs=F.ls('./img.xiublog.com：85/',r=1)                                    # 21 
_22=fs[-2]                                                              # 22 
_23=fs[-2][12:]                                                         # 23 
_24=fs[-2][16:]                                                         # 24 
_25=fs[-2][18]                                                          # 25 
_26=fs[-2][17]                                                          # 26 
_27=ord(fs[-2][17])                                                     # 27 
f=fs[-2]                                                                # 28 
for f in fs:
    a,e=f.split('/gallery/')
    a=a+'/gallery/'
    n=T.sub(e,'','/')                                                   # 29 
_30=n                                                                   # 30 
_31=a                                                                   # 31 
_32=e                                                                   # 32 
_33=n                                                                   # 33 
dnf={}
for f in fs:
    a,e=f.split('/gallery/')
    n=T.sub(e,'/','/')
    if not n: xxx
    a=T.sub(f,n+'/') #.../gallery/27715/
    U.dict_value_set(dnf,n,f)                                           # 34 
_35=n                                                                   # 35 
_36=a                                                                   # 36 
_37=e                                                                   # 37 
dnf={}
for nf, f in enumerate(fs):
    a,e=f.split('/gallery/')
    n=T.sub(e,'/','/')
    if not n:
        print(nf,f)
        continue
    a=T.sub(f,n+'/') #.../gallery/27715/
    U.dict_value_set(dnf,n,f)                                           # 38 
_39=dnf                                                                 # 39 
_40=len(dnf)                                                            # 40 
#_41=get_ipython().run_line_magic('pwd', '')                            # 41 
#get_ipython().run_line_magic('cd', 'fs[1]')                            # 42 
_43=U.cd(fs[1])                                                         # 43 
#get_ipython().run_line_magic('ll', '')                                 # 44 
_45=list(dnf)                                                           # 45 
dnfs={}
dnt={}
dna={}
for nf, f in enumerate(fs):
    a,e=f.split('/gallery/')
    n=T.sub(e,'/','/')
    if not n or not f.startswith('./'):
        print(nf,f)
        continue   
    a=T.sub(f,n+'/') #.../gallery/27715/
    dna[f]=a
    if n not in dnt:dnt[n]=''
    dnt[n]+='![image](%s)'%f[1:]
    
    U.dict_value_set(dnfs,n,f)
    
sumr=''''# lww-photos
林文文 出道至今的高清写真套图共22部，写真持续更新中～，敬请期待～  
'''
for n,t in dnt.items():
    dnt[n]=''
    for f in  fs:
        dnt[n]+= ''                                                     # 46 
_47=sumr                                                                # 47 
N.rpcServer(globals=globals(),locals=globals(),)                        # 48 
#get_ipython().run_line_magic('pip', 'install --user flask dill')       # 49 
N.rpcServer(globals=globals(),locals=globals(),)                        # 50 
N.rpcServer(globals=globals(),locals=globals(),)                        # 51 
N.rpcServer(globals=globals(),locals=globals(),)                        # 52 
_53=sys                                                                 # 53 
_54=sys.path                                                            # 54 
#_55=get_ipython().run_line_magic('pwd', '')                            # 55 
#get_ipython().run_line_magic('cd', '~')                                # 56 
#get_ipython().system('find -name dill')                                # 57 
sys.path.insert(0,'/home/leanengine/.local/lib/python3.9/site-packages')  # 58 
import diill                                                            # 59 
import diil                                                             # 60 
import dill                                                             # 61 
_62=N.rpcServer(globals=globals(),locals=globals(),)                    # 62 
_63=f                                                                   # 63 
_64=F.size(f)                                                           # 64 
_65=F.size(fs[44])                                                      # 65 
#get_ipython().run_line_magic('cd', '-')                                # 66 
#get_ipython().run_line_magic('cd', '-')                                # 67 
#get_ipython().run_line_magic('cd', '~/test')                           # 68 
_69=F.size(fs[44])                                                      # 69 
F.size(66)                                                              # 70 
_71=F.size(f)                                                           # 71 
_72=[f for f in fs if F.size(f)==0]                                     # 72 
_73=F.size(_[3])                                                        # 73 
#_74=get_ipython().run_line_magic('pwd', '')                            # 74 
#get_ipython().run_line_magic('mkdir', '~/zero')                        # 75 
#dnfs={}
dnt={}
dna={}
for nf, f in enumerate(fs):
    a,e=f.split('/gallery/')
    n=T.sub(e,'/','/')
    if not n or not f.startswith('./'):
        print(nf,f)
        continue   
    size=F.size(f)    
    
    a=T.sub(f,n+'/') #.../gallery/27715/
    dna[f]=a
    if n not in dnt:dnt[n]=''
    dnt[n]+='![image](%s)'%f[1:]
    
    U.dict_value_set(dnfs,n,f)
    
sumr=''''# lww-photos
林文文 出道至今的高清写真套图共22部，写真持续更新中～，敬请期待～  
'''
for n,t in dnt.items():
    dnt[n]=''
    for f in  fs:
        dnt[n]+= ''    
    
    
    =                                                                   # 76 
_77=f                                                                   # 77 
_78=F.size(U.gst+f)                                                     # 78 
_79=dnfs={}
dnt={}
dna={}
U.cdt()
for nf, f in enumerate(fs):
    a,e=f.split('/gallery/')
    n=T.sub(e,'/','/')
    if not n or not f.startswith('./') :
        print(nf,f)
        continue   
    size=F.size(U.gst+f)
    if not size:
        print(0,F.move(f,'/home/leanengine/zero/')    )
        continue
    #a=T.sub(f,n+'/') #.../gallery/27715/
    #dna[f]=a
    if n not in dnt:dnt[n]=''
    dnt[n]+='`{0}`\n![image]({0})'.format(f[1:])
    
    U.dict_value_set(dnfs,n,f)
    
sumr=''''# lww-photos
林文文 出道至今的高清写真套图共22部，写真持续更新中～，敬请期待～  
<hr>
'''
for ni, n in enumerate(dnt):
    ft=F.write(U.gst+n+'.md',dnt[n])
    print(ni,ft)
    sumr+='#### [{0}.{1}]({1})\n\n'.format(ni,'/%s.md'%n)
    
F.write(U.gst+'README.md',sumr)                                         # 79 
#get_ipython().run_line_magic('ll', '')                                 # 80 
#get_ipython().system('vi README.md')                                   # 81 
_82=[f for f in fs if F.size(f)==0]                                     # 82 
_83=F.size(_[3])                                                        # 83 
F.size(_[3])==0                                                         # 84 
#get_ipython().run_line_magic('ll', '')                                 # 85 
#ipy.save(_i79)                                                         # 86 
