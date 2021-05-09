import eel
import random
from datetime import datetime
import pandas as pd
import wx

eel.init('web')
errors = []


@eel.expose
def read_csv(wildcard="*",id):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    resp = ''
    path.split('/')
    print('/')
    try:
        df = pd.read_csv(path)

        df.columns
        resp = {
            "msg": "Cargado Correctamente",
            "type": "ok"}

    except:
        resp = {
            "msg": "Archivo no aceptado por favor revise que el archivo cumpla con las condiciones",
            "type": "error"}
    dialog.Destroy()
    errors.append(resp)
    return resp


@eel.expose
def run(timeawait, amountproxies):
    print(timeawait)
    print(amountproxies)
    return errors


eel.start('index.html', size=(600, 600))
