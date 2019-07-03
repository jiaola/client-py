#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Substance) on 2019-07-03.
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
#        self.category = None
#        """ What class/type of substance this is.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.code = None
#        """ What substance this is.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.description = None
#        """ Textual description of the substance, comments.
#        Type `str`
#
#. """
#
#
#        self.identifier = None
#        """ Unique identifier.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.ingredient = None
#        """ Composition information about the substance.
#        List of `SubstanceIngredient` items
#
# (represented as `dict` in JSON). """
#
#
#        self.instance = None
#        """ If this describes a specific package/container of the substance.
#        List of `SubstanceInstance` items
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ active | inactive | entered-in-error.
#        Type `str`
#
#. """
#

#        super(Substance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Substance, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("ingredient", "ingredient", SubstanceIngredient, {  # #}True, None, {  # #}False),
            ("instance", "instance", SubstanceInstance, {  # #}True, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


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
#        self.quantity = None
#        """ Optional amount (concentration).
#        Type `Ratio`
#
# (represented as `dict` in JSON). """
#
#
#        self.substanceCodeableConcept = None
#        """ A component of the substance.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.substanceReference = None
#        """ A component of the substance.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(SubstanceIngredient, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SubstanceIngredient, self).elementProperties()
        js.extend([
            ("quantity", "quantity", ratio.Ratio, {  # #}False, None, {  # #}False),
            ("substanceCodeableConcept", "substanceCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "substance", {  # #}True),
            ("substanceReference", "substanceReference", fhirreference.FHIRReference, {  # #}False, "substance", {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


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
#        self.expiry = None
#        """ When no longer valid to use.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.identifier = None
#        """ Identifier of the package/container.
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#
#
#        self.quantity = None
#        """ Amount of substance in the package.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#

#        super(SubstanceInstance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SubstanceInstance, self).elementProperties()
        js.extend([
            ("expiry", "expiry", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}False, None, {  # #}False),
            ("quantity", "quantity", quantity.Quantity, {  # #}False, None, {  # #}False),
        ])
        return js