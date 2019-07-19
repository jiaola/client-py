#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Basic) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class Basic(DomainResource):
    """ Resource for non-supported content.

    Basic is used for handling concepts not yet defined in FHIR, narrative-only
    resources that don't map to an existing resource, and custom resources not
    appropriate for inclusion in the FHIR specification.
    """
    resource_type: ClassVar[str] = "Basic"
    author: Optional[FHIRReference] = None
    code: CodeableConcept = None
    created: Optional[FHIRDate] = None
    identifier: Optional[List[Identifier]] = empty_list()
    subject: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(Basic, self).elementProperties()
        js.extend([
            ("author", "author", FHIRReference, False, None, False),
            ("code", "code", CodeableConcept, False, None, True),
            ("created", "created", FHIRDate, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("subject", "subject", FHIRReference, False, None, False),
        ])
        return js