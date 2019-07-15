#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/VisionPrescription) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity

from . import domainresource

@dataclass
class VisionPrescription(domainresource.DomainResource):
    """ Prescription for vision correction products for a patient.

    An authorization for the provision of glasses and/or contact lenses to a
    patient.
    """
    resource_type: ClassVar[str] = "VisionPrescription"
    created:fhirdate.FHIRDate = None
    dateWritten:fhirdate.FHIRDate = None
    encounter: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    lensSpecification: List[ VisionPrescriptionLensSpecification] = empty_list()
    patient:fhirreference.FHIRReference = None
    prescriber:fhirreference.FHIRReference = None
    status: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(VisionPrescription, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("dateWritten", "dateWritten", fhirdate.FHIRDate, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lensSpecification", "lensSpecification", VisionPrescriptionLensSpecification, True, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("prescriber", "prescriber", fhirreference.FHIRReference, False, None, True),
            ("status", "status", str, False, None, True),
        ])
        return js

from . import backboneelement

@dataclass
class VisionPrescriptionLensSpecification(backboneelement.BackboneElement):
    """ Vision lens authorization.

    Contain the details of  the individual lens specifications and serves as
    the authorization for the fullfillment by certified professionals.
    """
    resource_type: ClassVar[str] = "VisionPrescriptionLensSpecification"
    add: Optional[float] = None
    axis: Optional[int] = None
    backCurve: Optional[float] = None
    brand: Optional[str] = None
    color: Optional[str] = None
    cylinder: Optional[float] = None
    diameter: Optional[float] = None
    duration: Optional[quantity.Quantity] = None
    eye: str = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    power: Optional[float] = None
    prism: Optional[List[VisionPrescriptionLensSpecificationPrism]] = empty_list()
    product:codeableconcept.CodeableConcept = None
    sphere: Optional[float] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(VisionPrescriptionLensSpecification, self).elementProperties()
        js.extend([
            ("add", "add", float, False, None, False),
            ("axis", "axis", int, False, None, False),
            ("backCurve", "backCurve", float, False, None, False),
            ("brand", "brand", str, False, None, False),
            ("color", "color", str, False, None, False),
            ("cylinder", "cylinder", float, False, None, False),
            ("diameter", "diameter", float, False, None, False),
            ("duration", "duration", quantity.Quantity, False, None, False),
            ("eye", "eye", str, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("power", "power", float, False, None, False),
            ("prism", "prism", VisionPrescriptionLensSpecificationPrism, True, None, False),
            ("product", "product", codeableconcept.CodeableConcept, False, None, True),
            ("sphere", "sphere", float, False, None, False),
        ])
        return js

@dataclass
class VisionPrescriptionLensSpecificationPrism(backboneelement.BackboneElement):
    """ Eye alignment compensation.

    Allows for adjustment on two axis.
    """
    resource_type: ClassVar[str] = "VisionPrescriptionLensSpecificationPrism"
    amount: float = None
    base: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(VisionPrescriptionLensSpecificationPrism, self).elementProperties()
        js.extend([
            ("amount", "amount", float, False, None, True),
            ("base", "base", str, False, None, True),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
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