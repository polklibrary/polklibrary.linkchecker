# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import polklibrary.linkchecker


class PolklibraryLinkcheckerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=polklibrary.linkchecker)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'polklibrary.linkchecker:default')


POLKLIBRARY_LINKCHECKER_FIXTURE = PolklibraryLinkcheckerLayer()


POLKLIBRARY_LINKCHECKER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(POLKLIBRARY_LINKCHECKER_FIXTURE,),
    name='PolklibraryLinkcheckerLayer:IntegrationTesting',
)


POLKLIBRARY_LINKCHECKER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(POLKLIBRARY_LINKCHECKER_FIXTURE,),
    name='PolklibraryLinkcheckerLayer:FunctionalTesting',
)


POLKLIBRARY_LINKCHECKER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        POLKLIBRARY_LINKCHECKER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PolklibraryLinkcheckerLayer:AcceptanceTesting',
)
