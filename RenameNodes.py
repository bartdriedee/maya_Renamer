from maya import cmds

class RenamerWin(object):
    def __init__(self):
	    if(cmds.window('window1_ui',q=True,ex=True)):cmds.deleteUI('window1_ui')
	    if(cmds.windowPref('window1_ui',ex=1)):cmds.windowPref('window1_ui',r=1)
	    cmds.window('window1_ui',tlc=[466L, 853L],t=u'Renamer',tlb=True)
	    cmds.columnLayout('columnLayout1_ui',en=True)
	    cmds.textFieldGrp('textFieldButtonGrp1_ui',en=True,tx=u'type new name here',cc=(self.doRename))
	    cmds.showWindow('window1_ui')


    def doRename(self,newName):
        selection = cmds.ls(sl=True, long=True);
        selection.sort(key=lambda a: a.count("|"), reverse=True)

        for index in range(0,len(selection)):
            print selection[index]
            cmds.rename (selection[index], (newName + str(len(selection)-index)))
        print (str(len(selection)) + " nodes renamed to " + newName+"\n");