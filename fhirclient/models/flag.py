#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Flag) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class Flag(DomainResource):
    """ Key information to flag to healthcare providers.

    Prospective warnings of potential issues when providing care to the
    patient.
    """
    resource_type: ClassVar[str] = "Flag"
    author: Optional[FHIRReference] = None
    category: Optional[List[CodeableConcept]] = empty_list()
    code: CodeableConcept = None
    encounter: Optional[FHIRReference] = None
    identifier: Optional[List[Identifier]] = empty_list()
    period: Optional[Period] = None
    status: str = None
    subject: FHIRReference = None

    def elementProperties(self):
        js = super(Flag, self).elementProperties()
        js.extend([
            ("author", "author", FHIRReference, False, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("code", "code", CodeableConcept, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("period", "period", Period, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, True),
        ])
        return js