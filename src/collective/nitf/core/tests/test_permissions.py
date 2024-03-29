# -*- coding: utf-8 -*-

import unittest2 as unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from collective.nitf.core.testing import INTEGRATION_TESTING


class PermissionsTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        folder = self.portal['test-folder']
        folder.invokeFactory('collective.nitf.content', 'n1')
        self.n1 = folder['n1']

    def test_add_permissions(self):
        permission = 'collective.nitf: Add News Article'
        roles = self.portal.rolesOfPermission(permission)
        roles = [r['name'] for r in roles if r['selected']]
        self.assertEqual(roles, ['Contributor', 'Manager', 'Owner', 'Site Administrator'])

    # TODO: find a better way to test this
    def test_owner_permissions(self):
        # the owner can add Images, Files and Links
        # Manager is the owner in this context
        permissions = self.n1.permissionsOfRole('Manager')
        permissions = [p['name'] for p in permissions if p['selected']]
        self.assertTrue('ATContentTypes: Add Image' in permissions)
        self.assertTrue('ATContentTypes: Add File' in permissions)
        self.assertTrue('ATContentTypes: Add Link' in permissions)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
