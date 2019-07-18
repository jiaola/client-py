#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductIndication) on 2019-07-18.
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
from . import quantity

from . import backboneelement

@dataclass
class MedicinalProductIndicationOtherTherapy(backboneelement.BackboneElement):
    """ Information about the use of the medicinal product in relation to other
    therapies described as part of the indication.
    """
    resource_type: ClassVar[str] = "MedicinalProductIndicationOtherTherapy"
    medicationCodeableConcept:codeableconcept.CodeableConcept = None
    medicationReference:fhirreference.FHIRReference = None
    therapyRelationshipType:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductIndicationOtherTherapy, self).elementProperties()
        js.extend([
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("therapyRelationshipType", "therapyRelationshipType", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

from . import domainresource

@dataclass
class MedicinalProductIndication(domainresource.DomainResource):
    """ MedicinalProductIndication.

    Indication for the Medicinal Product.
    """
    resource_type: ClassVar[str] = "MedicinalProductIndication"
    comorbidity: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    diseaseStatus: Optional[codeableconcept.CodeableConcept] = None
    diseaseSymptomProcedure: Optional[codeableconcept.CodeableConcept] = None
    duration: Optional[quantity.Quantity] = None
    intendedEffect: Optional[codeableconcept.CodeableConcept] = None
    otherTherapy: Optional[List[MedicinalProductIndicationOtherTherapy]] = empty_list()
    population: Optional[List[population.Population]] = empty_list()
    subject: Optional[List[fhirreference.FHIRReference]] = empty_list()
    undesirableEffect: Optional[List[fhirreference.FHIRReference]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductIndication, self).elementProperties()
        js.extend([
            ("comorbidity", "comorbidity", codeableconcept.CodeableConcept, True, None, False),
            ("diseaseStatus", "diseaseStatus", codeableconcept.CodeableConcept, False, None, False),
            ("diseaseSymptomProcedure", "diseaseSymptomProcedure", codeableconcept.CodeableConcept, False, None, False),
            ("duration", "duration", quantity.Quantity, False, None, False),
            ("intendedEffect", "intendedEffect", codeableconcept.CodeableConcept, False, None, False),
            ("otherTherapy", "otherTherapy", MedicinalProductIndicationOtherTherapy, True, None, False),
            ("population", "population", population.Population, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("undesirableEffect", "undesirableEffect", fhirreference.FHIRReference, True, None, False),
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
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']