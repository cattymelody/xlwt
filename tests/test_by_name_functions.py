#!/usr/bin/env python
# coding:utf-8
# Author:  Fabio --<fabio_ferreiradasilva@yahoo.com.br>
# Purpose: test functions by sheet name
# Created: 30.07.2014

import unittest
import xlwt

class TestByName(unittest.TestCase):
    def setUp(self):
        self.wb = xlwt.Workbook()
        self.wb.add_sheet('Plan1')    
        self.wb.add_sheet('Plan2')
        self.wb.add_sheet('Plan3')
        self.wb.add_sheet('Plan4')

    def test_sheet_index(self):
        'Return sheet index by sheet name'
        idx = self.wb.sheet_index('Plan3')
        self.assertEqual(2, idx)

    def test_get_by_name(self):
        'Get sheet by name'
        ws = self.wb.get_sheet(1)
        self.assertEqual('Plan2', ws.name)
    
    def test_get_by_index(self):
        'Get sheet by index'
        ws = self.wb.get_sheet('Plan2')
        self.assertEqual('Plan2', ws.name)
    
    def test_invalid_sheet_parameter(self):
        'Raises exception when sheet is not string or integer'
        try:
            self.wb.get_sheet(1.1)
        except Exception, e:
            self.assertTrue('sheet must be integer or string', e)
        else:
            self.fail('exception not raised')

if __name__=='__main__':
    unittest.main()
