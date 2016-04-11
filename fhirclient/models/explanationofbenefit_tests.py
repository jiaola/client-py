#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 on 2016-04-01.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import explanationofbenefit
from .fhirdate import FHIRDate


class ExplanationOfBenefitTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ExplanationOfBenefit", js["resourceType"])
        return explanationofbenefit.ExplanationOfBenefit(js)
    
    def testExplanationOfBenefit1(self):
        inst = self.instantiate_from("explanationofbenefit-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ExplanationOfBenefit instance")
        self.implExplanationOfBenefit1(inst)
        
        js = inst.as_json()
        self.assertEqual("ExplanationOfBenefit", js["resourceType"])
        inst2 = explanationofbenefit.ExplanationOfBenefit(js)
        self.implExplanationOfBenefit1(inst2)
    
    def implExplanationOfBenefit1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Claim settled as per contract.")
        self.assertEqual(inst.id, "EB3500")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/explanationofbenefit")
        self.assertEqual(inst.identifier[0].value, "987654321")
        self.assertEqual(inst.item[0].adjudication[0].amount.code, "USD")
        self.assertEqual(inst.item[0].adjudication[0].amount.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].adjudication[0].amount.value, 120.0)
        self.assertEqual(inst.item[0].adjudication[0].category.code, "eligible")
        self.assertEqual(inst.item[0].adjudication[1].category.code, "eligpercent")
        self.assertEqual(inst.item[0].adjudication[1].value, 0.8)
        self.assertEqual(inst.item[0].adjudication[2].amount.code, "USD")
        self.assertEqual(inst.item[0].adjudication[2].amount.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].adjudication[2].amount.value, 96.0)
        self.assertEqual(inst.item[0].adjudication[2].category.code, "benefit")
        self.assertEqual(inst.item[0].net.code, "USD")
        self.assertEqual(inst.item[0].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].net.value, 135.57)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(inst.item[0].service.code, "1200")
        self.assertEqual(inst.item[0].service.system, "http://hl7.org/fhir/service-uscls")
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(inst.item[0].type.code, "service")
        self.assertEqual(inst.item[0].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].unitPrice.value, 135.57)
        self.assertEqual(inst.text.div, "<div>A human-readable rendering of the ExplanationOfBenefit</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.totalBenefit.code, "USD")
        self.assertEqual(inst.totalBenefit.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.totalBenefit.value, 96.0)
        self.assertEqual(inst.totalCost.code, "USD")
        self.assertEqual(inst.totalCost.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.totalCost.value, 135.57)
