#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SpecimenDefinition) on 2019-07-29.
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
from .range import Range


@dataclass
class SpecimenDefinitionTypeTestedContainerAdditive(BackboneElement):
    """ Additive associated with container.

    Substance introduced in the kind of container to preserve, maintain or
    enhance the specimen. Examples: Formalin, Citrate, EDTA.
    """
    resource_type: ClassVar[str] = "SpecimenDefinitionTypeTestedContainerAdditive"
    additiveCodeableConcept: CodeableConcept = None
    additiveReference: FHIRReference = None

    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedContainerAdditive, self).elementProperties()
        js.extend([
            ("additiveCodeableConcept", "additiveCodeableConcept", CodeableConcept, False, "additive", True),
            ("additiveReference", "additiveReference", FHIRReference, False, "additive", True),
        ])
        return js


@dataclass
class SpecimenDefinitionTypeTestedContainer(BackboneElement):
    """ The specimen's container.
    """
    resource_type: ClassVar[str] = "SpecimenDefinitionTypeTestedContainer"
    material: Optional[CodeableConcept] = None
    type: Optional[CodeableConcept] = None
    cap: Optional[CodeableConcept] = None
    description: Optional[str] = None
    capacity: Optional[Quantity] = None
    minimumVolumeQuantity: Optional[Quantity] = None
    minimumVolumeString: Optional[str] = None
    additive: Optional[List[SpecimenDefinitionTypeTestedContainerAdditive]] = empty_list()
    preparation: Optional[str] = None

    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedContainer, self).elementProperties()
        js.extend([
            ("material", "material", CodeableConcept, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("cap", "cap", CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("capacity", "capacity", Quantity, False, None, False),
            ("minimumVolumeQuantity", "minimumVolumeQuantity", Quantity, False, "minimumVolume", False),
            ("minimumVolumeString", "minimumVolumeString", str, False, "minimumVolume", False),
            ("additive", "additive", SpecimenDefinitionTypeTestedContainerAdditive, True, None, False),
            ("preparation", "preparation", str, False, None, False),
        ])
        return js


@dataclass
class SpecimenDefinitionTypeTestedHandling(BackboneElement):
    """ Specimen handling before testing.

    Set of instructions for preservation/transport of the specimen at a defined
    temperature interval, prior the testing process.
    """
    resource_type: ClassVar[str] = "SpecimenDefinitionTypeTestedHandling"
    temperatureQualifier: Optional[CodeableConcept] = None
    temperatureRange: Optional[Range] = None
    maxDuration: Optional[Duration] = None
    instruction: Optional[str] = None

    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedHandling, self).elementProperties()
        js.extend([
            ("temperatureQualifier", "temperatureQualifier", CodeableConcept, False, None, False),
            ("temperatureRange", "temperatureRange", Range, False, None, False),
            ("maxDuration", "maxDuration", Duration, False, None, False),
            ("instruction", "instruction", str, False, None, False),
        ])
        return js


@dataclass
class SpecimenDefinitionTypeTested(BackboneElement):
    """ Specimen in container intended for testing by lab.

    Specimen conditioned in a container as expected by the testing laboratory.
    """
    resource_type: ClassVar[str] = "SpecimenDefinitionTypeTested"
    isDerived: Optional[bool] = None
    type: Optional[CodeableConcept] = None
    preference: str = None
    container: Optional[SpecimenDefinitionTypeTestedContainer] = None
    requirement: Optional[str] = None
    retentionTime: Optional[Duration] = None
    rejectionCriterion: Optional[List[CodeableConcept]] = empty_list()
    handling: Optional[List[SpecimenDefinitionTypeTestedHandling]] = empty_list()

    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTested, self).elementProperties()
        js.extend([
            ("isDerived", "isDerived", bool, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("preference", "preference", str, False, None, True),
            ("container", "container", SpecimenDefinitionTypeTestedContainer, False, None, False),
            ("requirement", "requirement", str, False, None, False),
            ("retentionTime", "retentionTime", Duration, False, None, False),
            ("rejectionCriterion", "rejectionCriterion", CodeableConcept, True, None, False),
            ("handling", "handling", SpecimenDefinitionTypeTestedHandling, True, None, False),
        ])
        return js


@dataclass
class SpecimenDefinition(DomainResource):
    """ Kind of specimen.

    A kind of specimen with associated set of requirements.
    """
    resource_type: ClassVar[str] = "SpecimenDefinition"
    identifier: Optional[Identifier] = None
    typeCollected: Optional[CodeableConcept] = None
    patientPreparation: Optional[List[CodeableConcept]] = empty_list()
    timeAspect: Optional[str] = None
    collection: Optional[List[CodeableConcept]] = empty_list()
    typeTested: Optional[List[SpecimenDefinitionTypeTested]] = empty_list()

    def elementProperties(self):
        js = super(SpecimenDefinition, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, False, None, False),
            ("typeCollected", "typeCollected", CodeableConcept, False, None, False),
            ("patientPreparation", "patientPreparation", CodeableConcept, True, None, False),
            ("timeAspect", "timeAspect", str, False, None, False),
            ("collection", "collection", CodeableConcept, True, None, False),
            ("typeTested", "typeTested", SpecimenDefinitionTypeTested, True, None, False),
        ])
        return js