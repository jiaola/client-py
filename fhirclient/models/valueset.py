#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ValueSet) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .identifier import Identifier
from .usagecontext import UsageContext


@dataclass
class ValueSetExpansionParameter(BackboneElement):
    """ Parameter that controlled the expansion process.

    A parameter that controlled the expansion process. These parameters may be
    used by users of expanded value sets to check whether the expansion is
    suitable for a particular purpose, or to pick the correct expansion.
    """
    resource_type: ClassVar[str] = "ValueSetExpansionParameter"
    name: str = None
    valueBoolean: Optional[bool] = None
    valueCode: Optional[str] = None
    valueDateTime: Optional[FHIRDate] = None
    valueDecimal: Optional[float] = None
    valueInteger: Optional[int] = None
    valueString: Optional[str] = None
    valueUri: Optional[str] = None

    def elementProperties(self):
        js = super(ValueSetExpansionParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCode", "valueCode", str, False, "value", False),
            ("valueDateTime", "valueDateTime", FHIRDate, False, "value", False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueUri", "valueUri", str, False, "value", False),
        ])
        return js


@dataclass
class ValueSetExpansionContains(BackboneElement):
    """ Codes in the value set.

    The codes that are contained in the value set expansion.
    """
    resource_type: ClassVar[str] = "ValueSetExpansionContains"
    abstract: Optional[bool] = None
    code: Optional[str] = None
    contains: Optional[List[ValueSetExpansionContains]] = empty_list()
    designation: Optional[List[ValueSetComposeIncludeConceptDesignation]] = empty_list()
    display: Optional[str] = None
    inactive: Optional[bool] = None
    system: Optional[str] = None
    version: Optional[str] = None

    def elementProperties(self):
        js = super(ValueSetExpansionContains, self).elementProperties()
        js.extend([
            ("abstract", "abstract", bool, False, None, False),
            ("code", "code", str, False, None, False),
            ("contains", "contains", ValueSetExpansionContains, True, None, False),
            ("designation", "designation", ValueSetComposeIncludeConceptDesignation, True, None, False),
            ("display", "display", str, False, None, False),
            ("inactive", "inactive", bool, False, None, False),
            ("system", "system", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


@dataclass
class ValueSetExpansion(BackboneElement):
    """ Used when the value set is "expanded".

    A value set can also be "expanded", where the value set is turned into a
    simple collection of enumerated codes. This element holds the expansion, if
    it has been performed.
    """
    resource_type: ClassVar[str] = "ValueSetExpansion"
    contains: Optional[List[ValueSetExpansionContains]] = empty_list()
    identifier: Optional[str] = None
    offset: Optional[int] = None
    parameter: Optional[List[ValueSetExpansionParameter]] = empty_list()
    timestamp: FHIRDate = None
    total: Optional[int] = None

    def elementProperties(self):
        js = super(ValueSetExpansion, self).elementProperties()
        js.extend([
            ("contains", "contains", ValueSetExpansionContains, True, None, False),
            ("identifier", "identifier", str, False, None, False),
            ("offset", "offset", int, False, None, False),
            ("parameter", "parameter", ValueSetExpansionParameter, True, None, False),
            ("timestamp", "timestamp", FHIRDate, False, None, True),
            ("total", "total", int, False, None, False),
        ])
        return js


@dataclass
class ValueSetComposeIncludeFilter(BackboneElement):
    """ Select codes/concepts by their properties (including relationships).

    Select concepts by specify a matching criterion based on the properties
    (including relationships) defined by the system, or on filters defined by
    the system. If multiple filters are specified, they SHALL all be true.
    """
    resource_type: ClassVar[str] = "ValueSetComposeIncludeFilter"
    op: str = None
    property: str = None
    value: str = None

    def elementProperties(self):
        js = super(ValueSetComposeIncludeFilter, self).elementProperties()
        js.extend([
            ("op", "op", str, False, None, True),
            ("property", "property", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


@dataclass
class ValueSetComposeIncludeConceptDesignation(BackboneElement):
    """ Additional representations for this concept.

    Additional representations for this concept when used in this value set -
    other languages, aliases, specialized purposes, used for particular
    purposes, etc.
    """
    resource_type: ClassVar[str] = "ValueSetComposeIncludeConceptDesignation"
    language: Optional[str] = None
    use: Optional[Coding] = None
    value: str = None

    def elementProperties(self):
        js = super(ValueSetComposeIncludeConceptDesignation, self).elementProperties()
        js.extend([
            ("language", "language", str, False, None, False),
            ("use", "use", Coding, False, None, False),
            ("value", "value", str, False, None, True),
        ])
        return js


@dataclass
class ValueSetComposeIncludeConcept(BackboneElement):
    """ A concept defined in the system.

    Specifies a concept to be included or excluded.
    """
    resource_type: ClassVar[str] = "ValueSetComposeIncludeConcept"
    code: str = None
    designation: Optional[List[ValueSetComposeIncludeConceptDesignation]] = empty_list()
    display: Optional[str] = None

    def elementProperties(self):
        js = super(ValueSetComposeIncludeConcept, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("designation", "designation", ValueSetComposeIncludeConceptDesignation, True, None, False),
            ("display", "display", str, False, None, False),
        ])
        return js


@dataclass
class ValueSetComposeInclude(BackboneElement):
    """ Include one or more codes from a code system or other value set(s).
    """
    resource_type: ClassVar[str] = "ValueSetComposeInclude"
    concept: Optional[List[ValueSetComposeIncludeConcept]] = empty_list()
    filter: Optional[List[ValueSetComposeIncludeFilter]] = empty_list()
    system: Optional[str] = None
    valueSet: Optional[List[str]] = empty_list()
    version: Optional[str] = None

    def elementProperties(self):
        js = super(ValueSetComposeInclude, self).elementProperties()
        js.extend([
            ("concept", "concept", ValueSetComposeIncludeConcept, True, None, False),
            ("filter", "filter", ValueSetComposeIncludeFilter, True, None, False),
            ("system", "system", str, False, None, False),
            ("valueSet", "valueSet", str, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


@dataclass
class ValueSetCompose(BackboneElement):
    """ Content logical definition of the value set (CLD).

    A set of criteria that define the contents of the value set by including or
    excluding codes selected from the specified code system(s) that the value
    set draws from. This is also known as the Content Logical Definition (CLD).
    """
    resource_type: ClassVar[str] = "ValueSetCompose"
    exclude: Optional[List[ValueSetComposeInclude]] = empty_list()
    inactive: Optional[bool] = None
    include: List[ValueSetComposeInclude] = empty_list()
    lockedDate: Optional[FHIRDate] = None

    def elementProperties(self):
        js = super(ValueSetCompose, self).elementProperties()
        js.extend([
            ("exclude", "exclude", ValueSetComposeInclude, True, None, False),
            ("inactive", "inactive", bool, False, None, False),
            ("include", "include", ValueSetComposeInclude, True, None, True),
            ("lockedDate", "lockedDate", FHIRDate, False, None, False),
        ])
        return js


@dataclass
class ValueSet(DomainResource):
    """ A set of codes drawn from one or more code systems.

    A ValueSet resource instance specifies a set of codes drawn from one or
    more code systems, intended for use in a particular context. Value sets
    link between [CodeSystem](codesystem.html) definitions and their use in
    [coded elements](terminologies.html).
    """
    resource_type: ClassVar[str] = "ValueSet"
    compose: Optional[ValueSetCompose] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[FHIRDate] = None
    description: Optional[str] = None
    expansion: Optional[ValueSetExpansion] = None
    experimental: Optional[bool] = None
    identifier: Optional[List[Identifier]] = empty_list()
    immutable: Optional[bool] = None
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    name: Optional[str] = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    status: str = None
    title: Optional[str] = None
    url: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    version: Optional[str] = None

    def elementProperties(self):
        js = super(ValueSet, self).elementProperties()
        js.extend([
            ("compose", "compose", ValueSetCompose, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("expansion", "expansion", ValueSetExpansion, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("immutable", "immutable", bool, False, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js