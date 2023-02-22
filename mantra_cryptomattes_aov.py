import hou

for mantra in hou.selectedNodes():
	cryptomatte = mantra.parm("vm_cryptolayers")
	cryptomatte.set("2")
	property1 = mantra.parm("vm_cryptolayerprop1")
	property1.set("materialname")
	channel1 = mantra.parm("vm_cryptolayername1")
	channel1.set("CryptoMaterial")
	property2 = mantra.parm("vm_cryptolayerprop2")
	property2.set("name")
	channel2 = mantra.parm("vm_cryptolayername2")
	channel2.set("CryptoObject")
