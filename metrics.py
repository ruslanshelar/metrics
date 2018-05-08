import psutil
import sys

if len(sys.argv) <= 1:
	print("Enter param 'cpu' or 'mem' to get metrics")
	quit()

if sys.argv[1]  == "cpu":
	cpu = psutil.cpu_times()
	systemCpu = "system.cpu."
	idle = "idel " + str(cpu.idle)
	user = "user " + str(cpu.user)
	guest = "guest " + str(cpu.guest)
	iowait = "iowait " + str(cpu.iowait)
	stolen = "stolen " + str(cpu.steal)
	system = "system " + str(cpu.system)
	cpuArray = [idle, user, guest, iowait, stolen, system]
	for x in cpuArray:
		print(systemCpu +x)

if sys.argv[1] == "mem":
	mem = psutil.virtual_memory()
	swap = psutil.swap_memory()
	virtualStr = "virtual "
	swapStr = "swap "
	vtotal = "total " + str(mem.total)
	vused = "used " + str(mem.used)
	vfree = "free " + str(mem.free)
	vshared = "shared " + str(mem.shared)
	virtualArray = [vtotal, vused, vfree, vshared]
	stotal = "total " + str(swap.total)
	sused = "used " + str(swap.used)
	sfree = "free " + str(swap.free)
	swapArray = [stotal ,sused, sfree]
	for x in virtualArray:
		print(virtualStr + x)
	for x in swapArray:
		print(swapStr + x)

if sys.argv[1] != "mem" and sys.argv[1] != "cpu":
	print("No such argument") 
