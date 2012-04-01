# -*- coding:utf-8 -*-

from five import grok

from Products.CMFPlone.interfaces import INonInstallable


class HiddenProfiles(grok.GlobalUtility):

    grok.implements(INonInstallable)
    grok.provides(INonInstallable)
    grok.name('collective.nitf.core')

    def getNonInstallableProfiles(self):
        profiles = ['collective.nitf.core:uninstall', ]
        return profiles
