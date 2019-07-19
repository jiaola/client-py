#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/GraphDefinition) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .usagecontext import UsageContext


@dataclass
class GraphDefinitionLinkTargetCompartment(BackboneElement):
    """ Compartment Consistency Rules.
    """
    resource_type: ClassVar[str] = "GraphDefinitionLinkTargetCompartment"
    code: str = None
    description: Optional[str] = None
    expression: Optional[str] = None
    rule: str = None
    use: str = None

    def elementProperties(self):
        js = super(GraphDefinitionLinkTargetCompartment, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("rule", "rule", str, False, None, True),
            ("use", "use", str, False, None, True),
        ])
        return js


@dataclass
class GraphDefinitionLinkTarget(BackboneElement):
    """ Potential target for the link.
    """
    resource_type: ClassVar[str] = "GraphDefinitionLinkTarget"
    compartment: Optional[List[GraphDefinitionLinkTargetCompartment]] = empty_list()
    link: Optional[List[GraphDefinitionLink]] = empty_list()
    params: Optional[str] = None
    profile: Optional[str] = None
    type: str = None

    def elementProperties(self):
        js = super(GraphDefinitionLinkTarget, self).elementProperties()
        js.extend([
            ("compartment", "compartment", GraphDefinitionLinkTargetCompartment, True, None, False),
            ("link", "link", GraphDefinitionLink, True, None, False),
            ("params", "params", str, False, None, False),
            ("profile", "profile", str, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


@dataclass
class GraphDefinitionLink(BackboneElement):
    """ Links this graph makes rules about.
    """
    resource_type: ClassVar[str] = "GraphDefinitionLink"
    description: Optional[str] = None
    max: Optional[str] = None
    min: Optional[int] = None
    path: Optional[str] = None
    sliceName: Optional[str] = None
    target: Optional[List[GraphDefinitionLinkTarget]] = empty_list()

    def elementProperties(self):
        js = super(GraphDefinitionLink, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("max", "max", str, False, None, False),
            ("min", "min", int, False, None, False),
            ("path", "path", str, False, None, False),
            ("sliceName", "sliceName", str, False, None, False),
            ("target", "target", GraphDefinitionLinkTarget, True, None, False),
        ])
        return js


@dataclass
class GraphDefinition(DomainResource):
    """ Definition of a graph of resources.

    A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references. The
    Graph Definition resource defines a set and makes rules about the set.
    """
    resource_type: ClassVar[str] = "GraphDefinition"
    contact: Optional[List[ContactDetail]] = empty_list()
    date: Optional[FHIRDate] = None
    description: Optional[str] = None
    experimental: Optional[bool] = None
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    link: Optional[List[GraphDefinitionLink]] = empty_list()
    name: str = None
    profile: Optional[str] = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    start: str = None
    status: str = None
    url: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    version: Optional[str] = None

    def elementProperties(self):
        js = super(GraphDefinition, self).elementProperties()
        js.extend([
            ("contact", "contact", ContactDetail, True, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("link", "link", GraphDefinitionLink, True, None, False),
            ("name", "name", str, False, None, True),
            ("profile", "profile", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("start", "start", str, False, None, True),
            ("status", "status", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js