#!/usr/bin/env python
# this a short metrics stats of sysytem
import psutil as ps
import argparse as arg
import sys

usage = arg.ArgumentParser(description='EXAMPLE USAGE:')
usage.add_argument('arg', action='store', help='Please please write argument "mem","cpu" or "all" e.g.: ./metric cpu')
if len(sys.argv)==1:
    usage.print_help(sys.stderr)
    sys.exit(1)
value = vars(usage.parse_args())
def cpu():
  load = ps.cpu_percent(interval=1)
  load_per_core = ps.cpu_percent(interval=1, percpu=True)
  load_common = ps.cpu_times_percent(interval=1, percpu=False)
  cpu_core = ps.cpu_count(logical=False)
  cpu_logical_core = ps.cpu_count()
# print information
  print "You machine have phisical cores : ", cpu_core
  print "Logical cores :", cpu_logical_core
  print "Avarage load(%) :", load
  print "Load per core(%) :", load_per_core
  print "Common load(%) :", load_common 

def mem():
 mem = ps.virtual_memory()
 total = mem.total >> 30
 avail = mem.available >> 30
 used  = mem.used >> 30
 perc = mem.percent
 swap = ps.swap_memory()
 swtotal = swap.total >> 30
 swused = swap.used >> 30
 swfree = swap.free >> 30
 swperc = swap.percent
 print "Available(GB) :", avail
 print "Total(GB) :", total
 print "Used(GB) :", used
 print "In percent :", perc
 print "Swap total(GB) :", swtotal
 print "Used swap(GB) :", swused
 print "Free (GB) :", swfree
 print "Swap in % :", swperc

if value['arg'] == 'cpu':
 cpu()
elif value['arg'] == 'mem':
 mem()
elif value['arg'] == 'all':
 print "*** CPU ***"
 cpu()
 print "*** Memory ***"
 mem ()
else:
 print "try ran script with -h flag"
 sys.exit(1)
