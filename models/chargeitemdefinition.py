#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ChargeItemDefinition) on 2019-07-15.
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
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import usagecontext

from . import domainresource

@dataclass
class ChargeItemDefinition(domainresource.DomainResource):
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
    approvalDate: Optional[fhirdate.FHIRDate] = None
    code: Optional[codeableconcept.CodeableConcept] = None
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[fhirdate.FHIRDate] = None
    derivedFromUri: Optional[List[str]] = empty_list()
    description: Optional[str] = None
    effectivePeriod: Optional[period.Period] = None
    experimental: Optional[bool] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    instance: Optional[List[fhirreference.FHIRReference]] = empty_list()
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    lastReviewDate: Optional[fhirdate.FHIRDate] = None
    partOf: Optional[List[str]] = empty_list()
    propertyGroup: Optional[List[ChargeItemDefinitionPropertyGroup]] = empty_list()
    publisher: Optional[str] = None
    replaces: Optional[List[str]] = empty_list()
    status: str = None
    title: Optional[str] = None
    url: str = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ChargeItemDefinition, self).elementProperties()
        js.extend([
            ("applicability", "applicability", ChargeItemDefinitionApplicability, True, None, False),
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("derivedFromUri", "derivedFromUri", str, True, None, False),
            ("description", "description", str, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instance", "instance", fhirreference.FHIRReference, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("partOf", "partOf", str, True, None, False),
            ("propertyGroup", "propertyGroup", ChargeItemDefinitionPropertyGroup, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("replaces", "replaces", str, True, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class ChargeItemDefinitionApplicability(backboneelement.BackboneElement):
    """ Whether or not the billing code is applicable.

    Expressions that describe applicability criteria for the billing code.
    """
    resource_type: ClassVar[str] = "ChargeItemDefinitionApplicability"
    description: Optional[str] = None
    expression: Optional[str] = None
    language: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ChargeItemDefinitionApplicability, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("language", "language", str, False, None, False),
        ])
        return js

@dataclass
class ChargeItemDefinitionPropertyGroup(backboneelement.BackboneElement):
    """ Group of properties which are applicable under the same conditions.

    Group of properties which are applicable under the same conditions. If no
    applicability rules are established for the group, then all properties
    always apply.
    """
    resource_type: ClassVar[str] = "ChargeItemDefinitionPropertyGroup"
    applicability: Optional[List[ChargeItemDefinitionApplicability]] = empty_list()
    priceComponent: Optional[List[ChargeItemDefinitionPropertyGroupPriceComponent]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ChargeItemDefinitionPropertyGroup, self).elementProperties()
        js.extend([
            ("applicability", "applicability", ChargeItemDefinitionApplicability, True, None, False),
            ("priceComponent", "priceComponent", ChargeItemDefinitionPropertyGroupPriceComponent, True, None, False),
        ])
        return js

@dataclass
class ChargeItemDefinitionPropertyGroupPriceComponent(backboneelement.BackboneElement):
    """ Components of total line item price.

    The price for a ChargeItem may be calculated as a base price with
    surcharges/deductions that apply in certain conditions. A
    ChargeItemDefinition resource that defines the prices, factors and
    conditions that apply to a billing code is currently under development. The
    priceComponent element can be used to offer transparency to the recipient
    of the Invoice of how the prices have been calculated.
    """
    resource_type: ClassVar[str] = "ChargeItemDefinitionPropertyGroupPriceComponent"
    amount: Optional[money.Money] = None
    code: Optional[codeableconcept.CodeableConcept] = None
    factor: Optional[float] = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ChargeItemDefinitionPropertyGroupPriceComponent, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("type", "type", str, False, None, True),
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
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']