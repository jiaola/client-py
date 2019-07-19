#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/EnrollmentRequest) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class EnrollmentRequest(DomainResource):
    """ Enroll in coverage.

    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """
    resource_type: ClassVar[str] = "EnrollmentRequest"
    candidate: Optional[FHIRReference] = None
    coverage: Optional[FHIRReference] = None
    created: Optional[FHIRDate] = None
    identifier: Optional[List[Identifier]] = empty_list()
    insurer: Optional[FHIRReference] = None
    provider: Optional[FHIRReference] = None
    status: Optional[str] = None

    def elementProperties(self):
        js = super(EnrollmentRequest, self).elementProperties()
        js.extend([
            ("candidate", "candidate", FHIRReference, False, None, False),
            ("coverage", "coverage", FHIRReference, False, None, False),
            ("created", "created", FHIRDate, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("insurer", "insurer", FHIRReference, False, None, False),
            ("provider", "provider", FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
        ])
        return js