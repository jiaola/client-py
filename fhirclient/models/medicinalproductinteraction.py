#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductInteraction) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference


@dataclass
class MedicinalProductInteractionInteractant(BackboneElement):
    """ The specific medication, food or laboratory test that interacts.
    """
    resource_type: ClassVar[str] = "MedicinalProductInteractionInteractant"
    itemCodeableConcept: CodeableConcept = None
    itemReference: FHIRReference = None

    def elementProperties(self):
        js = super(MedicinalProductInteractionInteractant, self).elementProperties()
        js.extend([
            ("itemCodeableConcept", "itemCodeableConcept", CodeableConcept, False, "item", True),
            ("itemReference", "itemReference", FHIRReference, False, "item", True),
        ])
        return js


@dataclass
class MedicinalProductInteraction(DomainResource):
    """ MedicinalProductInteraction.

    The interactions of the medicinal product with other medicinal products, or
    other forms of interactions.
    """
    resource_type: ClassVar[str] = "MedicinalProductInteraction"
    description: Optional[str] = None
    effect: Optional[CodeableConcept] = None
    incidence: Optional[CodeableConcept] = None
    interactant: Optional[List[MedicinalProductInteractionInteractant]] = empty_list()
    management: Optional[CodeableConcept] = None
    subject: Optional[List[FHIRReference]] = empty_list()
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(MedicinalProductInteraction, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("effect", "effect", CodeableConcept, False, None, False),
            ("incidence", "incidence", CodeableConcept, False, None, False),
            ("interactant", "interactant", MedicinalProductInteractionInteractant, True, None, False),
            ("management", "management", CodeableConcept, False, None, False),
            ("subject", "subject", FHIRReference, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js