#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductInteraction) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirreference

from . import backboneelement

@dataclass
class MedicinalProductInteractionInteractant(backboneelement.BackboneElement):
    """ The specific medication, food or laboratory test that interacts.
    """
    resource_type: ClassVar[str] = "MedicinalProductInteractionInteractant"
    itemCodeableConcept:codeableconcept.CodeableConcept = None
    itemReference:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductInteractionInteractant, self).elementProperties()
        js.extend([
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True),
        ])
        return js

from . import domainresource

@dataclass
class MedicinalProductInteraction(domainresource.DomainResource):
    """ MedicinalProductInteraction.

    The interactions of the medicinal product with other medicinal products, or
    other forms of interactions.
    """
    resource_type: ClassVar[str] = "MedicinalProductInteraction"
    description: Optional[str] = None
    effect: Optional[codeableconcept.CodeableConcept] = None
    incidence: Optional[codeableconcept.CodeableConcept] = None
    interactant: Optional[List[MedicinalProductInteractionInteractant]] = empty_list()
    management: Optional[codeableconcept.CodeableConcept] = None
    subject: Optional[List[fhirreference.FHIRReference]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductInteraction, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("effect", "effect", codeableconcept.CodeableConcept, False, None, False),
            ("incidence", "incidence", codeableconcept.CodeableConcept, False, None, False),
            ("interactant", "interactant", MedicinalProductInteractionInteractant, True, None, False),
            ("management", "management", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']