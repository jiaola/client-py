#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CodeSystem) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import coding
from . import contactdetail
from . import domainresource
from . import fhirdate
from . import identifier
from . import usagecontext

from . import domainresource

@dataclass
class CodeSystem(domainresource.DomainResource):
    """ Declares the existence of and describes a code system or code system
    supplement.

    The CodeSystem resource is used to declare the existence of and describe a
    code system or code system supplement and its key properties, and
    optionally define a part or all of its content.
    """
    resource_type: ClassVar[str] = "CodeSystem"
    caseSensitive: Optional[bool] = None
    compositional: Optional[bool] = None
    concept: Optional[List[CodeSystemConcept]] = empty_list()
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    content: str = None
    copyright: Optional[str] = None
    count: Optional[int] = None
    date: Optional[fhirdate.FHIRDate] = None
    description: Optional[str] = None
    experimental: Optional[bool] = None
    filter: Optional[List[CodeSystemFilter]] = empty_list()
    hierarchyMeaning: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    name: Optional[str] = None
    property: Optional[List[CodeSystemProperty]] = empty_list()
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    status: str = None
    supplements: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    valueSet: Optional[str] = None
    version: Optional[str] = None
    versionNeeded: Optional[bool] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CodeSystem, self).elementProperties()
        js.extend([
            ("caseSensitive", "caseSensitive", bool, False, None, False),
            ("compositional", "compositional", bool, False, None, False),
            ("concept", "concept", CodeSystemConcept, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("content", "content", str, False, None, True),
            ("copyright", "copyright", str, False, None, False),
            ("count", "count", int, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("filter", "filter", CodeSystemFilter, True, None, False),
            ("hierarchyMeaning", "hierarchyMeaning", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("property", "property", CodeSystemProperty, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("supplements", "supplements", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("valueSet", "valueSet", str, False, None, False),
            ("version", "version", str, False, None, False),
            ("versionNeeded", "versionNeeded", bool, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class CodeSystemConcept(backboneelement.BackboneElement):
    """ Concepts in the code system.

    Concepts that are in the code system. The concept definitions are
    inherently hierarchical, but the definitions must be consulted to determine
    what the meanings of the hierarchical relationships are.
    """
    resource_type: ClassVar[str] = "CodeSystemConcept"
    code: str = None
    concept: Optional[List[CodeSystemConcept]] = empty_list()
    definition: Optional[str] = None
    designation: Optional[List[CodeSystemConceptDesignation]] = empty_list()
    display: Optional[str] = None
    property: Optional[List[CodeSystemConceptProperty]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CodeSystemConcept, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("concept", "concept", CodeSystemConcept, True, None, False),
            ("definition", "definition", str, False, None, False),
            ("designation", "designation", CodeSystemConceptDesignation, True, None, False),
            ("display", "display", str, False, None, False),
            ("property", "property", CodeSystemConceptProperty, True, None, False),
        ])
        return js

@dataclass
class CodeSystemConceptDesignation(backboneelement.BackboneElement):
    """ Additional representations for the concept.

    Additional representations for the concept - other languages, aliases,
    specialized purposes, used for particular purposes, etc.
    """
    resource_type: ClassVar[str] = "CodeSystemConceptDesignation"
    language: Optional[str] = None
    use: Optional[coding.Coding] = None
    value: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CodeSystemConceptDesignation, self).elementProperties()
        js.extend([
            ("language", "language", str, False, None, False),
            ("use", "use", coding.Coding, False, None, False),
            ("value", "value", str, False, None, True),
        ])
        return js

@dataclass
class CodeSystemConceptProperty(backboneelement.BackboneElement):
    """ Property value for the concept.

    A property value for this concept.
    """
    resource_type: ClassVar[str] = "CodeSystemConceptProperty"
    code: str = None
    valueBoolean: bool = None
    valueCode: str = None
    valueCoding:coding.Coding = None
    valueDateTime:fhirdate.FHIRDate = None
    valueDecimal: float = None
    valueInteger: int = None
    valueString: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CodeSystemConceptProperty, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCode", "valueCode", str, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
        ])
        return js

@dataclass
class CodeSystemFilter(backboneelement.BackboneElement):
    """ Filter that can be used in a value set.

    A filter that can be used in a value set compose statement when selecting
    concepts using a filter.
    """
    resource_type: ClassVar[str] = "CodeSystemFilter"
    code: str = None
    description: Optional[str] = None
    operator: List[ str] = empty_list()
    value: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CodeSystemFilter, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("operator", "operator", str, True, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js

@dataclass
class CodeSystemProperty(backboneelement.BackboneElement):
    """ Additional information supplied about each concept.

    A property defines an additional slot through which additional information
    can be provided about a concept.
    """
    resource_type: ClassVar[str] = "CodeSystemProperty"
    code: str = None
    description: Optional[str] = None
    type: str = None
    uri: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CodeSystemProperty, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("uri", "uri", str, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']