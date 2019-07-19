#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/EnrollmentResponse) on 2019-07-18.
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
class EnrollmentResponse(DomainResource):
    """ EnrollmentResponse resource.

    This resource provides enrollment and plan details from the processing of
    an EnrollmentRequest resource.
    """
    resource_type: ClassVar[str] = "EnrollmentResponse"
    created: Optional[FHIRDate] = None
    disposition: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    organization: Optional[FHIRReference] = None
    outcome: Optional[str] = None
    request: Optional[FHIRReference] = None
    requestProvider: Optional[FHIRReference] = None
    status: Optional[str] = None

    def elementProperties(self):
        js = super(EnrollmentResponse, self).elementProperties()
        js.extend([
            ("created", "created", FHIRDate, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("organization", "organization", FHIRReference, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("request", "request", FHIRReference, False, None, False),
            ("requestProvider", "requestProvider", FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
        ])
        return js