#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Population) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import range

from . import backboneelement

@dataclass
class Population(backboneelement.BackboneElement):
    """ A definition of a set of people that apply to some clinically related
    context, for example people contraindicated for a certain medication.

    A populatioof people with some set of grouping criteria.
    """
    resource_type: ClassVar[str] = "Population"
    ageCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    ageRange: Optional[range.Range] = None
    gender: Optional[codeableconcept.CodeableConcept] = None
    physiologicalCondition: Optional[codeableconcept.CodeableConcept] = None
    race: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Population, self).elementProperties()
        js.extend([
            ("ageCodeableConcept", "ageCodeableConcept", codeableconcept.CodeableConcept, False, "age", False),
            ("ageRange", "ageRange", range.Range, False, "age", False),
            ("gender", "gender", codeableconcept.CodeableConcept, False, None, False),
            ("physiologicalCondition", "physiologicalCondition", codeableconcept.CodeableConcept, False, None, False),
            ("race", "race", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']