import hou

# selected lights

lgts = hou.selectedNodes()

# calculate how many lights in the list

lgt_num = len(lgts)

# for each light add category number

count = -1

for each in lgts:
    cat = each.parm("categories")
    count += 1
    intval = str(count)
    cat.set(intval)
    name = each.name()
    print(name)

#-----------------------------------------------------------------------

# calculate how many image planes exist in the selected mantra node

for mantra in hou.selectedNodes():
    extraImagePlanes = mantra.parm("vm_numaux")
    value = extraImagePlanes.eval()
    valueint = int(value)
    print(valueint)


total = (value + lgt_num * 4)



total_lgtPlanes = (lgt_num * 4)

print(total_lgtPlanes)


# set new number of image planes 


extraImagePlanes.set(total)


# set vex variable for new image planes

all_vexVar = []
new_vexVar = []

for v in mantra.parms():
        vt = v.name()
        if "vm_variable_plane" in vt:
            all_vexVar.append(v)

for vp in all_vexVar[valueint: ]:
    new_vexVar.append(vp)

for d in new_vexVar[0::4]:
    d.set("direct")

for dc in new_vexVar[1::4]:
    dc.set("direct_comp")

for i in new_vexVar[2::4]:
    i.set("indirect")

for ic in new_vexVar[3::4]:
    ic.set("indirect_comp")


#-----------------------------------------------------------------------

lightName = []

for each in lgts:
    name = each.name()
    print(name)
    lightName.append(name)

# set vex variable for new image planes - collect all channel name parameters

channelName = []
new_cn = []

for v in mantra.parms():
        vt = v.name()
        if "vm_channel_plane" in vt:
        	channelName.append(v)

print(channelName)

# for loops appending channel names for direct, indirect, direct_comp and indirect_comp image planes
# naming convention starts with a underscore, followed by the lights name, then pass type

for cn in channelName[valueint: ]:
	new_cn.append(cn)

direct_count = -1
directcomp_count = -1
indirect_count = -1
indirectcomp_count = -1

for n in new_cn[::4]:
    direct_count += 1
    n.set("_" + lightName[direct_count] + "_direct")

for n in new_cn[1::4]:
    directcomp_count += 1
    n.set("_" + lightName[directcomp_count] + "_direct")

for n in new_cn[2::4]:
    indirect_count += 1
    n.set("_" + lightName[indirect_count] + "_indirect")

for n in new_cn[3::4]:
    indirectcomp_count += 1
    n.set("_" + lightName[indirectcomp_count] + "_indirect")


#-----------------------------------------------------------------------

# turning on component export for all the _comp passes

ev_grp = []

for v in mantra.parms():
    evName = v.name()
    if "vm_componentexport" in evName:
        ev_grp.append(v)

print(ev_grp)

for n in ev_grp[valueint + 1::2]:
    n.set(1)

#-----------------------------------------------------------------------

le_all = []

for v in mantra.parms():
    leName = v.name()
    if "vm_lightexport" in leName:
        le_all.append(v)

le_grp = []
for n in le_all[::3]:
    le_grp.append(n)

print(le_grp)

# creating lists for the light export settings


le_scope = []
for scope in le_all:
    scopeN = scope.name()
    if "vm_lightexport_scope" in scopeN:
        le_scope.append(scope)

le_select = []
for select in le_all:
    selectN = select.name()
    if "vm_lightexport_select" in selectN:
        le_select.append(select)

print(le_select)

# setting the parameters for the light export settings

for p in le_grp[valueint::1]:
    p.set("2")

for p in le_scope[valueint + 1::1]:
    p.set("*")


selectD_count = -1
selectDc_count = -1
selectI_count = -1
selectIc_count = -1

for p in le_select[valueint::4]:
    selectD_count += 1
    selectD_count_str = str(selectD_count)
    p.set(selectD_count_str)

for p in le_select[valueint + 1::4]:
    selectDc_count += 1
    selectDc_count_str = str(selectDc_count)
    p.set(selectDc_count_str)

for p in le_select[valueint + 2::4]:
    selectI_count += 1
    selectI_count_str = str(selectI_count)
    p.set(selectI_count_str)

for p in le_select[valueint + 3::4]:
    selectIc_count += 1
    selectIc_count_str = str(selectIc_count)
    p.set(selectIc_count_str)

#-----------------------------------------------------------------------

