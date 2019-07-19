#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ResearchSubject) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class ResearchSubject(DomainResource):
    """ Physical entity which is the primary unit of interest in the study.

    A physical entity which is the primary unit of operational and/or
    administrative interest in a study.
    """
    resource_type: ClassVar[str] = "ResearchSubject"
    actualArm: Optional[str] = None
    assignedArm: Optional[str] = None
    consent: Optional[FHIRReference] = None
    identifier: Optional[List[Identifier]] = empty_list()
    individual: FHIRReference = None
    period: Optional[Period] = None
    status: str = None
    study: FHIRReference = None

    def elementProperties(self):
        js = super(ResearchSubject, self).elementProperties()
        js.extend([
            ("actualArm", "actualArm", str, False, None, False),
            ("assignedArm", "assignedArm", str, False, None, False),
            ("consent", "consent", FHIRReference, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("individual", "individual", FHIRReference, False, None, True),
            ("period", "period", Period, False, None, False),
            ("status", "status", str, False, None, True),
            ("study", "study", FHIRReference, False, None, True),
        ])
        return js