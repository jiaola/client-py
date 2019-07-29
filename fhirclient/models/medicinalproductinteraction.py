#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductInteraction) on 2019-07-29.
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
    itemReference: FHIRReference = None
    itemCodeableConcept: CodeableConcept = None

    def elementProperties(self):
        js = super(MedicinalProductInteractionInteractant, self).elementProperties()
        js.extend([
            ("itemReference", "itemReference", FHIRReference, False, "item", True),
            ("itemCodeableConcept", "itemCodeableConcept", CodeableConcept, False, "item", True),
        ])
        return js


@dataclass
class MedicinalProductInteraction(DomainResource):
    """ MedicinalProductInteraction.

    The interactions of the medicinal product with other medicinal products, or
    other forms of interactions.
    """
    resource_type: ClassVar[str] = "MedicinalProductInteraction"
    subject: Optional[List[FHIRReference]] = empty_list()
    description: Optional[str] = None
    interactant: Optional[List[MedicinalProductInteractionInteractant]] = empty_list()
    type: Optional[CodeableConcept] = None
    effect: Optional[CodeableConcept] = None
    incidence: Optional[CodeableConcept] = None
    management: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(MedicinalProductInteraction, self).elementProperties()
        js.extend([
            ("subject", "subject", FHIRReference, True, None, False),
            ("description", "description", str, False, None, False),
            ("interactant", "interactant", MedicinalProductInteractionInteractant, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("effect", "effect", CodeableConcept, False, None, False),
            ("incidence", "incidence", CodeableConcept, False, None, False),
            ("management", "management", CodeableConcept, False, None, False),
        ])
        return js