#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MetadataResource) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .usagecontext import UsageContext


@dataclass
class MetadataResource(DomainResource):
    """ Common Ancestor declaration for definitional resources.

    Common Ancestor declaration for conformance and knowledge artifact
    resources.
    """
    resource_type: ClassVar[str] = "MetadataResource"
    contact: Optional[List[ContactDetail]] = empty_list()
    date: Optional[FHIRDate] = None
    description: Optional[str] = None
    experimental: Optional[bool] = None
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    name: Optional[str] = None
    publisher: Optional[str] = None
    status: str = None
    title: Optional[str] = None
    url: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    version: Optional[str] = None

    def elementProperties(self):
        js = super(MetadataResource, self).elementProperties()
        js.extend([
            ("contact", "contact", ContactDetail, True, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js