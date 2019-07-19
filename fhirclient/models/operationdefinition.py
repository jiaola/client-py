#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/OperationDefinition) on 2019-07-18.
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
class OperationDefinitionParameterReferencedFrom(BackboneElement):
    """ References to this parameter.

    Identifies other resource parameters within the operation invocation that
    are expected to resolve to this resource.
    """
    resource_type: ClassVar[str] = "OperationDefinitionParameterReferencedFrom"
    source: str = None
    sourceId: Optional[str] = None

    def elementProperties(self):
        js = super(OperationDefinitionParameterReferencedFrom, self).elementProperties()
        js.extend([
            ("source", "source", str, False, None, True),
            ("sourceId", "sourceId", str, False, None, False),
        ])
        return js


@dataclass
class OperationDefinitionParameterBinding(BackboneElement):
    """ ValueSet details if this is coded.

    Binds to a value set if this parameter is coded (code, Coding,
    CodeableConcept).
    """
    resource_type: ClassVar[str] = "OperationDefinitionParameterBinding"
    strength: str = None
    valueSet: str = None

    def elementProperties(self):
        js = super(OperationDefinitionParameterBinding, self).elementProperties()
        js.extend([
            ("strength", "strength", str, False, None, True),
            ("valueSet", "valueSet", str, False, None, True),
        ])
        return js


@dataclass
class OperationDefinitionParameter(BackboneElement):
    """ Parameters for the operation/query.

    The parameters for the operation/query.
    """
    resource_type: ClassVar[str] = "OperationDefinitionParameter"
    binding: Optional[OperationDefinitionParameterBinding] = None
    documentation: Optional[str] = None
    max: str = None
    min: int = None
    name: str = None
    part: Optional[List[OperationDefinitionParameter]] = empty_list()
    referencedFrom: Optional[List[OperationDefinitionParameterReferencedFrom]] = empty_list()
    searchType: Optional[str] = None
    targetProfile: Optional[List[str]] = empty_list()
    type: Optional[str] = None
    use: str = None

    def elementProperties(self):
        js = super(OperationDefinitionParameter, self).elementProperties()
        js.extend([
            ("binding", "binding", OperationDefinitionParameterBinding, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("max", "max", str, False, None, True),
            ("min", "min", int, False, None, True),
            ("name", "name", str, False, None, True),
            ("part", "part", OperationDefinitionParameter, True, None, False),
            ("referencedFrom", "referencedFrom", OperationDefinitionParameterReferencedFrom, True, None, False),
            ("searchType", "searchType", str, False, None, False),
            ("targetProfile", "targetProfile", str, True, None, False),
            ("type", "type", str, False, None, False),
            ("use", "use", str, False, None, True),
        ])
        return js


@dataclass
class OperationDefinitionOverload(BackboneElement):
    """ Define overloaded variants for when  generating code.

    Defines an appropriate combination of parameters to use when invoking this
    operation, to help code generators when generating overloaded parameter
    sets for this operation.
    """
    resource_type: ClassVar[str] = "OperationDefinitionOverload"
    comment: Optional[str] = None
    parameterName: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(OperationDefinitionOverload, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("parameterName", "parameterName", str, True, None, False),
        ])
        return js


@dataclass
class OperationDefinition(DomainResource):
    """ Definition of an operation or a named query.

    A formal computable definition of an operation (on the RESTful interface)
    or a named query (using the search interaction).
    """
    resource_type: ClassVar[str] = "OperationDefinition"
    affectsState: Optional[bool] = None
    base: Optional[str] = None
    code: str = None
    comment: Optional[str] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    date: Optional[FHIRDate] = None
    description: Optional[str] = None
    experimental: Optional[bool] = None
    inputProfile: Optional[str] = None
    instance: bool = None
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    kind: str = None
    name: str = None
    outputProfile: Optional[str] = None
    overload: Optional[List[OperationDefinitionOverload]] = empty_list()
    parameter: Optional[List[OperationDefinitionParameter]] = empty_list()
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    resource: Optional[List[str]] = empty_list()
    status: str = None
    system: bool = None
    title: Optional[str] = None
    type: bool = None
    url: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    version: Optional[str] = None

    def elementProperties(self):
        js = super(OperationDefinition, self).elementProperties()
        js.extend([
            ("affectsState", "affectsState", bool, False, None, False),
            ("base", "base", str, False, None, False),
            ("code", "code", str, False, None, True),
            ("comment", "comment", str, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("inputProfile", "inputProfile", str, False, None, False),
            ("instance", "instance", bool, False, None, True),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("outputProfile", "outputProfile", str, False, None, False),
            ("overload", "overload", OperationDefinitionOverload, True, None, False),
            ("parameter", "parameter", OperationDefinitionParameter, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("resource", "resource", str, True, None, False),
            ("status", "status", str, False, None, True),
            ("system", "system", bool, False, None, True),
            ("title", "title", str, False, None, False),
            ("type", "type", bool, False, None, True),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js