#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductContraindication) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .population import Population


@dataclass
class MedicinalProductContraindicationOtherTherapy(BackboneElement):
    """ Information about the use of the medicinal product in relation to other
    therapies described as part of the indication.
    """
    resource_type: ClassVar[str] = "MedicinalProductContraindicationOtherTherapy"
    medicationCodeableConcept: CodeableConcept = None
    medicationReference: FHIRReference = None
    therapyRelationshipType: CodeableConcept = None

    def elementProperties(self):
        js = super(MedicinalProductContraindicationOtherTherapy, self).elementProperties()
        js.extend([
            ("medicationCodeableConcept", "medicationCodeableConcept", CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", FHIRReference, False, "medication", True),
            ("therapyRelationshipType", "therapyRelationshipType", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class MedicinalProductContraindication(DomainResource):
    """ MedicinalProductContraindication.

    The clinical particulars - indications, contraindications etc. of a
    medicinal product, including for regulatory purposes.
    """
    resource_type: ClassVar[str] = "MedicinalProductContraindication"
    comorbidity: Optional[List[CodeableConcept]] = empty_list()
    disease: Optional[CodeableConcept] = None
    diseaseStatus: Optional[CodeableConcept] = None
    otherTherapy: Optional[List[MedicinalProductContraindicationOtherTherapy]] = empty_list()
    population: Optional[List[Population]] = empty_list()
    subject: Optional[List[FHIRReference]] = empty_list()
    therapeuticIndication: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(MedicinalProductContraindication, self).elementProperties()
        js.extend([
            ("comorbidity", "comorbidity", CodeableConcept, True, None, False),
            ("disease", "disease", CodeableConcept, False, None, False),
            ("diseaseStatus", "diseaseStatus", CodeableConcept, False, None, False),
            ("otherTherapy", "otherTherapy", MedicinalProductContraindicationOtherTherapy, True, None, False),
            ("population", "population", Population, True, None, False),
            ("subject", "subject", FHIRReference, True, None, False),
            ("therapeuticIndication", "therapeuticIndication", FHIRReference, True, None, False),
        ])
        return js