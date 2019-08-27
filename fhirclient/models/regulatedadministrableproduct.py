#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/RegulatedAdministrableProduct) on 2019-08-26.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .duration import Duration
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .ratio import Ratio


@dataclass
class RegulatedAdministrableProductRouteOfAdministrationTargetSpeciesWithdrawalPeriod(BackboneElement):
    """ A species specific time during which consumption of animal product is not
    appropriate.
    """
    resource_type: ClassVar[str] = "RegulatedAdministrableProductRouteOfAdministrationTargetSpeciesWithdrawalPeriod"

    tissue: CodeableConcept = None
    value: Quantity = None
    supportingInformation: Optional[str] = None


@dataclass
class RegulatedAdministrableProductRouteOfAdministrationTargetSpecies(BackboneElement):
    """ A species for which this route applies.
    """
    resource_type: ClassVar[str] = "RegulatedAdministrableProductRouteOfAdministrationTargetSpecies"

    code: CodeableConcept = None
    withdrawalPeriod: Optional[List[RegulatedAdministrableProductRouteOfAdministrationTargetSpeciesWithdrawalPeriod]] = None


@dataclass
class RegulatedAdministrableProductCharacteristics(BackboneElement):
    """ Characteristics e.g. a products onset of action.
    """
    resource_type: ClassVar[str] = "RegulatedAdministrableProductCharacteristics"

    code: CodeableConcept = None
    status: Optional[CodeableConcept] = None


@dataclass
class RegulatedAdministrableProductRouteOfAdministration(BackboneElement):
    """ The path by which the pharmaceutical product is taken into or makes contact
    with the body.
    """
    resource_type: ClassVar[str] = "RegulatedAdministrableProductRouteOfAdministration"

    code: CodeableConcept = None
    firstDose: Optional[Quantity] = None
    maxSingleDose: Optional[Quantity] = None
    maxDosePerDay: Optional[Quantity] = None
    maxDosePerTreatmentPeriod: Optional[Ratio] = None
    maxTreatmentPeriod: Optional[Duration] = None
    targetSpecies: Optional[List[RegulatedAdministrableProductRouteOfAdministrationTargetSpecies]] = None


@dataclass
class RegulatedAdministrableProduct(DomainResource):
    """ A pharmaceutical product described in terms of its composition and dose
    form.
    """
    resource_type: ClassVar[str] = "RegulatedAdministrableProduct"

    identifier: Optional[List[Identifier]] = None
    subject: Optional[List[FHIRReference]] = None
    administrableDoseForm: CodeableConcept = None
    unitOfPresentation: Optional[CodeableConcept] = None
    ingredient: Optional[List[FHIRReference]] = None
    device: Optional[List[FHIRReference]] = None
    characteristics: Optional[List[RegulatedAdministrableProductCharacteristics]] = None
    routeOfAdministration: List[RegulatedAdministrableProductRouteOfAdministration] = field(default_factory=list)