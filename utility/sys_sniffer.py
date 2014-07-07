#!/usr/bin/python
#coding=utf8
import os

#get system's memory infomation
def memory_stat():
	mem = {}
	f = open("/proc/meminfo")
	lines = f.readlines()
	f.close()
	for line in lines:
		if len(line) < 2: continue
		name = line.split(':')[0]
		var = line.split(':')[1].split()[0]
		mem[name] = long(var) * 1024.0
	mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
	return mem

#get system's cpu information
def cpu_stat():
    cpu = []
    cpuinfo = {}
    f = open("/proc/cpuinfo")
    lines = f.readlines()
    f.close()
    for line in lines:
        if line == '\n':
            cpu.append(cpuinfo)
            cpuinfo = {}
        if len(line) < 2: continue
        name = line.split(':')[0].rstrip()
        var = line.split(':')[1]
        cpuinfo[name] = var
    return cpu

#get system's load information
def load_stat():
    loadavg = {}
    f = open("/proc/loadavg")
    con = f.read().split()
    f.close()
    loadavg['lavg_1']=con[0]
    loadavg['lavg_5']=con[1]
    loadavg['lavg_15']=con[2]
    loadavg['nr']=con[3]
    loadavg['last_pid']=con[4]
    return loadavg

#get machine's up time
def uptime_stat():
    uptime = {}
    f = open("/proc/uptime")
    con = f.read().split()
    f.close()
    all_sec = float(con[0])
    MINUTE,HOUR,DAY = 60,3600,86400
    uptime['day'] = int(all_sec / DAY )
    uptime['hour'] = int((all_sec % DAY) / HOUR)
    uptime['minute'] = int((all_sec % HOUR) / MINUTE)
    uptime['second'] = int(all_sec % MINUTE)
    uptime['Free rate'] = float(con[1]) / float(con[0])
    return uptime

#get netstat
def net_stat():
    net = []
    f = open("/proc/net/dev")
    lines = f.readlines()
    f.close()
    for line in lines[2:]:
		content = line.split(':')
		con = content[1].split()
		intf = dict(
            zip(
                ( 'interface','ReceiveBytes','ReceivePackets',
                  'ReceiveErrs','ReceiveDrop','ReceiveFifo',
                  'ReceiveFrames','ReceiveCompressed','ReceiveMulticast',
                  'TransmitBytes','TransmitPackets','TransmitErrs',
                  'TransmitDrop', 'TransmitFifo','TransmitFrames',
                  'TransmitCompressed','TransmitMulticast' ),
                ( content[0].rstrip(':'),int(con[0]),int(con[1]),
                  int(con[2]),int(con[3]),int(con[4]),
                  int(con[5]),int(con[6]),int(con[7]),
                  int(con[8]),int(con[9]),int(con[10]),
                  int(con[11]),int(con[12]),int(con[13]),
                  int(con[14]),int(con[15]))
            )
        )
		net.append(intf)
    return net

#get hard disk's state
def disk_stat():
    hd={}
    disk = os.statvfs("/")
    hd['available'] = disk.f_bsize * disk.f_bavail
    hd['capacity'] = disk.f_bsize * disk.f_blocks
    hd['used'] = disk.f_bsize * disk.f_bfree
    return hd

if __name__=="__main__":
	memstat = memory_stat()
	print '--------------------------------------------------'
	for key in memstat.keys():
		print key,'\t',memstat[key]
	print '--------------------------------------------------'
	cpustat = cpu_stat()
	for cpuinfo in cpustat:
		for key in cpuinfo:
			print key,'\t',cpuinfo[key]
	print '--------------------------------------------------'
	loadstat = load_stat()
	for key in loadstat.keys():
		print key,'\t',loadstat[key]
	print '--------------------------------------------------'
	uptime = uptime_stat()
	for key in uptime.keys():
		print key,'\t',uptime[key]
	print '--------------------------------------------------'
	diskstat = disk_stat()
	for key in diskstat.keys():
		print key,'\t',diskstat[key]
	print '--------------------------------------------------'
	netstat = net_stat()
	for ifinfo in netstat:
		for key in ifinfo:
			print key,'\t',ifinfo[key]
	print '--------------------------------------------------'
