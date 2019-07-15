#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/InsurancePlan) on 2019-07-15.
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
from . import money
from . import period
from . import quantity

from . import domainresource

@dataclass
class InsurancePlan(domainresource.DomainResource):
    """ Details of a Health Insurance product/plan provided by an organization.
    """
    resource_type: ClassVar[str] = "InsurancePlan"
    administeredBy: Optional[fhirreference.FHIRReference] = None
    alias: Optional[List[str]] = empty_list()
    contact: Optional[List[InsurancePlanContact]] = empty_list()
    coverage: Optional[List[InsurancePlanCoverage]] = empty_list()
    coverageArea: Optional[List[fhirreference.FHIRReference]] = empty_list()
    endpoint: Optional[List[fhirreference.FHIRReference]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    name: Optional[str] = None
    network: Optional[List[fhirreference.FHIRReference]] = empty_list()
    ownedBy: Optional[fhirreference.FHIRReference] = None
    period: Optional[period.Period] = None
    plan: Optional[List[InsurancePlanPlan]] = empty_list()
    status: Optional[str] = None
    type: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(InsurancePlan, self).elementProperties()
        js.extend([
            ("administeredBy", "administeredBy", fhirreference.FHIRReference, False, None, False),
            ("alias", "alias", str, True, None, False),
            ("contact", "contact", InsurancePlanContact, True, None, False),
            ("coverage", "coverage", InsurancePlanCoverage, True, None, False),
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, True, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", str, False, None, False),
            ("network", "network", fhirreference.FHIRReference, True, None, False),
            ("ownedBy", "ownedBy", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("plan", "plan", InsurancePlanPlan, True, None, False),
            ("status", "status", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class InsurancePlanContact(backboneelement.BackboneElement):
    """ Contact for the product.

    The contact for the health insurance product for a certain purpose.
    """
    resource_type: ClassVar[str] = "InsurancePlanContact"
    address: Optional[address.Address] = None
    name: Optional[humanname.HumanName] = None
    purpose: Optional[codeableconcept.CodeableConcept] = None
    telecom: Optional[List[contactpoint.ContactPoint]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(InsurancePlanContact, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("name", "name", humanname.HumanName, False, None, False),
            ("purpose", "purpose", codeableconcept.CodeableConcept, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js

@dataclass
class InsurancePlanCoverage(backboneelement.BackboneElement):
    """ Coverage details.

    Details about the coverage offered by the insurance product.
    """
    resource_type: ClassVar[str] = "InsurancePlanCoverage"
    benefit: List[ InsurancePlanCoverageBenefit] = empty_list()
    network: Optional[List[fhirreference.FHIRReference]] = empty_list()
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(InsurancePlanCoverage, self).elementProperties()
        js.extend([
            ("benefit", "benefit", InsurancePlanCoverageBenefit, True, None, True),
            ("network", "network", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class InsurancePlanCoverageBenefit(backboneelement.BackboneElement):
    """ List of benefits.

    Specific benefits under this type of coverage.
    """
    resource_type: ClassVar[str] = "InsurancePlanCoverageBenefit"
    limit: Optional[List[InsurancePlanCoverageBenefitLimit]] = empty_list()
    requirement: Optional[str] = None
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(InsurancePlanCoverageBenefit, self).elementProperties()
        js.extend([
            ("limit", "limit", InsurancePlanCoverageBenefitLimit, True, None, False),
            ("requirement", "requirement", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class InsurancePlanCoverageBenefitLimit(backboneelement.BackboneElement):
    """ Benefit limits.

    The specific limits on the benefit.
    """
    resource_type: ClassVar[str] = "InsurancePlanCoverageBenefitLimit"
    code: Optional[codeableconcept.CodeableConcept] = None
    value: Optional[quantity.Quantity] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(InsurancePlanCoverageBenefitLimit, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", quantity.Quantity, False, None, False),
        ])
        return js

@dataclass
class InsurancePlanPlan(backboneelement.BackboneElement):
    """ Plan details.

    Details about an insurance plan.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlan"
    coverageArea: Optional[List[fhirreference.FHIRReference]] = empty_list()
    generalCost: Optional[List[InsurancePlanPlanGeneralCost]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    network: Optional[List[fhirreference.FHIRReference]] = empty_list()
    specificCost: Optional[List[InsurancePlanPlanSpecificCost]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(InsurancePlanPlan, self).elementProperties()
        js.extend([
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, True, None, False),
            ("generalCost", "generalCost", InsurancePlanPlanGeneralCost, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("network", "network", fhirreference.FHIRReference, True, None, False),
            ("specificCost", "specificCost", InsurancePlanPlanSpecificCost, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class InsurancePlanPlanGeneralCost(backboneelement.BackboneElement):
    """ Overall costs.

    Overall costs associated with the plan.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlanGeneralCost"
    comment: Optional[str] = None
    cost: Optional[money.Money] = None
    groupSize: Optional[int] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(InsurancePlanPlanGeneralCost, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("cost", "cost", money.Money, False, None, False),
            ("groupSize", "groupSize", int, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class InsurancePlanPlanSpecificCost(backboneelement.BackboneElement):
    """ Specific costs.

    Costs associated with the coverage provided by the product.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlanSpecificCost"
    benefit: Optional[List[InsurancePlanPlanSpecificCostBenefit]] = empty_list()
    category:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(InsurancePlanPlanSpecificCost, self).elementProperties()
        js.extend([
            ("benefit", "benefit", InsurancePlanPlanSpecificCostBenefit, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class InsurancePlanPlanSpecificCostBenefit(backboneelement.BackboneElement):
    """ Benefits list.

    List of the specific benefits under this category of benefit.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlanSpecificCostBenefit"
    cost: Optional[List[InsurancePlanPlanSpecificCostBenefitCost]] = empty_list()
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(InsurancePlanPlanSpecificCostBenefit, self).elementProperties()
        js.extend([
            ("cost", "cost", InsurancePlanPlanSpecificCostBenefitCost, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class InsurancePlanPlanSpecificCostBenefitCost(backboneelement.BackboneElement):
    """ List of the costs.

    List of the costs associated with a specific benefit.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlanSpecificCostBenefitCost"
    applicability: Optional[codeableconcept.CodeableConcept] = None
    qualifiers: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    type:codeableconcept.CodeableConcept = None
    value: Optional[quantity.Quantity] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(InsurancePlanPlanSpecificCostBenefitCost, self).elementProperties()
        js.extend([
            ("applicability", "applicability", codeableconcept.CodeableConcept, False, None, False),
            ("qualifiers", "qualifiers", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", quantity.Quantity, False, None, False),
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
try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']