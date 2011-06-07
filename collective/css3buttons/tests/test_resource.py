from unittest import TestSuite, makeSuite
from zope.component import getAdapter
from zope.publisher.browser import TestRequest

from collective.css3buttons.tests import base


class ResourceTestCase(base.TestCase):

    def test_0010_images(self):
        request = TestRequest()
        res = getAdapter(request, name='collective.css3buttons.images')
        self.assertNotEqual(res.get('css3buttons_backgrounds.png', None), None)
        self.assertNotEqual(res.get('css3buttons_icons.png', None), None)

    def test_0020_stylesheets(self):
        request = TestRequest()
        res = getAdapter(request, name='collective.css3buttons.stylesheets')
        self.assertNotEqual(res.get('css3buttons.css', None), None)


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(ResourceTestCase))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
