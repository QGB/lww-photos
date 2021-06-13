#coding=utf-8
import sys;'qgb.U' in sys.modules or sys.path.append('/home/leanengine/');from qgb import *

#get_ipython().system('ps -Aef')                                        # 1 
#get_ipython().system('kill -9 32')                                     # 2 
#get_ipython().system('ps -Aef')                                        # 3 
#from qgb import *                                                      # 4 
up=U.set_input('xiublog',default=U.cbg())
p=F.mkdir(T.pathname_legalized( U.gst+up[5+3:]) )
mutex=U.mutex()
print(p)
futures=[]

def get_bytes(f,timeout=99,):
     b=N.HTTP.get_bytes(up+f,file=p+f,timeout=99 )
     mutex.acquire()
     print(U.stime()[20:],f,'%r'%b)
     mutex.release()
import concurrent.futures
with U.ThreadPoolExecutor(max_workers=22) as executor:
    for i in range(0,66):
        f='%03d.jpg'%i
        if i==0:f='0.jpg'
        if F.exist(p+f):
            print(i,'#skip')
            continue
        futures.append( executor.submit(get_bytes,f ) )

    done, not_done = concurrent.futures.wait(futures, timeout=0)
    try:
        while not_done:
            freshly_done, not_done = concurrent.futures.wait(not_done, timeout=0.2)
            done |= freshly_done
    except KeyboardInterrupt as e:
        for future in not_done:future.cancel()
        concurrent.futures.wait(not_done, timeout=None)                 # 5 
up=U.set_input('xiublog',default='')
p=F.mkdir(T.pathname_legalized( U.gst+up[5+3:]) )
mutex=U.mutex()
print(p)
futures=[]

def get_bytes(f,timeout=99,):
     b=N.HTTP.get_bytes(up+f,file=p+f,timeout=99 )
     mutex.acquire()
     print(U.stime()[20:],f,'%r'%b)
     mutex.release()
import concurrent.futures
with U.ThreadPoolExecutor(max_workers=22) as executor:
    for i in range(0,66):
        f='%03d.jpg'%i
        if i==0:f='0.jpg'
        if F.exist(p+f):
            print(i,'#skip')
            continue
        futures.append( executor.submit(get_bytes,f ) )

    done, not_done = concurrent.futures.wait(futures, timeout=0)
    try:
        while not_done:
            freshly_done, not_done = concurrent.futures.wait(not_done, timeout=0.2)
            done |= freshly_done
    except KeyboardInterrupt as e:
        for future in not_done:future.cancel()
        concurrent.futures.wait(not_done, timeout=None)                 # 6 
up=U.set_input('xiublog',default='')
p=F.mkdir(T.pathname_legalized( U.gst+up[5+3:]) )
mutex=U.mutex()
print(p)
futures=[]

def get_bytes(f,timeout=99,):
     b=N.HTTP.get_bytes(up+f,file=p+f,timeout=99 )
     mutex.acquire()
     print(U.stime()[20:],f,'%r'%b)
     mutex.release()
import concurrent.futures
with U.ThreadPoolExecutor(max_workers=22) as executor:
    for i in range(0,66):
        f='%03d.jpg'%i
        if i==0:f='0.jpg'
        if F.exist(p+f):
            print(i,'#skip')
            continue
        futures.append( executor.submit(get_bytes,f ) )

    done, not_done = concurrent.futures.wait(futures, timeout=0)
    try:
        while not_done:
            freshly_done, not_done = concurrent.futures.wait(not_done, timeout=0.2)
            done |= freshly_done
    except KeyboardInterrupt as e:
        for future in not_done:future.cancel()
        concurrent.futures.wait(not_done, timeout=None)                 # 7 
_8=p+f                                                                  # 8 
_9=F.size(p+f)                                                          # 9 
#_10=get_ipython().run_line_magic('pwd', '')                            # 10 
#_11=U.cdqp() 
get_ipython().system('git pull origin master')
U.r(py,U,T,N,F,N.HTTP,N.HTML,) 
U.cdb()                                                                 # 11 
up=U.set_input('xiublog',default='')
p=F.mkdir(T.pathname_legalized( U.gst+up[5+3:]) )
mutex=U.mutex()
print(p)
futures=[]

def get_bytes(f,timeout=99,):
     b=N.HTTP.get_bytes(up+f,file=p+f,timeout=99 )
     mutex.acquire()
     print(U.stime()[20:],f,'%r'%b)
     mutex.release()
