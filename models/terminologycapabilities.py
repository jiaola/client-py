#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/TerminologyCapabilities) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import contactdetail
from . import domainresource
from . import fhirdate
from . import usagecontext

from . import domainresource

@dataclass
class TerminologyCapabilities(domainresource.DomainResource):
    """ A statement of system capabilities.

    A TerminologyCapabilities resource documents a set of capabilities
    (behaviors) of a FHIR Terminology Server that may be used as a statement of
    actual server functionality or a statement of required or desired server
    implementation.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilities"
    closure: Optional[TerminologyCapabilitiesClosure] = None
    codeSearch: Optional[str] = None
    codeSystem: Optional[List[TerminologyCapabilitiesCodeSystem]] = empty_list()
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date:fhirdate.FHIRDate = None
    description: Optional[str] = None
    expansion: Optional[TerminologyCapabilitiesExpansion] = None
    experimental: Optional[bool] = None
    implementation: Optional[TerminologyCapabilitiesImplementation] = None
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    kind: str = None
    lockedDate: Optional[bool] = None
    name: Optional[str] = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    software: Optional[TerminologyCapabilitiesSoftware] = None
    status: str = None
    title: Optional[str] = None
    translation: Optional[TerminologyCapabilitiesTranslation] = None
    url: Optional[str] = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    validateCode: Optional[TerminologyCapabilitiesValidateCode] = None
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TerminologyCapabilities, self).elementProperties()
        js.extend([
            ("closure", "closure", TerminologyCapabilitiesClosure, False, None, False),
            ("codeSearch", "codeSearch", str, False, None, False),
            ("codeSystem", "codeSystem", TerminologyCapabilitiesCodeSystem, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("description", "description", str, False, None, False),
            ("expansion", "expansion", TerminologyCapabilitiesExpansion, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("implementation", "implementation", TerminologyCapabilitiesImplementation, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("lockedDate", "lockedDate", bool, False, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("software", "software", TerminologyCapabilitiesSoftware, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("translation", "translation", TerminologyCapabilitiesTranslation, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("validateCode", "validateCode", TerminologyCapabilitiesValidateCode, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class TerminologyCapabilitiesClosure(backboneelement.BackboneElement):
    """ Information about the [ConceptMap/$closure](conceptmap-operation-
    closure.html) operation.

    Whether the $closure operation is supported.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesClosure"
    translation: Optional[bool] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesClosure, self).elementProperties()
        js.extend([
            ("translation", "translation", bool, False, None, False),
        ])
        return js

@dataclass
class TerminologyCapabilitiesCodeSystem(backboneelement.BackboneElement):
    """ A code system supported by the server.

    Identifies a code system that is supported by the server. If there is a no
    code system URL, then this declares the general assumptions a client can
    make about support for any CodeSystem resource.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesCodeSystem"
    subsumption: Optional[bool] = None
    uri: Optional[str] = None
    version: Optional[List[TerminologyCapabilitiesCodeSystemVersion]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesCodeSystem, self).elementProperties()
        js.extend([
            ("subsumption", "subsumption", bool, False, None, False),
            ("uri", "uri", str, False, None, False),
            ("version", "version", TerminologyCapabilitiesCodeSystemVersion, True, None, False),
        ])
        return js

@dataclass
class TerminologyCapabilitiesCodeSystemVersion(backboneelement.BackboneElement):
    """ Version of Code System supported.

    For the code system, a list of versions that are supported by the server.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesCodeSystemVersion"
    code: Optional[str] = None
    compositional: Optional[bool] = None
    filter: Optional[List[TerminologyCapabilitiesCodeSystemVersionFilter]] = empty_list()
    isDefault: Optional[bool] = None
    language: Optional[List[str]] = empty_list()
    property: Optional[List[str]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesCodeSystemVersion, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("compositional", "compositional", bool, False, None, False),
            ("filter", "filter", TerminologyCapabilitiesCodeSystemVersionFilter, True, None, False),
            ("isDefault", "isDefault", bool, False, None, False),
            ("language", "language", str, True, None, False),
            ("property", "property", str, True, None, False),
        ])
        return js

@dataclass
class TerminologyCapabilitiesCodeSystemVersionFilter(backboneelement.BackboneElement):
    """ Filter Properties supported.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesCodeSystemVersionFilter"
    code: str = None
    op: List[ str] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesCodeSystemVersionFilter, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("op", "op", str, True, None, True),
        ])
        return js

@dataclass
class TerminologyCapabilitiesExpansion(backboneelement.BackboneElement):
    """ Information about the [ValueSet/$expand](valueset-operation-expand.html)
    operation.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesExpansion"
    hierarchical: Optional[bool] = None
    incomplete: Optional[bool] = None
    paging: Optional[bool] = None
    parameter: Optional[List[TerminologyCapabilitiesExpansionParameter]] = empty_list()
    textFilter: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesExpansion, self).elementProperties()
        js.extend([
            ("hierarchical", "hierarchical", bool, False, None, False),
            ("incomplete", "incomplete", bool, False, None, False),
            ("paging", "paging", bool, False, None, False),
            ("parameter", "parameter", TerminologyCapabilitiesExpansionParameter, True, None, False),
            ("textFilter", "textFilter", str, False, None, False),
        ])
        return js

@dataclass
class TerminologyCapabilitiesExpansionParameter(backboneelement.BackboneElement):
    """ Supported expansion parameter.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesExpansionParameter"
    documentation: Optional[str] = None
    name: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesExpansionParameter, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("name", "name", str, False, None, True),
        ])
        return js

@dataclass
class TerminologyCapabilitiesImplementation(backboneelement.BackboneElement):
    """ If this describes a specific instance.

    Identifies a specific implementation instance that is described by the
    terminology capability statement - i.e. a particular installation, rather
    than the capabilities of a software program.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesImplementation"
    description: str = None
    url: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesImplementation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("url", "url", str, False, None, False),
        ])
        return js

@dataclass
class TerminologyCapabilitiesSoftware(backboneelement.BackboneElement):
    """ Software that is covered by this terminology capability statement.

    Software that is covered by this terminology capability statement.  It is
    used when the statement describes the capabilities of a particular software
    version, independent of an installation.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesSoftware"
    name: str = None
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesSoftware, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js

@dataclass
class TerminologyCapabilitiesTranslation(backboneelement.BackboneElement):
    """ Information about the [ConceptMap/$translate](conceptmap-operation-
    translate.html) operation.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesTranslation"
    needsMap: bool = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesTranslation, self).elementProperties()
        js.extend([
            ("needsMap", "needsMap", bool, False, None, True),
        ])
        return js

@dataclass
class TerminologyCapabilitiesValidateCode(backboneelement.BackboneElement):
    """ Information about the [ValueSet/$validate-code](valueset-operation-
    validate-code.html) operation.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesValidateCode"
    translations: bool = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesValidateCode, self).elementProperties()
        js.extend([
            ("translations", "translations", bool, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']