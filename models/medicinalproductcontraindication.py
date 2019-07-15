#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductContraindication) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirreference
from . import population

from . import domainresource

@dataclass
class MedicinalProductContraindication(domainresource.DomainResource):
    """ MedicinalProductContraindication.

    The clinical particulars - indications, contraindications etc. of a
    medicinal product, including for regulatory purposes.
    """
    resource_type: ClassVar[str] = "MedicinalProductContraindication"
    comorbidity: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    disease: Optional[codeableconcept.CodeableConcept] = None
    diseaseStatus: Optional[codeableconcept.CodeableConcept] = None
    otherTherapy: Optional[List[MedicinalProductContraindicationOtherTherapy]] = empty_list()
    population: Optional[List[population.Population]] = empty_list()
    subject: Optional[List[fhirreference.FHIRReference]] = empty_list()
    therapeuticIndication: Optional[List[fhirreference.FHIRReference]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductContraindication, self).elementProperties()
        js.extend([
            ("comorbidity", "comorbidity", codeableconcept.CodeableConcept, True, None, False),
            ("disease", "disease", codeableconcept.CodeableConcept, False, None, False),
            ("diseaseStatus", "diseaseStatus", codeableconcept.CodeableConcept, False, None, False),
            ("otherTherapy", "otherTherapy", MedicinalProductContraindicationOtherTherapy, True, None, False),
            ("population", "population", population.Population, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("therapeuticIndication", "therapeuticIndication", fhirreference.FHIRReference, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class MedicinalProductContraindicationOtherTherapy(backboneelement.BackboneElement):
    """ Information about the use of the medicinal product in relation to other
    therapies described as part of the indication.
    """
    resource_type: ClassVar[str] = "MedicinalProductContraindicationOtherTherapy"
    medicationCodeableConcept:codeableconcept.CodeableConcept = None
    medicationReference:fhirreference.FHIRReference = None
    therapyRelationshipType:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductContraindicationOtherTherapy, self).elementProperties()
        js.extend([
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("therapyRelationshipType", "therapyRelationshipType", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import population
except ImportError:
    population = sys.modules[__package__ + '.population']