import concurrent.futures
with U.ThreadPoolExecutor(max_workers=22) as executor:
    for i in range(0,66):
        f='%03d.jpg'%i
        if i==0:f='0.jpg'
        if F.exist(p+f):
            print(i,'#skip','%r'%F.size(p+f),)
            continue
        futures.append( executor.submit(get_bytes,f ) )

    done, not_done = concurrent.futures.wait(futures, timeout=0)
    try:
        while not_done:
            freshly_done, not_done = concurrent.futures.wait(not_done, timeout=0.2)
            done |= freshly_done
    except KeyboardInterrupt as e:
        for future in not_done:future.cancel()
        concurrent.futures.wait(not_done, timeout=None)                 # 12 
up=U.set_input('xiublog',default='')
p=F.mkdir(T.pathname_legalized( U.gst+up[5+3:]) )
mutex=U.mutex()
print(p)
futures=[]

def get_bytes(f,timeout=99,):
     b=N.HTTP.get_bytes(up+f,file=p+f,timeout=99 )
     mutex.acquire()
     print(U.stime()[20:],f,'%r'%b)
     mutex.release()
import concurrent.futures
with U.ThreadPoolExecutor(max_workers=22) as executor:
    for i in range(0,66):
        f='%03d.jpg'%i
        if i==0:f='0.jpg'
        if F.exist(p+f):
            print(i,'#skip','%r'%F.size(p+f),)
            continue
        futures.append( executor.submit(get_bytes,f ) )

    done, not_done = concurrent.futures.wait(futures, timeout=0)
    try:
        while not_done:
            freshly_done, not_done = concurrent.futures.wait(not_done, timeout=0.2)
            done |= freshly_done
    except KeyboardInterrupt as e:
        for future in not_done:future.cancel()
        concurrent.futures.wait(not_done, timeout=None)                 # 13 
up=U.set_input('xiublog',default='')
p=F.mkdir(T.pathname_legalized( U.gst+up[5+3:]) )
mutex=U.mutex()
print(p)
futures=[]

def get_bytes(f,timeout=99,):
     b=N.HTTP.get_bytes(up+f,file=p+f,timeout=99 )
     mutex.acquire()
     print(U.stime()[20:],f,'%r'%b)
     mutex.release()
import concurrent.futures
with U.ThreadPoolExecutor(max_workers=22) as executor:
    for i in range(0,66):
        f='%03d.jpg'%i
        if i==0:f='0.jpg'
        if F.exist(p+f):
            print(i,'#skip','%r'%F.size(p+f),)
            continue
        futures.append( executor.submit(get_bytes,f ) )

    done, not_done = concurrent.futures.wait(futures, timeout=0)
    try:
        while not_done:
            freshly_done, not_done = concurrent.futures.wait(not_done, timeout=0.2)
            done |= freshly_done
    except KeyboardInterrupt as e:
        for future in not_done:future.cancel()
        concurrent.futures.wait(not_done, timeout=None)                 # 14 
up=U.set_input('xiublog',default='')
p=F.mkdir(T.pathname_legalized( U.gst+up[5+3:]) )
mutex=U.mutex()
print(p)
futures=[]

def get_bytes(f,timeout=99,):
     b=N.HTTP.get_bytes(up+f,file=p+f,timeout=99 )
     mutex.acquire()
     print(U.stime()[20:],f,'%r'%b)
     mutex.release()
import concurrent.futures
with U.ThreadPoolExecutor(max_workers=22) as executor:
    for i in range(0,66):
        f='%03d.jpg'%i
        if i==0:f='0.jpg'
        if F.exist(p+f):
            print(i,'#skip','%r'%F.size(p+f),)
            continue
        futures.append( executor.submit(get_bytes,f ) )

    done, not_done = concurrent.futures.wait(futures, timeout=0)
    try:
        while not_done:
            freshly_done, not_done = concurrent.futures.wait(not_done, timeout=0.2)
            done |= freshly_done
    except KeyboardInterrupt as e:
        for future in not_done:future.cancel()
        concurrent.futures.wait(not_done, timeout=None)                 # 15 
up=U.set_input('xiublog',default='')
p=F.mkdir(T.pathname_legalized( U.gst+up[5+3:]) )
mutex=U.mutex()
print(p)
futures=[]

def get_bytes(f,timeout=99,):
     b=N.HTTP.get_bytes(up+f,file=p+f,timeout=99 )
     mutex.acquire()
     print(U.stime()[20:],f,'%r'%b)
     mutex.release()
import concurrent.futures
with U.ThreadPoolExecutor(max_workers=22) as executor:
    for i in range(0,66):
        f='%03d.jpg'%i
        if i==0:f='0.jpg'
        if F.exist(p+f):
            print(i,'#skip','%r'%F.size(p+f),)
            continue
        futures.append( executor.submit(get_bytes,f ) )

    done, not_done = concurrent.futures.wait(futures, timeout=0)
    try:
        while not_done:
            freshly_done, not_done = concurrent.futures.wait(not_done, timeout=0.2)
            done |= freshly_done
    except KeyboardInterrupt as e:
        for future in not_done:future.cancel()
        concurrent.futures.wait(not_done, timeout=None)                 # 16 
