#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductUndesirableEffect) on 2019-07-22.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .population import Population


@dataclass
class MedicinalProductUndesirableEffect(DomainResource):
    """ MedicinalProductUndesirableEffect.

    Describe the undesirable effects of the medicinal product.
    """
    resource_type: ClassVar[str] = "MedicinalProductUndesirableEffect"
    subject: Optional[List[FHIRReference]] = empty_list()
    symptomConditionEffect: Optional[CodeableConcept] = None
    classification: Optional[CodeableConcept] = None
    frequencyOfOccurrence: Optional[CodeableConcept] = None
    population: Optional[List[Population]] = empty_list()

    def elementProperties(self):
        js = super(MedicinalProductUndesirableEffect, self).elementProperties()
        js.extend([
            ("subject", "subject", FHIRReference, True, None, False),
            ("symptomConditionEffect", "symptomConditionEffect", CodeableConcept, False, None, False),
            ("classification", "classification", CodeableConcept, False, None, False),
            ("frequencyOfOccurrence", "frequencyOfOccurrence", CodeableConcept, False, None, False),
            ("population", "population", Population, True, None, False),
        ])
        return js