#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CompartmentDefinition) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .usagecontext import UsageContext


@dataclass
class CompartmentDefinitionResource(BackboneElement):
    """ How a resource is related to the compartment.

    Information about how a resource is related to the compartment.
    """
    resource_type: ClassVar[str] = "CompartmentDefinitionResource"
    code: str = None
    documentation: Optional[str] = None
    param: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(CompartmentDefinitionResource, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
            ("param", "param", str, True, None, False),
        ])
        return js


@dataclass
class CompartmentDefinition(DomainResource):
    """ Compartment Definition for a resource.

    A compartment definition that defines how resources are accessed on a
    server.
    """
    resource_type: ClassVar[str] = "CompartmentDefinition"
    code: str = None
    contact: Optional[List[ContactDetail]] = empty_list()
    date: Optional[FHIRDate] = None
    description: Optional[str] = None
    experimental: Optional[bool] = None
    name: str = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    resource: Optional[List[CompartmentDefinitionResource]] = empty_list()
    search: bool = None
    status: str = None
    url: str = None
    useContext: Optional[List[UsageContext]] = empty_list()
    version: Optional[str] = None

    def elementProperties(self):
        js = super(CompartmentDefinition, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("contact", "contact", ContactDetail, True, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("name", "name", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("resource", "resource", CompartmentDefinitionResource, True, None, False),
            ("search", "search", bool, False, None, True),
            ("status", "status", str, False, None, True),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js