up=U.set_input('xiublog',default='')
p=F.mkdir(T.pathname_legalized( U.gst+up[5+3:]) )
mutex=U.mutex()
print(p)
futures=[]

def get_bytes(f,timeout=99,):
     b=N.HTTP.get_bytes(up+f,file=p+f,timeout=99 )
     mutex.acquire()
     print(U.stime()[20:],f,'%r'%b)
     mutex.release()
import concurrent.futures
with U.ThreadPoolExecutor(max_workers=22) as executor:
    for i in range(0,99):
        f='%03d.jpg'%i
        if i==0:f='0.jpg'
        if F.exist(p+f):
            print(i,'#skip','%r'%F.size(p+f),)
            continue
        futures.append( executor.submit(get_bytes,f ) )

    done, not_done = concurrent.futures.wait(futures, timeout=0)
    try:
        while not_done:
            freshly_done, not_done = concurrent.futures.wait(not_done, timeout=0.2)
            done |= freshly_done
    except KeyboardInterrupt as e:
        for future in not_done:future.cancel()
        concurrent.futures.wait(not_done, timeout=None)                 # 17 
#_18=U.cdqp() 
get_ipython().system('git pull origin master')
U.r(py,U,T,N,F,N.HTTP,N.HTML,) 
U.cdb()                                                                 # 18 
#_19=U.cdqp() 
get_ipython().system('git pull origin master')
U.r(py,U,T,N,F,N.HTTP,N.HTML,) 
U.cdb()                                                                 # 19 
up=U.set_input('xiublog',default='')
p=F.mkdir(T.pathname_legalized( U.gst+up[5+3:]) )
mutex=U.mutex()
print(p)
futures=[]

def get_bytes(f,timeout=99,):
     b=N.HTTP.get_bytes(up+f,file=p+f,timeout=99 )
     mutex.acquire()
     print(U.stime()[20:],f,'%r'%b)
     mutex.release()
import concurrent.futures
with U.ThreadPoolExecutor(max_workers=22) as executor:
    for i in range(0,99):
        f='%03d.jpg'%i
        if i==0:f='0.jpg'
        if F.exist(p+f):
            print(i,'#skip','%r'%F.size(p+f),)
            continue
        futures.append( executor.submit(get_bytes,f ) )

    done, not_done = concurrent.futures.wait(futures, timeout=0)
    try:
        while not_done:
            freshly_done, not_done = concurrent.futures.wait(not_done, timeout=0.2)
            done |= freshly_done
    except KeyboardInterrupt as e:
        for future in not_done:future.cancel()
        concurrent.futures.wait(not_done, timeout=None)                 # 20 
up=U.set_input('xiublog',default='')
p=F.mkdir(T.pathname_legalized( U.gst+up[5+3:]) )
mutex=U.mutex()
print(p)
futures=[]

def get_bytes(f,timeout=99,):
     b=N.HTTP.get_bytes(up+f,file=p+f,timeout=99 )
     mutex.acquire()
     print(U.stime()[20:],f,'%r'%b)
     mutex.release()
import concurrent.futures
with U.ThreadPoolExecutor(max_workers=22) as executor:
    for i in range(0,99):
        f='%03d.jpg'%i
        if i==0:f='0.jpg'
        if F.exist(p+f):
            print(i,'#skip','%r'%F.size(p+f),)
            continue
        futures.append( executor.submit(get_bytes,f ) )

    done, not_done = concurrent.futures.wait(futures, timeout=0)
    try:
        while not_done:
            freshly_done, not_done = concurrent.futures.wait(not_done, timeout=0.2)
            done |= freshly_done
    except KeyboardInterrupt as e:
        for future in not_done:future.cancel()
        concurrent.futures.wait(not_done, timeout=None)                 # 21 
_22=p                                                                   # 22 
_23=F.ls(p)                                                             # 23 
_24=len(_)                                                              # 24 
#get_ipython().run_line_magic('cd', '~/testt')                          # 25 
#get_ipython().run_line_magic('cd', '~/test')                           # 26 
#get_ipython().run_line_magic('ls', '')                                 # 27 
#get_ipython().run_line_magic('ll', '')                                 # 28 
#get_ipython().system('du -m |sort -n')                                 # 29 
#get_ipython().system('df -h')                                          # 30 
up=U.set_input('xiublog',default='')
p=F.mkdir(T.pathname_legalized( U.gst+up[5+3:]) )
mutex=U.mutex()
print(p)
futures=[]

