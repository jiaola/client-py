#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/StructureDefinition) on 2019-07-18.
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
from . import elementdefinition
from . import fhirdate
from . import identifier
from . import usagecontext

from . import backboneelement

@dataclass
class StructureDefinitionSnapshot(backboneelement.BackboneElement):
    """ Snapshot view of the structure.

    A snapshot view is expressed in a standalone form that can be used and
    interpreted without considering the base StructureDefinition.
    """
    resource_type: ClassVar[str] = "StructureDefinitionSnapshot"
    element: List[elementdefinition.ElementDefinition] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(StructureDefinitionSnapshot, self).elementProperties()
        js.extend([
            ("element", "element", elementdefinition.ElementDefinition, True, None, True),
        ])
        return js

@dataclass
class StructureDefinitionMapping(backboneelement.BackboneElement):
    """ External specification that the content is mapped to.

    An external specification that the content is mapped to.
    """
    resource_type: ClassVar[str] = "StructureDefinitionMapping"
    comment: Optional[str] = None
    identity: str = None
    name: Optional[str] = None
    uri: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(StructureDefinitionMapping, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("identity", "identity", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("uri", "uri", str, False, None, False),
        ])
        return js

@dataclass
class StructureDefinitionDifferential(backboneelement.BackboneElement):
    """ Differential view of the structure.

    A differential view is expressed relative to the base StructureDefinition -
    a statement of differences that it applies.
    """
    resource_type: ClassVar[str] = "StructureDefinitionDifferential"
    element: List[elementdefinition.ElementDefinition] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(StructureDefinitionDifferential, self).elementProperties()
        js.extend([
            ("element", "element", elementdefinition.ElementDefinition, True, None, True),
        ])
        return js

@dataclass
class StructureDefinitionContext(backboneelement.BackboneElement):
    """ If an extension, where it can be used in instances.

    Identifies the types of resource or data type elements to which the
    extension can be applied.
    """
    resource_type: ClassVar[str] = "StructureDefinitionContext"
    expression: str = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(StructureDefinitionContext, self).elementProperties()
        js.extend([
            ("expression", "expression", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js

from . import domainresource

@dataclass
class StructureDefinition(domainresource.DomainResource):
    """ Structural Definition.

    A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for describing
    extensions and constraints on resources and data types.
    """
    resource_type: ClassVar[str] = "StructureDefinition"
    abstract: bool = None
    baseDefinition: Optional[str] = None
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    context: Optional[List[StructureDefinitionContext]] = empty_list()
    contextInvariant: Optional[List[str]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[fhirdate.FHIRDate] = None
    derivation: Optional[str] = None
    description: Optional[str] = None
    differential: Optional[StructureDefinitionDifferential] = None
    experimental: Optional[bool] = None
    fhirVersion: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    keyword: Optional[List[coding.Coding]] = empty_list()
    kind: str = None
    mapping: Optional[List[StructureDefinitionMapping]] = empty_list()
    name: str = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    snapshot: Optional[StructureDefinitionSnapshot] = None
    status: str = None
    title: Optional[str] = None
    type: str = None
    url: str = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(StructureDefinition, self).elementProperties()
        js.extend([
            ("abstract", "abstract", bool, False, None, True),
            ("baseDefinition", "baseDefinition", str, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("context", "context", StructureDefinitionContext, True, None, False),
            ("contextInvariant", "contextInvariant", str, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("derivation", "derivation", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("differential", "differential", StructureDefinitionDifferential, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("fhirVersion", "fhirVersion", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("keyword", "keyword", coding.Coding, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("mapping", "mapping", StructureDefinitionMapping, True, None, False),
            ("name", "name", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("snapshot", "snapshot", StructureDefinitionSnapshot, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
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
    from . import elementdefinition
except ImportError:
    elementdefinition = sys.modules[__package__ + '.elementdefinition']
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