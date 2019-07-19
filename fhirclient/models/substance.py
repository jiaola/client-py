#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Substance) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .ratio import Ratio


@dataclass
class SubstanceInstance(BackboneElement):
    """ If this describes a specific package/container of the substance.

    Substance may be used to describe a kind of substance, or a specific
    package/container of the substance: an instance.
    """
    resource_type: ClassVar[str] = "SubstanceInstance"
    expiry: Optional[FHIRDate] = None
    identifier: Optional[Identifier] = None
    quantity: Optional[Quantity] = None

    def elementProperties(self):
        js = super(SubstanceInstance, self).elementProperties()
        js.extend([
            ("expiry", "expiry", FHIRDate, False, None, False),
            ("identifier", "identifier", Identifier, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
        ])
        return js


@dataclass
class SubstanceIngredient(BackboneElement):
    """ Composition information about the substance.

    A substance can be composed of other substances.
    """
    resource_type: ClassVar[str] = "SubstanceIngredient"
    quantity: Optional[Ratio] = None
    substanceCodeableConcept: CodeableConcept = None
    substanceReference: FHIRReference = None

    def elementProperties(self):
        js = super(SubstanceIngredient, self).elementProperties()
        js.extend([
            ("quantity", "quantity", Ratio, False, None, False),
            ("substanceCodeableConcept", "substanceCodeableConcept", CodeableConcept, False, "substance", True),
            ("substanceReference", "substanceReference", FHIRReference, False, "substance", True),
        ])
        return js


@dataclass
class Substance(DomainResource):
    """ A homogeneous material with a definite composition.
    """
    resource_type: ClassVar[str] = "Substance"
    category: Optional[List[CodeableConcept]] = empty_list()
    code: CodeableConcept = None
    description: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    ingredient: Optional[List[SubstanceIngredient]] = empty_list()
    instance: Optional[List[SubstanceInstance]] = empty_list()
    status: Optional[str] = None

    def elementProperties(self):
        js = super(Substance, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, True, None, False),
            ("code", "code", CodeableConcept, False, None, True),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("ingredient", "ingredient", SubstanceIngredient, True, None, False),
            ("instance", "instance", SubstanceInstance, True, None, False),
            ("status", "status", str, False, None, False),
        ])
        return js