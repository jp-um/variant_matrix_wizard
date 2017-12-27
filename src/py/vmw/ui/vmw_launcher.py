#!/usr/bin/env python3

import wx

import vmwizard as vmw


if __name__ == '__main__':
    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, "Variant Matrix")
    wiz = vmw.Wizard(frame)
    frame.Show(True)
    frame.Centre()
    app.MainLoop()

