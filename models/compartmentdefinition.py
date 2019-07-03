#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CompartmentDefinition) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import contactdetail
from . import domainresource
from . import fhirdate
from . import usagecontext


from . import domainresource

@dataclass
class CompartmentDefinition(domainresource.DomainResource):
    """ Compartment Definition for a resource.

    A compartment definition that defines how resources are accessed on a
    server.
    """
    resource_type: ClassVar[str] = "CompartmentDefinition"
    code: str = None
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    date: Optional[fhirdate.FHIRDate] = None
    description: Optional[str] = None
    experimental: Optional[bool] = None
    name: str = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    resource: Optional[List[CompartmentDefinitionResource]] = empty_list()
    search: bool = None
    status: str = None
    url: str = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    version: Optional[str] = None

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
#        self.code = None
#        """ Patient | Encounter | RelatedPerson | Practitioner | Device.
#        Type `str`
#
#. """
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
#        self.description = None
#        """ Natural language description of the compartment definition.
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
#        self.name = None
#        """ Name for this compartment definition (computer friendly).
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
#        """ Why this compartment definition is defined.
#        Type `str`
#
#. """
#
#
#        self.resource = None
#        """ How a resource is related to the compartment.
#        List of `CompartmentDefinitionResource` items
#
# (represented as `dict` in JSON). """
#
#
#        self.search = None
#        """ Whether the search syntax is supported.
#        Type `bool`
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
#        self.url = None
#        """ Canonical identifier for this compartment definition, represented
        as a URI (globally unique).
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
#        """ Business version of the compartment definition.
#        Type `str`
#
#. """
#

#        super(CompartmentDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CompartmentDefinition, self).elementProperties()
        js.extend([
            ("code", "code", str, {  # #}False, None, {  # #}True),
            ("contact", "contact", contactdetail.ContactDetail, {  # #}True, None, {  # #}False),
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("experimental", "experimental", bool, {  # #}False, None, {  # #}False),
            ("name", "name", str, {  # #}False, None, {  # #}True),
            ("publisher", "publisher", str, {  # #}False, None, {  # #}False),
            ("purpose", "purpose", str, {  # #}False, None, {  # #}False),
            ("resource", "resource", CompartmentDefinitionResource, {  # #}True, None, {  # #}False),
            ("search", "search", bool, {  # #}False, None, {  # #}True),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("url", "url", str, {  # #}False, None, {  # #}True),
            ("useContext", "useContext", usagecontext.UsageContext, {  # #}True, None, {  # #}False),
            ("version", "version", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import contactdetail
from . import fhirdate
from . import usagecontext


from . import backboneelement

@dataclass
class CompartmentDefinitionResource(backboneelement.BackboneElement):
    """ How a resource is related to the compartment.

    Information about how a resource is related to the compartment.
    """
    resource_type: ClassVar[str] = "CompartmentDefinitionResource"
    code: str = None
    documentation: Optional[str] = None
    param: Optional[List[str]] = empty_list()

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
#        self.code = None
#        """ Name of resource type.
#        Type `str`
#
#. """
#
#
#        self.documentation = None
#        """ Additional documentation about the resource and compartment.
#        Type `str`
#
#. """
#
#
#        self.param = None
#        """ Search Parameter Name, or chained parameters.
#        List of `str` items
#
#. """
#

#        super(CompartmentDefinitionResource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CompartmentDefinitionResource, self).elementProperties()
        js.extend([
            ("code", "code", str, {  # #}False, None, {  # #}True),
            ("documentation", "documentation", str, {  # #}False, None, {  # #}False),
            ("param", "param", str, {  # #}True, None, {  # #}False),
        ])
        return js