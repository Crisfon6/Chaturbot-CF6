import eel
import random
from datetime import datetime
import pandas as pd
import wx

eel.init('web')

@eel.expose
def add(proxies,models,credentials):
    print(proxies)
    
    return 3

@eel.expose
def pythonFunction(wildcard="*"):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path

eel.start('index.html' ,size=(600, 600))