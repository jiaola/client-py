#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SearchParameter) on 2019-07-03.
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
class SearchParameter(domainresource.DomainResource):
    """ Search parameter for a resource.

    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """
    resource_type: ClassVar[str] = "SearchParameter"
    base: List[ str] = empty_list()
    chain: Optional[List[str]] = empty_list()
    code: str = None
    comparator: Optional[List[str]] = empty_list()
    component: Optional[List[SearchParameterComponent]] = empty_list()
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    date: Optional[fhirdate.FHIRDate] = None
    derivedFrom: Optional[str] = None
    description: str = None
    experimental: Optional[bool] = None
    expression: Optional[str] = None
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    modifier: Optional[List[str]] = empty_list()
    multipleAnd: Optional[bool] = None
    multipleOr: Optional[bool] = None
    name: str = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    status: str = None
    target: Optional[List[str]] = empty_list()
    type: str = None
    url: str = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    version: Optional[str] = None
    xpath: Optional[str] = None
    xpathUsage: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.base = None
#        """ The resource type(s) this search parameter applies to.
#        List of `str` items
#
#. """
#
#
#        self.chain = None
#        """ Chained names supported.
#        List of `str` items
#
#. """
#
#
#        self.code = None
#        """ Code used in URL.
#        Type `str`
#
#. """
#
#
#        self.comparator = None
#        """ eq | ne | gt | lt | ge | le | sa | eb | ap.
#        List of `str` items
#
#. """
#
#
#        self.component = None
#        """ For Composite resources to define the parts.
#        List of `SearchParameterComponent` items
#
# (represented as `dict` in JSON). """
#
#
#        self.contact = None
#        """ Contact details for the publisher.
#        List of `ContactDetail` items
#
# (represented as `dict` in JSON). """
#
#
#        self.date = None
#        """ Date last changed.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.derivedFrom = None
#        """ Original definition for the search parameter.
#        Type `str`
#
#. """
#
#
#        self.description = None
#        """ Natural language description of the search parameter.
#        Type `str`
#
#. """
#
#
#        self.experimental = None
#        """ For testing purposes, not real usage.
#        Type `bool`
#
#. """
#
#
#        self.expression = None
#        """ FHIRPath expression that extracts the values.
#        Type `str`
#
#. """
#
#
#        self.jurisdiction = None
#        """ Intended jurisdiction for search parameter (if applicable).
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.modifier = None
#        """ missing | exact | contains | not | text | in | not-in | below |
        above | type | identifier | ofType.
#        List of `str` items
#
#. """
#
#
#        self.multipleAnd = None
#        """ Allow multiple parameters (and).
#        Type `bool`
#
#. """
#
#
#        self.multipleOr = None
#        """ Allow multiple values per parameter (or).
#        Type `bool`
#
#. """
#
#
#        self.name = None
#        """ Name for this search parameter (computer friendly).
#        Type `str`
#
#. """
#
#
#        self.publisher = None
#        """ Name of the publisher (organization or individual).
#        Type `str`
#
#. """
#
#
#        self.purpose = None
#        """ Why this search parameter is defined.
#        Type `str`
#
#. """
#
#
#        self.status = None
#        """ draft | active | retired | unknown.
#        Type `str`
#
#. """
#
#
#        self.target = None
#        """ Types of resource (if a resource reference).
#        List of `str` items
#
#. """
#
#
#        self.type = None
#        """ number | date | string | token | reference | composite | quantity |
        uri | special.
#        Type `str`
#
#. """
#
#
#        self.url = None
#        """ Canonical identifier for this search parameter, represented as a
        URI (globally unique).
#        Type `str`
#
#. """
#
#
#        self.useContext = None
#        """ The context that the content is intended to support.
#        List of `UsageContext` items
#
# (represented as `dict` in JSON). """
#
#
#        self.version = None
#        """ Business version of the search parameter.
#        Type `str`
#
#. """
#
#
#        self.xpath = None
#        """ XPath that extracts the values.
#        Type `str`
#
#. """
#
#
#        self.xpathUsage = None
#        """ normal | phonetic | nearby | distance | other.
#        Type `str`
#
#. """
#

#        super(SearchParameter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SearchParameter, self).elementProperties()
        js.extend([
            ("base", "base", str, {  # #}True, None, {  # #}True),
            ("chain", "chain", str, {  # #}True, None, {  # #}False),
            ("code", "code", str, {  # #}False, None, {  # #}True),
            ("comparator", "comparator", str, {  # #}True, None, {  # #}False),
            ("component", "component", SearchParameterComponent, {  # #}True, None, {  # #}False),
            ("contact", "contact", contactdetail.ContactDetail, {  # #}True, None, {  # #}False),
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("derivedFrom", "derivedFrom", str, {  # #}False, None, {  # #}False),
            ("description", "description", str, {  # #}False, None, {  # #}True),
            ("experimental", "experimental", bool, {  # #}False, None, {  # #}False),
            ("expression", "expression", str, {  # #}False, None, {  # #}False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("modifier", "modifier", str, {  # #}True, None, {  # #}False),
            ("multipleAnd", "multipleAnd", bool, {  # #}False, None, {  # #}False),
            ("multipleOr", "multipleOr", bool, {  # #}False, None, {  # #}False),
            ("name", "name", str, {  # #}False, None, {  # #}True),
            ("publisher", "publisher", str, {  # #}False, None, {  # #}False),
            ("purpose", "purpose", str, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("target", "target", str, {  # #}True, None, {  # #}False),
            ("type", "type", str, {  # #}False, None, {  # #}True),
            ("url", "url", str, {  # #}False, None, {  # #}True),
            ("useContext", "useContext", usagecontext.UsageContext, {  # #}True, None, {  # #}False),
            ("version", "version", str, {  # #}False, None, {  # #}False),
            ("xpath", "xpath", str, {  # #}False, None, {  # #}False),
            ("xpathUsage", "xpathUsage", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import contactdetail
from . import fhirdate
from . import usagecontext


from . import backboneelement

@dataclass
class SearchParameterComponent(backboneelement.BackboneElement):
    """ For Composite resources to define the parts.

    Used to define the parts of a composite search parameter.
    """
    resource_type: ClassVar[str] = "SearchParameterComponent"
    definition: str = None
    expression: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.definition = None
#        """ Defines how the part works.
#        Type `str`
#
#. """
#
#
#        self.expression = None
#        """ Subexpression relative to main expression.
#        Type `str`
#
#. """
#

#        super(SearchParameterComponent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SearchParameterComponent, self).elementProperties()
        js.extend([
            ("definition", "definition", str, {  # #}False, None, {  # #}True),
            ("expression", "expression", str, {  # #}False, None, {  # #}True),
        ])
        return js