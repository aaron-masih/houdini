import hou, os

fileCache = hou.selectedNodes()[0]

parm = fileCache.parm("file")

parmval = parm.rawValue()

hipPath = os.path.dirname(hou.hipFile.path())

newPath = parmval.replace("$HIP/", hipPath + "/")

parm.set(newPath)