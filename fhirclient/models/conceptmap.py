#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ConceptMap) on 2019-07-18.
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
from .identifier import Identifier
from .usagecontext import UsageContext


@dataclass
class ConceptMapGroupUnmapped(BackboneElement):
    """ What to do when there is no mapping for the source concept.

    What to do when there is no mapping for the source concept. "Unmapped" does
    not include codes that are unmatched, and the unmapped element is ignored
    in a code is specified to have equivalence = unmatched.
    """
    resource_type: ClassVar[str] = "ConceptMapGroupUnmapped"
    code: Optional[str] = None
    display: Optional[str] = None
    mode: str = None
    url: Optional[str] = None

    def elementProperties(self):
        js = super(ConceptMapGroupUnmapped, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("url", "url", str, False, None, False),
        ])
        return js


@dataclass
class ConceptMapGroupElementTargetDependsOn(BackboneElement):
    """ Other elements required for this mapping (from context).

    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified element can be resolved, and it has the
    specified value.
    """
    resource_type: ClassVar[str] = "ConceptMapGroupElementTargetDependsOn"
    display: Optional[str] = None
    property: str = None
    system: Optional[str] = None
    value: str = None

    def elementProperties(self):
        js = super(ConceptMapGroupElementTargetDependsOn, self).elementProperties()
        js.extend([
            ("display", "display", str, False, None, False),
            ("property", "property", str, False, None, True),
            ("system", "system", str, False, None, False),
            ("value", "value", str, False, None, True),
        ])
        return js


@dataclass
class ConceptMapGroupElementTarget(BackboneElement):
    """ Concept in target system for element.

    A concept from the target value set that this concept maps to.
    """
    resource_type: ClassVar[str] = "ConceptMapGroupElementTarget"
    code: Optional[str] = None
    comment: Optional[str] = None
    dependsOn: Optional[List[ConceptMapGroupElementTargetDependsOn]] = empty_list()
    display: Optional[str] = None
    equivalence: str = None
    product: Optional[List[ConceptMapGroupElementTargetDependsOn]] = empty_list()

    def elementProperties(self):
        js = super(ConceptMapGroupElementTarget, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("dependsOn", "dependsOn", ConceptMapGroupElementTargetDependsOn, True, None, False),
            ("display", "display", str, False, None, False),
            ("equivalence", "equivalence", str, False, None, True),
            ("product", "product", ConceptMapGroupElementTargetDependsOn, True, None, False),
        ])
        return js


@dataclass
class ConceptMapGroupElement(BackboneElement):
    """ Mappings for a concept from the source set.

    Mappings for an individual concept in the source to one or more concepts in
    the target.
    """
    resource_type: ClassVar[str] = "ConceptMapGroupElement"
    code: Optional[str] = None
    display: Optional[str] = None
    target: Optional[List[ConceptMapGroupElementTarget]] = empty_list()

    def elementProperties(self):
        js = super(ConceptMapGroupElement, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("target", "target", ConceptMapGroupElementTarget, True, None, False),
        ])
        return js


@dataclass
class ConceptMapGroup(BackboneElement):
    """ Same source and target systems.

    A group of mappings that all have the same source and target system.
    """
    resource_type: ClassVar[str] = "ConceptMapGroup"
    element: List[ConceptMapGroupElement] = empty_list()
    source: Optional[str] = None
    sourceVersion: Optional[str] = None
    target: Optional[str] = None
    targetVersion: Optional[str] = None
    unmapped: Optional[ConceptMapGroupUnmapped] = None

    def elementProperties(self):
        js = super(ConceptMapGroup, self).elementProperties()
        js.extend([
            ("element", "element", ConceptMapGroupElement, True, None, True),
            ("source", "source", str, False, None, False),
            ("sourceVersion", "sourceVersion", str, False, None, False),
            ("target", "target", str, False, None, False),
            ("targetVersion", "targetVersion", str, False, None, False),
            ("unmapped", "unmapped", ConceptMapGroupUnmapped, False, None, False),
        ])
        return js


@dataclass
class ConceptMap(DomainResource):
    """ A map from one set of concepts to one or more other concepts.

    A statement of relationships from one set of concepts to one or more other
    concepts - either concepts in code systems, or data element/data element
    concepts, or classes in class models.
    """
    resource_type: ClassVar[str] = "ConceptMap"
    contact: Optional[List[ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[FHIRDate] = None
    description: Optional[str] = None
    experimental: Optional[bool] = None
    group: Optional[List[ConceptMapGroup]] = empty_list()
    identifier: Optional[Identifier] = None
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    name: Optional[str] = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    sourceCanonical: Optional[str] = None
    sourceUri: Optional[str] = None
    status: str = None
    targetCanonical: Optional[str] = None
    targetUri: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    version: Optional[str] = None

    def elementProperties(self):
        js = super(ConceptMap, self).elementProperties()
        js.extend([
            ("contact", "contact", ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("group", "group", ConceptMapGroup, True, None, False),
            ("identifier", "identifier", Identifier, False, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("sourceCanonical", "sourceCanonical", str, False, "source", False),
            ("sourceUri", "sourceUri", str, False, "source", False),
            ("status", "status", str, False, None, True),
            ("targetCanonical", "targetCanonical", str, False, "target", False),
            ("targetUri", "targetUri", str, False, "target", False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js