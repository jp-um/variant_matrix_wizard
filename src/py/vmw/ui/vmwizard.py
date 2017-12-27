#!/usr/bin/env python3

import wx

from wx.adv import Wizard as wiz
from wx.adv import WizardPage, WizardPageSimple
from vmw.ui.wizardpages.step0_data_files_type_selection import Step0DataFilesTypeSelection

from demo import images

def makePageTitle(wizPg, title):
    sizer = wx.BoxSizer(wx.VERTICAL)
    wizPg.SetSizer(sizer)
    title = wx.StaticText(wizPg, -1, title)
    title.SetFont(wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
    sizer.Add(title, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
    sizer.Add(wx.StaticLine(wizPg, -1), 0, wx.EXPAND|wx.ALL, 5)
    return sizer


class TitledPage(WizardPageSimple):
    def __init__(self, parent, title):
        WizardPageSimple.__init__(self, parent)
        self.sizer = makePageTitle(self, title)

class Wizard(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1)
        wizard = wiz(self, -1, "Simple Wizard", images.WizTest1.GetBitmap())
        page1 = Step0DataFilesTypeSelection(wizard)
        #page1 = TitledPage(wizard, "Page 2")
        page2 = TitledPage(wizard, "Page 2")
        self.page1 = page1

        page1.GetSizer().Add(wx.StaticText(page1, -1, """
        This wizard is totally useless, but is meant to show how to
        chain simple wizard pages together in a non-dynamic manner.
        IOW, the order of the pages never changes, and so the
        wxWizardPageSimple class can easily be used for the pages."""))
        wizard.FitToPage(page1)
        page2.sizer.Add(wx.StaticText(page2, -1, "\nThis is the last page."))

        # Use the convenience Chain function to connect the pages
        page1.SetNext(page2)

        wizard.GetPageAreaSizer().Add(page1)
        if wizard.RunWizard(page1):
            wx.MessageBox("Wizard completed successfully", "That's all folks!")
        else:
            wx.MessageBox("Wizard was cancelled", "That's all folks!")

    def test(self, b):
        print("???")
