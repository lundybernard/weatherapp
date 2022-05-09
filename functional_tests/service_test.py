from unittest import TestCase

PT_SVC_ADDR = 'http://0.0.0.0:5000/'
#PT_SVC_ADDR = 'http://127.0.0.1:5000/'

from bat.tests.common_api_tests import CommonAPITest


class ServiceFunctionalTest(TestCase, CommonAPITest):

    def setUp(t):
        CommonAPITest.setUp(t)
        t.service_address = PT_SVC_ADDR
        #t.location = 'AABP'
