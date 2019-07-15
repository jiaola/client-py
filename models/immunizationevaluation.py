#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier

from . import domainresource

@dataclass
class ImmunizationEvaluation(domainresource.DomainResource):
    """ Immunization evaluation information.

    Describes a comparison of an immunization event against published
    recommendations to determine if the administration is "valid" in relation
    to those  recommendations.
    """
    resource_type: ClassVar[str] = "ImmunizationEvaluation"
    authority: Optional[fhirreference.FHIRReference] = None
    date: Optional[fhirdate.FHIRDate] = None
    description: Optional[str] = None
    doseNumberPositiveInt: Optional[int] = None
    doseNumberString: Optional[str] = None
    doseStatus:codeableconcept.CodeableConcept = None
    doseStatusReason: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    immunizationEvent:fhirreference.FHIRReference = None
    patient:fhirreference.FHIRReference = None
    series: Optional[str] = None
    seriesDosesPositiveInt: Optional[int] = None
    seriesDosesString: Optional[str] = None
    status: str = None
    targetDisease:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImmunizationEvaluation, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", False),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", False),
            ("doseStatus", "doseStatus", codeableconcept.CodeableConcept, False, None, True),
            ("doseStatusReason", "doseStatusReason", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("immunizationEvent", "immunizationEvent", fhirreference.FHIRReference, False, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("series", "series", str, False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("status", "status", str, False, None, True),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']