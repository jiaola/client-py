#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/InsurancePlan) on 2019-07-18.
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
from .money import Money
from .period import Period
from .quantity import Quantity


@dataclass
class InsurancePlanPlanSpecificCostBenefitCost(BackboneElement):
    """ List of the costs.

    List of the costs associated with a specific benefit.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlanSpecificCostBenefitCost"
    applicability: Optional[CodeableConcept] = None
    qualifiers: Optional[List[CodeableConcept]] = empty_list()
    type: CodeableConcept = None
    value: Optional[Quantity] = None

    def elementProperties(self):
        js = super(InsurancePlanPlanSpecificCostBenefitCost, self).elementProperties()
        js.extend([
            ("applicability", "applicability", CodeableConcept, False, None, False),
            ("qualifiers", "qualifiers", CodeableConcept, True, None, False),
            ("type", "type", CodeableConcept, False, None, True),
            ("value", "value", Quantity, False, None, False),
        ])
        return js


@dataclass
class InsurancePlanPlanSpecificCostBenefit(BackboneElement):
    """ Benefits list.

    List of the specific benefits under this category of benefit.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlanSpecificCostBenefit"
    cost: Optional[List[InsurancePlanPlanSpecificCostBenefitCost]] = empty_list()
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(InsurancePlanPlanSpecificCostBenefit, self).elementProperties()
        js.extend([
            ("cost", "cost", InsurancePlanPlanSpecificCostBenefitCost, True, None, False),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class InsurancePlanPlanSpecificCost(BackboneElement):
    """ Specific costs.

    Costs associated with the coverage provided by the product.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlanSpecificCost"
    benefit: Optional[List[InsurancePlanPlanSpecificCostBenefit]] = empty_list()
    category: CodeableConcept = None

    def elementProperties(self):
        js = super(InsurancePlanPlanSpecificCost, self).elementProperties()
        js.extend([
            ("benefit", "benefit", InsurancePlanPlanSpecificCostBenefit, True, None, False),
            ("category", "category", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class InsurancePlanPlanGeneralCost(BackboneElement):
    """ Overall costs.

    Overall costs associated with the plan.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlanGeneralCost"
    comment: Optional[str] = None
    cost: Optional[Money] = None
    groupSize: Optional[int] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(InsurancePlanPlanGeneralCost, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("cost", "cost", Money, False, None, False),
            ("groupSize", "groupSize", int, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class InsurancePlanPlan(BackboneElement):
    """ Plan details.

    Details about an insurance plan.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlan"
    coverageArea: Optional[List[FHIRReference]] = empty_list()
    generalCost: Optional[List[InsurancePlanPlanGeneralCost]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    network: Optional[List[FHIRReference]] = empty_list()
    specificCost: Optional[List[InsurancePlanPlanSpecificCost]] = empty_list()
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(InsurancePlanPlan, self).elementProperties()
        js.extend([
            ("coverageArea", "coverageArea", FHIRReference, True, None, False),
            ("generalCost", "generalCost", InsurancePlanPlanGeneralCost, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("network", "network", FHIRReference, True, None, False),
            ("specificCost", "specificCost", InsurancePlanPlanSpecificCost, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class InsurancePlanCoverageBenefitLimit(BackboneElement):
    """ Benefit limits.

    The specific limits on the benefit.
    """
    resource_type: ClassVar[str] = "InsurancePlanCoverageBenefitLimit"
    code: Optional[CodeableConcept] = None
    value: Optional[Quantity] = None

    def elementProperties(self):
        js = super(InsurancePlanCoverageBenefitLimit, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("value", "value", Quantity, False, None, False),
        ])
        return js


@dataclass
class InsurancePlanCoverageBenefit(BackboneElement):
    """ List of benefits.

    Specific benefits under this type of coverage.
    """
    resource_type: ClassVar[str] = "InsurancePlanCoverageBenefit"
    limit: Optional[List[InsurancePlanCoverageBenefitLimit]] = empty_list()
    requirement: Optional[str] = None
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(InsurancePlanCoverageBenefit, self).elementProperties()
        js.extend([
            ("limit", "limit", InsurancePlanCoverageBenefitLimit, True, None, False),
            ("requirement", "requirement", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class InsurancePlanCoverage(BackboneElement):
    """ Coverage details.

    Details about the coverage offered by the insurance product.
    """
    resource_type: ClassVar[str] = "InsurancePlanCoverage"
    benefit: List[InsurancePlanCoverageBenefit] = empty_list()
    network: Optional[List[FHIRReference]] = empty_list()
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(InsurancePlanCoverage, self).elementProperties()
        js.extend([
            ("benefit", "benefit", InsurancePlanCoverageBenefit, True, None, True),
            ("network", "network", FHIRReference, True, None, False),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class InsurancePlanContact(BackboneElement):
    """ Contact for the product.

    The contact for the health insurance product for a certain purpose.
    """
    resource_type: ClassVar[str] = "InsurancePlanContact"
    address: Optional[Address] = None
    name: Optional[HumanName] = None
    purpose: Optional[CodeableConcept] = None
    telecom: Optional[List[ContactPoint]] = empty_list()

    def elementProperties(self):
        js = super(InsurancePlanContact, self).elementProperties()
        js.extend([
            ("address", "address", Address, False, None, False),
            ("name", "name", HumanName, False, None, False),
            ("purpose", "purpose", CodeableConcept, False, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
        ])
        return js


@dataclass
class InsurancePlan(DomainResource):
    """ Details of a Health Insurance product/plan provided by an organization.
    """
    resource_type: ClassVar[str] = "InsurancePlan"
    administeredBy: Optional[FHIRReference] = None
    alias: Optional[List[str]] = empty_list()
    contact: Optional[List[InsurancePlanContact]] = empty_list()
    coverage: Optional[List[InsurancePlanCoverage]] = empty_list()
    coverageArea: Optional[List[FHIRReference]] = empty_list()
    endpoint: Optional[List[FHIRReference]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    name: Optional[str] = None
    network: Optional[List[FHIRReference]] = empty_list()
    ownedBy: Optional[FHIRReference] = None
    period: Optional[Period] = None
    plan: Optional[List[InsurancePlanPlan]] = empty_list()
    status: Optional[str] = None
    type: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(InsurancePlan, self).elementProperties()
        js.extend([
            ("administeredBy", "administeredBy", FHIRReference, False, None, False),
            ("alias", "alias", str, True, None, False),
            ("contact", "contact", InsurancePlanContact, True, None, False),
            ("coverage", "coverage", InsurancePlanCoverage, True, None, False),
            ("coverageArea", "coverageArea", FHIRReference, True, None, False),
            ("endpoint", "endpoint", FHIRReference, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("name", "name", str, False, None, False),
            ("network", "network", FHIRReference, True, None, False),
            ("ownedBy", "ownedBy", FHIRReference, False, None, False),
            ("period", "period", Period, False, None, False),
            ("plan", "plan", InsurancePlanPlan, True, None, False),
            ("status", "status", str, False, None, False),
            ("type", "type", CodeableConcept, True, None, False),
        ])
        return js