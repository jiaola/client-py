#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductInteraction) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirreference


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.description = None
#        """ The interaction described.
#        Type `str`
#
#. """
#
#
#        self.effect = None
#        """ The effect of the interaction, for example "reduced gastric
        absorption of primary medication".
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.incidence = None
#        """ The incidence of the interaction, e.g. theoretical, observed.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.interactant = None
#        """ The specific medication, food or laboratory test that interacts.
#        List of `MedicinalProductInteractionInteractant` items
#
# (represented as `dict` in JSON). """
#
#
#        self.management = None
#        """ Actions for managing the interaction.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.subject = None
#        """ The medication for which this is a described interaction.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ The type of the interaction e.g. drug-drug interaction, drug-food
        interaction, drug-lab test interaction.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(MedicinalProductInteraction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicinalProductInteraction, self).elementProperties()
        js.extend([
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("effect", "effect", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("incidence", "incidence", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("interactant", "interactant", MedicinalProductInteractionInteractant, {  # #}True, None, {  # #}False),
            ("management", "management", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("subject", "subject", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.itemCodeableConcept = None
#        """ The specific medication, food or laboratory test that interacts.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.itemReference = None
#        """ The specific medication, food or laboratory test that interacts.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(MedicinalProductInteractionInteractant, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicinalProductInteractionInteractant, self).elementProperties()
        js.extend([
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "item", {  # #}True),
            ("itemReference", "itemReference", fhirreference.FHIRReference, {  # #}False, "item", {  # #}True),
        ])
        return js