#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Organization) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .address import Address
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .humanname import HumanName
from .identifier import Identifier


@dataclass
class OrganizationContact(BackboneElement):
    """ Contact for the organization for a certain purpose.
    """
    resource_type: ClassVar[str] = "OrganizationContact"
    address: Optional[Address] = None
    name: Optional[HumanName] = None
    purpose: Optional[CodeableConcept] = None
    telecom: Optional[List[ContactPoint]] = empty_list()

    def elementProperties(self):
        js = super(OrganizationContact, self).elementProperties()
        js.extend([
            ("address", "address", Address, False, None, False),
            ("name", "name", HumanName, False, None, False),
            ("purpose", "purpose", CodeableConcept, False, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
        ])
        return js


@dataclass
class Organization(DomainResource):
    """ A grouping of people or organizations with a common purpose.

    A formally or informally recognized grouping of people or organizations
    formed for the purpose of achieving some form of collective action.
    Includes companies, institutions, corporations, departments, community
    groups, healthcare practice groups, payer/insurer, etc.
    """
    resource_type: ClassVar[str] = "Organization"
    active: Optional[bool] = None
    address: Optional[List[Address]] = empty_list()
    alias: Optional[List[str]] = empty_list()
    contact: Optional[List[OrganizationContact]] = empty_list()
    endpoint: Optional[List[FHIRReference]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    name: Optional[str] = None
    partOf: Optional[FHIRReference] = None
    telecom: Optional[List[ContactPoint]] = empty_list()
    type: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(Organization, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("address", "address", Address, True, None, False),
            ("alias", "alias", str, True, None, False),
            ("contact", "contact", OrganizationContact, True, None, False),
            ("endpoint", "endpoint", FHIRReference, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("name", "name", str, False, None, False),
            ("partOf", "partOf", FHIRReference, False, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
            ("type", "type", CodeableConcept, True, None, False),
        ])
        return js