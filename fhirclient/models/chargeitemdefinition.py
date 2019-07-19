#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ChargeItemDefinition) on 2019-07-18.
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
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .period import Period
from .usagecontext import UsageContext


@dataclass
class ChargeItemDefinitionPropertyGroupPriceComponent(BackboneElement):
    """ Components of total line item price.

    The price for a ChargeItem may be calculated as a base price with
    surcharges/deductions that apply in certain conditions. A
    ChargeItemDefinition resource that defines the prices, factors and
    conditions that apply to a billing code is currently under development. The
    priceComponent element can be used to offer transparency to the recipient
    of the Invoice of how the prices have been calculated.
    """
    resource_type: ClassVar[str] = "ChargeItemDefinitionPropertyGroupPriceComponent"
    amount: Optional[Money] = None
    code: Optional[CodeableConcept] = None
    factor: Optional[float] = None
    type: str = None

    def elementProperties(self):
        js = super(ChargeItemDefinitionPropertyGroupPriceComponent, self).elementProperties()
        js.extend([
            ("amount", "amount", Money, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


@dataclass
class ChargeItemDefinitionPropertyGroup(BackboneElement):
    """ Group of properties which are applicable under the same conditions.

    Group of properties which are applicable under the same conditions. If no
    applicability rules are established for the group, then all properties
    always apply.
    """
    resource_type: ClassVar[str] = "ChargeItemDefinitionPropertyGroup"
    applicability: Optional[List[ChargeItemDefinitionApplicability]] = empty_list()
    priceComponent: Optional[List[ChargeItemDefinitionPropertyGroupPriceComponent]] = empty_list()

    def elementProperties(self):
        js = super(ChargeItemDefinitionPropertyGroup, self).elementProperties()
        js.extend([
            ("applicability", "applicability", ChargeItemDefinitionApplicability, True, None, False),
            ("priceComponent", "priceComponent", ChargeItemDefinitionPropertyGroupPriceComponent, True, None, False),
        ])
        return js


@dataclass
class ChargeItemDefinitionApplicability(BackboneElement):
    """ Whether or not the billing code is applicable.

    Expressions that describe applicability criteria for the billing code.
    """
    resource_type: ClassVar[str] = "ChargeItemDefinitionApplicability"
    description: Optional[str] = None
    expression: Optional[str] = None
    language: Optional[str] = None

    def elementProperties(self):
        js = super(ChargeItemDefinitionApplicability, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("language", "language", str, False, None, False),
        ])
        return js


@dataclass
class ChargeItemDefinition(DomainResource):
    """ Definition of properties and rules about how the price and the
    applicability of a ChargeItem can be determined.

    The ChargeItemDefinition resource provides the properties that apply to the
    (billing) codes necessary to calculate costs and prices. The properties may
    differ largely depending on type and realm, therefore this resource gives
    only a rough structure and requires profiling for each type of billing code
    system.
    """
    resource_type: ClassVar[str] = "ChargeItemDefinition"
    applicability: Optional[List[ChargeItemDefinitionApplicability]] = empty_list()
    approvalDate: Optional[FHIRDate] = None
    code: Optional[CodeableConcept] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[FHIRDate] = None
    derivedFromUri: Optional[List[str]] = empty_list()
    description: Optional[str] = None
    effectivePeriod: Optional[Period] = None
    experimental: Optional[bool] = None
    identifier: Optional[List[Identifier]] = empty_list()
    instance: Optional[List[FHIRReference]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    lastReviewDate: Optional[FHIRDate] = None
    partOf: Optional[List[str]] = empty_list()
    propertyGroup: Optional[List[ChargeItemDefinitionPropertyGroup]] = empty_list()
    publisher: Optional[str] = None
    replaces: Optional[List[str]] = empty_list()
    status: str = None
    title: Optional[str] = None
    url: str = None
    useContext: Optional[List[UsageContext]] = empty_list()
    version: Optional[str] = None

    def elementProperties(self):
        js = super(ChargeItemDefinition, self).elementProperties()
        js.extend([
            ("applicability", "applicability", ChargeItemDefinitionApplicability, True, None, False),
            ("approvalDate", "approvalDate", FHIRDate, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("derivedFromUri", "derivedFromUri", str, True, None, False),
            ("description", "description", str, False, None, False),
            ("effectivePeriod", "effectivePeriod", Period, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("instance", "instance", FHIRReference, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", FHIRDate, False, None, False),
            ("partOf", "partOf", str, True, None, False),
            ("propertyGroup", "propertyGroup", ChargeItemDefinitionPropertyGroup, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("replaces", "replaces", str, True, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js