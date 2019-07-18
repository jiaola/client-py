#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Organization) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import backboneelement
from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirreference
from . import humanname
from . import identifier

from . import backboneelement

@dataclass
class OrganizationContact(backboneelement.BackboneElement):
    """ Contact for the organization for a certain purpose.
    """
    resource_type: ClassVar[str] = "OrganizationContact"
    address: Optional[address.Address] = None
    name: Optional[humanname.HumanName] = None
    purpose: Optional[codeableconcept.CodeableConcept] = None
    telecom: Optional[List[contactpoint.ContactPoint]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(OrganizationContact, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("name", "name", humanname.HumanName, False, None, False),
            ("purpose", "purpose", codeableconcept.CodeableConcept, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js

from . import domainresource

@dataclass
class Organization(domainresource.DomainResource):
    """ A grouping of people or organizations with a common purpose.

    A formally or informally recognized grouping of people or organizations
    formed for the purpose of achieving some form of collective action.
    Includes companies, institutions, corporations, departments, community
    groups, healthcare practice groups, payer/insurer, etc.
    """
    resource_type: ClassVar[str] = "Organization"
    active: Optional[bool] = None
    address: Optional[List[address.Address]] = empty_list()
    alias: Optional[List[str]] = empty_list()
    contact: Optional[List[OrganizationContact]] = empty_list()
    endpoint: Optional[List[fhirreference.FHIRReference]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    name: Optional[str] = None
    partOf: Optional[fhirreference.FHIRReference] = None
    telecom: Optional[List[contactpoint.ContactPoint]] = empty_list()
    type: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Organization, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("alias", "alias", str, True, None, False),
            ("contact", "contact", OrganizationContact, True, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", str, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import humanname
except ImportError:
    humanname = sys.modules[__package__ + '.humanname']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']