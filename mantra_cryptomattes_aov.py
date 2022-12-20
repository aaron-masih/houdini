import hou

for mantra in hou.selectedNodes():
	cryptomatte = mantra.parm("vm_cryptolayers")
	cryptomatte.set("2")
	property2 = mantra.parm("vm_cryptolayerprop2")
	property2.set("name")
	channel2 = mantra.parm("vm_cryptolayername2")
	channel2.set("CryptoObject")