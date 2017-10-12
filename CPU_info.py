# coding:utf8
import psutil
logical_cores = psutil.cpu_count(logical=True)
if logical_cores is None:
    logical_cores = 1

physical_cores = psutil.cpu_count(logical=False)
if physical_cores is None:
    physical_cores = 1

print ("逻辑处理器: %d" % (logical_cores),"个")
print ("物理处理器: %d" % (physical_cores),'个')

if logical_cores / physical_cores == 2:
    print ("超线程: 支持")
else:
    print ("超线程: 不支持")