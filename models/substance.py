#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Substance) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio

from . import domainresource

@dataclass
class Substance(domainresource.DomainResource):
    """ A homogeneous material with a definite composition.
    """
    resource_type: ClassVar[str] = "Substance"
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    code:codeableconcept.CodeableConcept = None
    description: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    ingredient: Optional[List[SubstanceIngredient]] = empty_list()
    instance: Optional[List[SubstanceInstance]] = empty_list()
    status: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Substance, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("ingredient", "ingredient", SubstanceIngredient, True, None, False),
            ("instance", "instance", SubstanceInstance, True, None, False),
            ("status", "status", str, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class SubstanceIngredient(backboneelement.BackboneElement):
    """ Composition information about the substance.

    A substance can be composed of other substances.
    """
    resource_type: ClassVar[str] = "SubstanceIngredient"
    quantity: Optional[ratio.Ratio] = None
    substanceCodeableConcept:codeableconcept.CodeableConcept = None
    substanceReference:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceIngredient, self).elementProperties()
        js.extend([
            ("quantity", "quantity", ratio.Ratio, False, None, False),
            ("substanceCodeableConcept", "substanceCodeableConcept", codeableconcept.CodeableConcept, False, "substance", True),
            ("substanceReference", "substanceReference", fhirreference.FHIRReference, False, "substance", True),
        ])
        return js

@dataclass
class SubstanceInstance(backboneelement.BackboneElement):
    """ If this describes a specific package/container of the substance.

    Substance may be used to describe a kind of substance, or a specific
    package/container of the substance: an instance.
    """
    resource_type: ClassVar[str] = "SubstanceInstance"
    expiry: Optional[fhirdate.FHIRDate] = None
    identifier: Optional[identifier.Identifier] = None
    quantity: Optional[quantity.Quantity] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceInstance, self).elementProperties()
        js.extend([
            ("expiry", "expiry", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
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
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']