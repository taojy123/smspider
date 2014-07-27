#Boa:Frame:Frame1

import wx
import threading
from core import get_rnum

mself = None

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, 
 wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, wxID_FRAME1TEXTCTRL3, 
 wxID_FRAME1TEXTCTRL4, 
] = [wx.NewId() for _init_ctrls in range(11)]



class SpiderThread(threading.Thread):
    def run(self):
        global mself
        mself.textCtrl2.SetValue("")
        mobiles = mself.textCtrl1.GetValue()
        startdate = mself.textCtrl3.GetValue()
        enddate = mself.textCtrl4.GetValue()
        mobiles = mobiles.split("\n")[:10]
        for mobile in mobiles:
            try:
                rnum = get_rnum(mobile, startdate, enddate)
                mself.textCtrl2.SetValue(mself.textCtrl2.GetValue() + "%s : %s \n" % (mobile, rnum))
            except:
                print "Error", mobile
        
        
class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(248, 97), size=wx.Size(763, 507),
              style=wx.DEFAULT_FRAME_STYLE, title='Smspider')
        self.SetClientSize(wx.Size(747, 469))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(747, 469),
              style=wx.TAB_TRAVERSAL)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(32, 56), size=wx.Size(152, 384),
              style=wx.TE_MULTILINE,
              value='13670349173\n13623023755\n13727691350\n15815199893\n15989807252\n15815226705\n13790878291\n15018814894\n15018351675')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self.panel1, pos=wx.Point(368, 56), size=wx.Size(344, 384),
              style=wx.TE_MULTILINE, value='')

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self.panel1, pos=wx.Point(216, 64), size=wx.Size(112, 22),
              style=0, value='2014/07/27')

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL4, name='textCtrl4',
              parent=self.panel1, pos=wx.Point(216, 168), size=wx.Size(112, 22),
              style=0, value='2014/07/28')

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='\xbf\xaa\xca\xbc\xca\xb1\xbc\xe4', name='staticText1',
              parent=self.panel1, pos=wx.Point(248, 32), size=wx.Size(48, 14),
              style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='\xbd\xe1\xca\xf8\xca\xb1\xbc\xe4', name='staticText2',
              parent=self.panel1, pos=wx.Point(248, 136), size=wx.Size(48, 14),
              style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='\xc7\xeb\xca\xe4\xc8\xeb\xca\xd6\xbb\xfa\xba\xc5\xc1\xd0\xb1\xed',
              name='staticText3', parent=self.panel1, pos=wx.Point(56, 32),
              size=wx.Size(96, 14), style=0)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label='\xbf\xaa\xca\xbc', name='button1', parent=self.panel1,
              pos=wx.Point(232, 360), size=wx.Size(88, 72), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label='\xca\xe4\xb3\xf6\xbd\xe1\xb9\xfb', name='staticText4',
              parent=self.panel1, pos=wx.Point(464, 32), size=wx.Size(48, 14),
              style=0)

    def __init__(self, parent):
        global mself
        mself = self
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        SpiderThread().start()
        event.Skip()
