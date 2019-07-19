#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Endpoint) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class Endpoint(DomainResource):
    """ The technical details of an endpoint that can be used for electronic
    services.

    The technical details of an endpoint that can be used for electronic
    services, such as for web services providing XDS.b or a REST endpoint for
    another FHIR server. This may include any security context information.
    """
    resource_type: ClassVar[str] = "Endpoint"
    address: str = None
    connectionType: Coding = None
    contact: Optional[List[ContactPoint]] = empty_list()
    header: Optional[List[str]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    managingOrganization: Optional[FHIRReference] = None
    name: Optional[str] = None
    payloadMimeType: Optional[List[str]] = empty_list()
    payloadType: List[CodeableConcept] = empty_list()
    period: Optional[Period] = None
    status: str = None

    def elementProperties(self):
        js = super(Endpoint, self).elementProperties()
        js.extend([
            ("address", "address", str, False, None, True),
            ("connectionType", "connectionType", Coding, False, None, True),
            ("contact", "contact", ContactPoint, True, None, False),
            ("header", "header", str, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("managingOrganization", "managingOrganization", FHIRReference, False, None, False),
            ("name", "name", str, False, None, False),
            ("payloadMimeType", "payloadMimeType", str, True, None, False),
            ("payloadType", "payloadType", CodeableConcept, True, None, True),
            ("period", "period", Period, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js