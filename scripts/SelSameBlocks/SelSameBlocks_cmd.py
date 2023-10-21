"""
@name:          SelSameBlocks
@description:   Selects alle the blocks with the same definition as the selected blocks.
@author:        Ejnar Brendsdal
@version:       1.3cn
@link:          https://github.com/ejnaren/rhinotools
@notes:         Works with Rhino 7.


@license:

The MIT License (MIT)

Copyright (c) 2016 Ejnar Brendsdal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


@Installation: Copy to the Rhino script folder. ie.: C:\Users\"USER"\AppData\Roaming\McNeel\Rhinoceros\7.0\scripts
                Options to use the function:
                1. Recommended: Import the bundled "Block Tools" toolbar with readymade buttons to call the functions.
                2. Add a new button with the following macro: ( _NoEcho !-_RunPythonScript "SelectSameBlocks.py" _Echo )
                3. Add an alias with the above command
                3. Call the script directly by using this command: "-RunPythonScript SelectSameBlocks.py"

@Changelog:
    1.1:    Make script into a command to be included in the BlockTools part of RhinoTools
            Name change to "SelSameBlocks" to conform to Rhino standard
    1.3: Unify version numbers and small redraw optimization.
"""

#******* Imports ********************
#************************************

#coding=utf-8

import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino.Geometry as G

#******* Main function ********************
#******************************************

def RunCommand( is_interactive ):
    if sc.escape_test(False):
        print "操作已取消" #do something

    print "正在选取相同父本的图块"

    #******* Get blocks *****************
    #************************************

    objectIds = rs.GetObjects("选取要操作的图块", 4096, preselect=True)
    if not objectIds:
        print "没有选取物件"
        return False


    #pause viewport redraw
    rs.EnableRedraw(False)

    #******* Sort blocks by Name ********
    #************************************
    blockNames = []
    for id in objectIds:
        blockName = rs.BlockInstanceName(id)
        if blockName not in blockNames:
            blockNames.append(blockName)

    #******* Get block instances by name ********
    #********************************************
    selIds = []
    for name in blockNames:
        blockIds = rs.BlockInstances(name)
        selIds.extend(blockIds)

    #******* Select blocks **************
    #************************************
    rs.SelectObjects(selIds)

    rs.EnableRedraw(True)

    print "操作已完成"
    #End RunCommand()

    #end sane
    return 0

RunCommand(True) #Run script
