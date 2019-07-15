#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SpecimenDefinition) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import duration
from . import fhirreference
from . import identifier
from . import quantity
from . import range

from . import domainresource

@dataclass
class SpecimenDefinition(domainresource.DomainResource):
    """ Kind of specimen.

    A kind of specimen with associated set of requirements.
    """
    resource_type: ClassVar[str] = "SpecimenDefinition"
    collection: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    identifier: Optional[identifier.Identifier] = None
    patientPreparation: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    timeAspect: Optional[str] = None
    typeCollected: Optional[codeableconcept.CodeableConcept] = None
    typeTested: Optional[List[SpecimenDefinitionTypeTested]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SpecimenDefinition, self).elementProperties()
        js.extend([
            ("collection", "collection", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("patientPreparation", "patientPreparation", codeableconcept.CodeableConcept, True, None, False),
            ("timeAspect", "timeAspect", str, False, None, False),
            ("typeCollected", "typeCollected", codeableconcept.CodeableConcept, False, None, False),
            ("typeTested", "typeTested", SpecimenDefinitionTypeTested, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class SpecimenDefinitionTypeTested(backboneelement.BackboneElement):
    """ Specimen in container intended for testing by lab.

    Specimen conditioned in a container as expected by the testing laboratory.
    """
    resource_type: ClassVar[str] = "SpecimenDefinitionTypeTested"
    container: Optional[SpecimenDefinitionTypeTestedContainer] = None
    handling: Optional[List[SpecimenDefinitionTypeTestedHandling]] = empty_list()
    isDerived: Optional[bool] = None
    preference: str = None
    rejectionCriterion: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    requirement: Optional[str] = None
    retentionTime: Optional[duration.Duration] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTested, self).elementProperties()
        js.extend([
            ("container", "container", SpecimenDefinitionTypeTestedContainer, False, None, False),
            ("handling", "handling", SpecimenDefinitionTypeTestedHandling, True, None, False),
            ("isDerived", "isDerived", bool, False, None, False),
            ("preference", "preference", str, False, None, True),
            ("rejectionCriterion", "rejectionCriterion", codeableconcept.CodeableConcept, True, None, False),
            ("requirement", "requirement", str, False, None, False),
            ("retentionTime", "retentionTime", duration.Duration, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class SpecimenDefinitionTypeTestedContainer(backboneelement.BackboneElement):
    """ The specimen's container.
    """
    resource_type: ClassVar[str] = "SpecimenDefinitionTypeTestedContainer"
    additive: Optional[List[SpecimenDefinitionTypeTestedContainerAdditive]] = empty_list()
    cap: Optional[codeableconcept.CodeableConcept] = None
    capacity: Optional[quantity.Quantity] = None
    description: Optional[str] = None
    material: Optional[codeableconcept.CodeableConcept] = None
    minimumVolumeQuantity: Optional[quantity.Quantity] = None
    minimumVolumeString: Optional[str] = None
    preparation: Optional[str] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedContainer, self).elementProperties()
        js.extend([
            ("additive", "additive", SpecimenDefinitionTypeTestedContainerAdditive, True, None, False),
            ("cap", "cap", codeableconcept.CodeableConcept, False, None, False),
            ("capacity", "capacity", quantity.Quantity, False, None, False),
            ("description", "description", str, False, None, False),
            ("material", "material", codeableconcept.CodeableConcept, False, None, False),
            ("minimumVolumeQuantity", "minimumVolumeQuantity", quantity.Quantity, False, "minimumVolume", False),
            ("minimumVolumeString", "minimumVolumeString", str, False, "minimumVolume", False),
            ("preparation", "preparation", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class SpecimenDefinitionTypeTestedContainerAdditive(backboneelement.BackboneElement):
    """ Additive associated with container.

    Substance introduced in the kind of container to preserve, maintain or
    enhance the specimen. Examples: Formalin, Citrate, EDTA.
    """
    resource_type: ClassVar[str] = "SpecimenDefinitionTypeTestedContainerAdditive"
    additiveCodeableConcept:codeableconcept.CodeableConcept = None
    additiveReference:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedContainerAdditive, self).elementProperties()
        js.extend([
            ("additiveCodeableConcept", "additiveCodeableConcept", codeableconcept.CodeableConcept, False, "additive", True),
            ("additiveReference", "additiveReference", fhirreference.FHIRReference, False, "additive", True),
        ])
        return js

@dataclass
class SpecimenDefinitionTypeTestedHandling(backboneelement.BackboneElement):
    """ Specimen handling before testing.

    Set of instructions for preservation/transport of the specimen at a defined
    temperature interval, prior the testing process.
    """
    resource_type: ClassVar[str] = "SpecimenDefinitionTypeTestedHandling"
    instruction: Optional[str] = None
    maxDuration: Optional[duration.Duration] = None
    temperatureQualifier: Optional[codeableconcept.CodeableConcept] = None
    temperatureRange: Optional[range.Range] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedHandling, self).elementProperties()
        js.extend([
            ("instruction", "instruction", str, False, None, False),
            ("maxDuration", "maxDuration", duration.Duration, False, None, False),
            ("temperatureQualifier", "temperatureQualifier", codeableconcept.CodeableConcept, False, None, False),
            ("temperatureRange", "temperatureRange", range.Range, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']