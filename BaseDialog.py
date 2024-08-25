# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class BaseDialog
###########################################################################

class BaseDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"SHB PY GUI Keyboard Sound", pos = wx.DefaultPosition, size = wx.Size( 317,368 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBoxRandomize = wx.CheckBox( self, wx.ID_ANY, u"Randomize?", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_checkBoxRandomize, 0, wx.ALL, 5 )

		self.m_buttonStartStop = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonStartStop.SetMinSize( wx.Size( 9999,-1 ) )

		bSizer2.Add( self.m_buttonStartStop, 0, wx.ALL, 5 )

		self.m_buttonClearList = wx.Button( self, wx.ID_ANY, u"ClearList", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonClearList.SetMinSize( wx.Size( 9999,-1 ) )

		bSizer2.Add( self.m_buttonClearList, 0, wx.ALL, 5 )

		self.m_buttonAddSoundWAV = wx.Button( self, wx.ID_ANY, u"Add Sound WAV", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonAddSoundWAV.SetMinSize( wx.Size( 9999,-1 ) )

		bSizer2.Add( self.m_buttonAddSoundWAV, 0, wx.ALL, 5 )

		m_listBoxSoundWAVChoices = []
		self.m_listBoxSoundWAV = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxSoundWAVChoices, 0 )
		self.m_listBoxSoundWAV.SetMinSize( wx.Size( 9999,9999 ) )

		bSizer2.Add( self.m_listBoxSoundWAV, 0, wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


