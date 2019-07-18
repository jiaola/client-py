#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductPharmaceutical) on 2019-07-18.
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
from . import ratio

from . import backboneelement

@dataclass
class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod(backboneelement.BackboneElement):
    """ A species specific time during which consumption of animal product is not
    appropriate.
    """
    resource_type: ClassVar[str] = "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod"
    supportingInformation: Optional[str] = None
    tissue:codeableconcept.CodeableConcept = None
    value:quantity.Quantity = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod, self).elementProperties()
        js.extend([
            ("supportingInformation", "supportingInformation", str, False, None, False),
            ("tissue", "tissue", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", quantity.Quantity, False, None, True),
        ])
        return js

@dataclass
class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies(backboneelement.BackboneElement):
    """ A species for which this route applies.
    """
    resource_type: ClassVar[str] = "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies"
    code:codeableconcept.CodeableConcept = None
    withdrawalPeriod: Optional[List[MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("withdrawalPeriod", "withdrawalPeriod", MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod, True, None, False),
        ])
        return js

@dataclass
class MedicinalProductPharmaceuticalRouteOfAdministration(backboneelement.BackboneElement):
    """ The path by which the pharmaceutical product is taken into or makes contact
    with the body.
    """
    resource_type: ClassVar[str] = "MedicinalProductPharmaceuticalRouteOfAdministration"
    code:codeableconcept.CodeableConcept = None
    firstDose: Optional[quantity.Quantity] = None
    maxDosePerDay: Optional[quantity.Quantity] = None
    maxDosePerTreatmentPeriod: Optional[ratio.Ratio] = None
    maxSingleDose: Optional[quantity.Quantity] = None
    maxTreatmentPeriod: Optional[duration.Duration] = None
    targetSpecies: Optional[List[MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalRouteOfAdministration, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("firstDose", "firstDose", quantity.Quantity, False, None, False),
            ("maxDosePerDay", "maxDosePerDay", quantity.Quantity, False, None, False),
            ("maxDosePerTreatmentPeriod", "maxDosePerTreatmentPeriod", ratio.Ratio, False, None, False),
            ("maxSingleDose", "maxSingleDose", quantity.Quantity, False, None, False),
            ("maxTreatmentPeriod", "maxTreatmentPeriod", duration.Duration, False, None, False),
            ("targetSpecies", "targetSpecies", MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies, True, None, False),
        ])
        return js

@dataclass
class MedicinalProductPharmaceuticalCharacteristics(backboneelement.BackboneElement):
    """ Characteristics e.g. a products onset of action.
    """
    resource_type: ClassVar[str] = "MedicinalProductPharmaceuticalCharacteristics"
    code:codeableconcept.CodeableConcept = None
    status: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalCharacteristics, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

from . import domainresource

@dataclass
class MedicinalProductPharmaceutical(domainresource.DomainResource):
    """ A pharmaceutical product described in terms of its composition and dose
    form.
    """
    resource_type: ClassVar[str] = "MedicinalProductPharmaceutical"
    administrableDoseForm:codeableconcept.CodeableConcept = None
    characteristics: Optional[List[MedicinalProductPharmaceuticalCharacteristics]] = empty_list()
    device: Optional[List[fhirreference.FHIRReference]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    ingredient: Optional[List[fhirreference.FHIRReference]] = empty_list()
    routeOfAdministration: List[ MedicinalProductPharmaceuticalRouteOfAdministration] = empty_list()
    unitOfPresentation: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductPharmaceutical, self).elementProperties()
        js.extend([
            ("administrableDoseForm", "administrableDoseForm", codeableconcept.CodeableConcept, False, None, True),
            ("characteristics", "characteristics", MedicinalProductPharmaceuticalCharacteristics, True, None, False),
            ("device", "device", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("ingredient", "ingredient", fhirreference.FHIRReference, True, None, False),
            ("routeOfAdministration", "routeOfAdministration", MedicinalProductPharmaceuticalRouteOfAdministration, True, None, True),
            ("unitOfPresentation", "unitOfPresentation", codeableconcept.CodeableConcept, False, None, False),
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
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']