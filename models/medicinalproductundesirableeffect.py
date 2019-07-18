#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductUndesirableEffect) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import domainresource
from . import fhirreference
from . import population

from . import domainresource

@dataclass
class MedicinalProductUndesirableEffect(domainresource.DomainResource):
    """ MedicinalProductUndesirableEffect.

    Describe the undesirable effects of the medicinal product.
    """
    resource_type: ClassVar[str] = "MedicinalProductUndesirableEffect"
    classification: Optional[codeableconcept.CodeableConcept] = None
    frequencyOfOccurrence: Optional[codeableconcept.CodeableConcept] = None
    population: Optional[List[population.Population]] = empty_list()
    subject: Optional[List[fhirreference.FHIRReference]] = empty_list()
    symptomConditionEffect: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductUndesirableEffect, self).elementProperties()
        js.extend([
            ("classification", "classification", codeableconcept.CodeableConcept, False, None, False),
            ("frequencyOfOccurrence", "frequencyOfOccurrence", codeableconcept.CodeableConcept, False, None, False),
            ("population", "population", population.Population, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("symptomConditionEffect", "symptomConditionEffect", codeableconcept.CodeableConcept, False, None, False),
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