def get_bytes(f,timeout=99,):
     b=N.HTTP.get_bytes(up+f,file=p+f,timeout=99 )
     mutex.acquire()
     print(U.stime()[20:],f,'%r'%b)
     mutex.release()
import concurrent.futures
with U.ThreadPoolExecutor(max_workers=22) as executor:
    for i in range(0,99):
        f='%03d.jpg'%i
        if i==0:f='0.jpg'
        if F.exist(p+f):
            print(i,'#skip','%r'%F.size(p+f),)
            continue
        futures.append( executor.submit(get_bytes,f ) )

    done, not_done = concurrent.futures.wait(futures, timeout=0)
    try:
        while not_done:
            freshly_done, not_done = concurrent.futures.wait(not_done, timeout=0.2)
            done |= freshly_done
    except KeyboardInterrupt as e:
        for future in not_done:future.cancel()
        concurrent.futures.wait(not_done, timeout=None)                 # 31 
#ipy.save(_i)                                                           # 32 
f="/home/leanengine/test/ipy/up=U.set_input('xiublog',default='') p=F.mkdir(T.pathname_legalized( U.gst+up[5+3__]) ) mutex=U.mutex() print(p) futures=[] def get_bytes(f,timeout=99,)__ b=N.HTTP.get_bytes(up+f,file=p+f,timeout=99 ) mutex.acquire() print(U.stime()[20__],f,'%r'%b) mutex..py"  # 33 
_34=f                                                                   # 34 
F.wrie(f,1)                                                             # 35 
F.write(f,1)                                                            # 36 
_37=len(f)                                                              # 37 
_38=f[16:]                                                              # 38 
_39=f[20:]                                                              # 39 
_40=f[26:]                                                              # 40 
_41=f[26:]                                                              # 41 
_42=len(f[26:])                                                         # 42 
#_43=ipy.input('ipy.save')                                              # 43 
_44=_i31                                                                # 44 
#ipy.save(_i31)                                                         # 45 
_46=len(f[26:])                                                         # 46 
_47=f                                                                   # 47 
_48=F.new(f)                                                            # 48 
#_49=ipy.gsavePath                                                      # 49 
#_50=len(ipy.gsavePath)                                                 # 50 
#_51=U.cdqp() 
get_ipython().system('git pull origin master')
U.r(py,U,T,N,F,N.HTTP,N.HTML,) 
U.cdb()                                                                 # 51 
U.r(ipy)                                                                # 52 
#ipy.save(_i31)                                                         # 53 
#get_ipython().run_line_magic('debug', 'ipy.save(_i31)')                # 54 
#_55=U.cdqp() 
get_ipython().system('git pull origin master')
U.r(py,U,T,N,F,N.HTTP,N.HTML,) 
U.cdb()                                                                 # 55 
U.r(ipy)                                                                # 56 
#ipy.save(_i31)                                                         # 57 
_58=f                                                                   # 58 
#_59=U.cdqp() 
get_ipython().system('git pull origin master')
U.r(py,U,T,N,F,N.HTTP,N.HTML,) 
U.cdb()                                                                 # 59 
U.r(ipy)                                                                # 60 
#ipy.save(_i31)                                                         # 61 
#_62=U.cdqp() 
get_ipython().system('git pull origin master')
U.r(py,U,T,N,F,N.HTTP,N.HTML,ipy) 
U.cdb()                                                                 # 62 
#ipy.save(_i31)                                                         # 63 
#_64=U.cdqp() 
get_ipython().system('git pull origin master')
U.r(py,U,T,N,F,N.HTTP,N.HTML,ipy) 
U.cdb()                                                                 # 64 
#_65=ipy.save(_i31)                                                     # 65 
#_66=get_ipython().run_line_magic('pwd', '')                            # 66 
#get_ipython().run_line_magic('ll', '-alhR')                            # 67 
#get_ipython().run_line_magic('ll', '')                                 # 68 
#get_ipython().run_line_magic('rm', 'up*')                              # 69 
#get_ipython().run_line_magic('ll', '')                                 # 70 
_71=F.ls('./ipy/')                                                      # 71 
_72=_[0]                                                                # 72 
f=_                                                                     # 73 
#get_ipython().system('vim {repr(f)}')                                  # 74 
#get_ipython().system('vi {repr(f)}')                                   # 75 
#_76=ipy.save()                                                         # 76 
#get_ipython().system('vi {repr(f)}')                                   # 77 
#get_ipython().system('git init')                                       # 78 
#get_ipython().system('git add -A;git commit -m init')                  # 79 
#get_ipython().system('git config --global user.email "you@example.com";git config --global user.name "Your Name"')  # 80 
#get_ipython().system('git add -A;git commit -m init')                  # 81 
#ipy.save()                                                             # 82 
