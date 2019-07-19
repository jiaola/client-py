#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductPharmaceutical) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .duration import Duration
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .ratio import Ratio


@dataclass
class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod(BackboneElement):
    """ A species specific time during which consumption of animal product is not
    appropriate.
    """
    resource_type: ClassVar[str] = "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod"
    supportingInformation: Optional[str] = None
    tissue: CodeableConcept = None
    value: Quantity = None

    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod, self).elementProperties()
        js.extend([
            ("supportingInformation", "supportingInformation", str, False, None, False),
            ("tissue", "tissue", CodeableConcept, False, None, True),
            ("value", "value", Quantity, False, None, True),
        ])
        return js


@dataclass
class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies(BackboneElement):
    """ A species for which this route applies.
    """
    resource_type: ClassVar[str] = "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies"
    code: CodeableConcept = None
    withdrawalPeriod: Optional[List[MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod]] = empty_list()

    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("withdrawalPeriod", "withdrawalPeriod", MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod, True, None, False),
        ])
        return js


@dataclass
class MedicinalProductPharmaceuticalRouteOfAdministration(BackboneElement):
    """ The path by which the pharmaceutical product is taken into or makes contact
    with the body.
    """
    resource_type: ClassVar[str] = "MedicinalProductPharmaceuticalRouteOfAdministration"
    code: CodeableConcept = None
    firstDose: Optional[Quantity] = None
    maxDosePerDay: Optional[Quantity] = None
    maxDosePerTreatmentPeriod: Optional[Ratio] = None
    maxSingleDose: Optional[Quantity] = None
    maxTreatmentPeriod: Optional[Duration] = None
    targetSpecies: Optional[List[MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies]] = empty_list()

    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalRouteOfAdministration, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("firstDose", "firstDose", Quantity, False, None, False),
            ("maxDosePerDay", "maxDosePerDay", Quantity, False, None, False),
            ("maxDosePerTreatmentPeriod", "maxDosePerTreatmentPeriod", Ratio, False, None, False),
            ("maxSingleDose", "maxSingleDose", Quantity, False, None, False),
            ("maxTreatmentPeriod", "maxTreatmentPeriod", Duration, False, None, False),
            ("targetSpecies", "targetSpecies", MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies, True, None, False),
        ])
        return js


@dataclass
class MedicinalProductPharmaceuticalCharacteristics(BackboneElement):
    """ Characteristics e.g. a products onset of action.
    """
    resource_type: ClassVar[str] = "MedicinalProductPharmaceuticalCharacteristics"
    code: CodeableConcept = None
    status: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalCharacteristics, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("status", "status", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class MedicinalProductPharmaceutical(DomainResource):
    """ A pharmaceutical product described in terms of its composition and dose
    form.
    """
    resource_type: ClassVar[str] = "MedicinalProductPharmaceutical"
    administrableDoseForm: CodeableConcept = None
    characteristics: Optional[List[MedicinalProductPharmaceuticalCharacteristics]] = empty_list()
    device: Optional[List[FHIRReference]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    ingredient: Optional[List[FHIRReference]] = empty_list()
    routeOfAdministration: List[MedicinalProductPharmaceuticalRouteOfAdministration] = empty_list()
    unitOfPresentation: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(MedicinalProductPharmaceutical, self).elementProperties()
        js.extend([
            ("administrableDoseForm", "administrableDoseForm", CodeableConcept, False, None, True),
            ("characteristics", "characteristics", MedicinalProductPharmaceuticalCharacteristics, True, None, False),
            ("device", "device", FHIRReference, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("ingredient", "ingredient", FHIRReference, True, None, False),
            ("routeOfAdministration", "routeOfAdministration", MedicinalProductPharmaceuticalRouteOfAdministration, True, None, True),
            ("unitOfPresentation", "unitOfPresentation", CodeableConcept, False, None, False),
        ])
        return js