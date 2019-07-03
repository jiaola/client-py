#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-baa72e6471 (http://hl7.org/fhir/StructureDefinition/SubstanceDefinition) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio


from . import domainresource

@dataclass
class SubstanceDefinition(domainresource.DomainResource):
    """ The detailed description of a substance, typically at a level beyond what
    is used for prescribing.
    """
    resource_type: ClassVar[str] = "SubstanceDefinition"
    identifier: Optional[identifier.Identifier] = None
    type: Optional[codeableconcept.CodeableConcept] = None
    status: Optional[codeableconcept.CodeableConcept] = None
    domain: Optional[codeableconcept.CodeableConcept] = None
    description: Optional[str] = None
    source: Optional[List[fhirreference.FHIRReference]] = empty_list()
    comment: Optional[str] = None
    moiety: Optional[List[SubstanceDefinitionMoiety]] = empty_list()
    property: Optional[List[SubstanceDefinitionProperty]] = empty_list()
    referenceInformation: Optional[fhirreference.FHIRReference] = None
    structure: Optional[SubstanceDefinitionStructure] = None
    code: Optional[List[SubstanceDefinitionstr]] = empty_list()
    name: Optional[List[SubstanceDefinitionName]] = empty_list()
    molecularWeight: Optional[List[SubstanceDefinitionStructureIsotopeMolecularWeight]] = empty_list()
    relationship: Optional[List[SubstanceDefinitionRelationship]] = empty_list()
    nucleicAcid: Optional[fhirreference.FHIRReference] = None
    polymer: Optional[fhirreference.FHIRReference] = None
    protein: Optional[fhirreference.FHIRReference] = None
    sourceMaterial: Optional[fhirreference.FHIRReference] = None

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
#        self.identifier = None
#        """ Identifier by which this substance is known.
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ High level categorization, e.g. polymer or nucleic acid.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ Status of substance within the catalogue e.g. approved.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.domain = None
#        """ If the substance applies to only human or veterinary use.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.description = None
#        """ Textual description of the substance.
#        Type `str`
#
#. """
#
#
#        self.source = None
#        """ Supporting literature.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.comment = None
#        """ Textual comment about this record of a substance.
#        Type `str`
#
#. """
#
#
#        self.moiety = None
#        """ Moiety, for structural modifications.
#        List of `SubstanceDefinitionMoiety` items
#
# (represented as `dict` in JSON). """
#
#
#        self.property = None
#        """ General specifications for this substance, including how it is
        related to other substances.
#        List of `SubstanceDefinitionProperty` items
#
# (represented as `dict` in JSON). """
#
#
#        self.referenceInformation = None
#        """ General information detailing this substance.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.structure = None
#        """ Structural information.
#        Type `SubstanceDefinitionStructure`
#
# (represented as `dict` in JSON). """
#
#
#        self.code = None
#        """ Codes associated with the substance.
#        List of `SubstanceDefinitionstr` items
#
# (represented as `dict` in JSON). """
#
#
#        self.name = None
#        """ Names applicable to this substance.
#        List of `SubstanceDefinitionName` items
#
# (represented as `dict` in JSON). """
#
#
#        self.molecularWeight = None
#        """ The molecular weight or weight range (for proteins, polymers or
        nucleic acids).
#        List of `SubstanceDefinitionStructureIsotopeMolecularWeight` items
#
# (represented as `dict` in JSON). """
#
#
#        self.relationship = None
#        """ A link between this substance and another, with details of the
        relationship.
#        List of `SubstanceDefinitionRelationship` items
#
# (represented as `dict` in JSON). """
#
#
#        self.nucleicAcid = None
#        """ Data items specific to nucleic acids.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.polymer = None
#        """ Data items specific to polymers.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.protein = None
#        """ Data items specific to proteins.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.sourceMaterial = None
#        """ Material or taxonomic/anatomical source for the substance.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
        
#        super(SubstanceDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceDefinition, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("domain", "domain", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("moiety", "moiety", SubstanceDefinitionMoiety, True, None, False),
            ("property", "property", SubstanceDefinitionProperty, True, None, False),
            ("referenceInformation", "referenceInformation", fhirreference.FHIRReference, False, None, False),
            ("structure", "structure", SubstanceDefinitionStructure, False, None, False),
            ("code", "code", SubstanceDefinitionstr, True, None, False),
            ("name", "name", SubstanceDefinitionName, True, None, False),
            ("molecularWeight", "molecularWeight", SubstanceDefinitionStructureIsotopeMolecularWeight, True, None, False),
            ("relationship", "relationship", SubstanceDefinitionRelationship, True, None, False),
            ("nucleicAcid", "nucleicAcid", fhirreference.FHIRReference, False, None, False),
            ("polymer", "polymer", fhirreference.FHIRReference, False, None, False),
            ("protein", "protein", fhirreference.FHIRReference, False, None, False),
            ("sourceMaterial", "sourceMaterial", fhirreference.FHIRReference, False, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import backboneelement
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio


from . import backboneelement

@dataclass
class SubstanceDefinitionMoiety(backboneelement.BackboneElement):
    """ Moiety, for structural modifications.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionMoiety"
    role: Optional[codeableconcept.CodeableConcept] = None
    identifier: Optional[identifier.Identifier] = None
    name: Optional[str] = None
    stereochemistry: Optional[codeableconcept.CodeableConcept] = None
    opticalActivity: Optional[codeableconcept.CodeableConcept] = None
    molecularFormula: Optional[str] = None
    amountQuantity: Optional[quantity.Quantity] = None
    amountString: Optional[str] = None

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
#        self.role = None
#        """ Role that the moiety is playing.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Identifier by which this moiety substance is known.
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#
#
#        self.name = None
#        """ Textual name for this moiety substance.
#        Type `str`
#
#. """
#
#
#        self.stereochemistry = None
#        """ Stereochemistry type.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.opticalActivity = None
#        """ Optical activity type.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.molecularFormula = None
#        """ Molecular formula.
#        Type `str`
#
#. """
#
#
#        self.amountQuantity = None
#        """ Quantitative value for this moiety.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.amountString = None
#        """ Quantitative value for this moiety.
#        Type `str`
#
#. """
#
        
#        super(SubstanceDefinitionMoiety, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceDefinitionMoiety, self).elementProperties()
        js.extend([
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("name", "name", str, False, None, False),
            ("stereochemistry", "stereochemistry", codeableconcept.CodeableConcept, False, None, False),
            ("opticalActivity", "opticalActivity", codeableconcept.CodeableConcept, False, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio


@dataclass
class SubstanceDefinitionProperty(backboneelement.BackboneElement):
    """ General specifications for this substance, including how it is related to
    other substances.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionProperty"
    category: Optional[codeableconcept.CodeableConcept] = None
    code: Optional[codeableconcept.CodeableConcept] = None
    parameters: Optional[str] = None
    definingSubstanceReference: Optional[fhirreference.FHIRReference] = None
    definingSubstanceCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    amountQuantity: Optional[quantity.Quantity] = None
    amountString: Optional[str] = None

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
#        """ A category for this property, e.g. Physical, Chemical, Enzymatic.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.code = None
#        """ Property type e.g. viscosity, pH, isoelectric point.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.parameters = None
#        """ Parameters that were used in the measurement of a property (e.g.
        for viscosity: measured at 20C with a pH of 7.1).
#        Type `str`
#
#. """
#
#
#        self.definingSubstanceReference = None
#        """ A substance upon which a defining property depends (e.g. for
        solubility: in water, in alcohol).
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.definingSubstanceCodeableConcept = None
#        """ A substance upon which a defining property depends (e.g. for
        solubility: in water, in alcohol).
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.amountQuantity = None
#        """ Quantitative value for this property.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.amountString = None
#        """ Quantitative value for this property.
#        Type `str`
#
#. """
#
        
#        super(SubstanceDefinitionProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceDefinitionProperty, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("parameters", "parameters", str, False, None, False),
            ("definingSubstanceReference", "definingSubstanceReference", fhirreference.FHIRReference, False, "definingSubstance", False),
            ("definingSubstanceCodeableConcept", "definingSubstanceCodeableConcept", codeableconcept.CodeableConcept, False, "definingSubstance", False),
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio


@dataclass
class SubstanceDefinitionStructure(backboneelement.BackboneElement):
    """ Structural information.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionStructure"
    stereochemistry: Optional[codeableconcept.CodeableConcept] = None
    opticalActivity: Optional[codeableconcept.CodeableConcept] = None
    molecularFormula: Optional[str] = None
    molecularFormulaByMoiety: Optional[str] = None
    isotope: Optional[List[SubstanceDefinitionStructureIsotope]] = empty_list()
    molecularWeight: Optional[SubstanceDefinitionStructureIsotopeMolecularWeight] = None
    source: Optional[List[fhirreference.FHIRReference]] = empty_list()
    representation: Optional[List[SubstanceDefinitionStructureRepresentation]] = empty_list()

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
#        self.stereochemistry = None
#        """ Stereochemistry type.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.opticalActivity = None
#        """ Optical activity type.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.molecularFormula = None
#        """ Molecular formula.
#        Type `str`
#
#. """
#
#
#        self.molecularFormulaByMoiety = None
#        """ Specified per moiety according to the Hill system, i.e. first C,
        then H, then alphabetical, each moiety separated by a dot.
#        Type `str`
#
#. """
#
#
#        self.isotope = None
#        """ Applicable for single substances that contain a radionuclide or a
        non-natural isotopic ratio.
#        List of `SubstanceDefinitionStructureIsotope` items
#
# (represented as `dict` in JSON). """
#
#
#        self.molecularWeight = None
#        """ The molecular weight or weight range (for proteins, polymers or
        nucleic acids).
#        Type `SubstanceDefinitionStructureIsotopeMolecularWeight`
#
# (represented as `dict` in JSON). """
#
#
#        self.source = None
#        """ Supporting literature.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.representation = None
#        """ Molecular structural representation.
#        List of `SubstanceDefinitionStructureRepresentation` items
#
# (represented as `dict` in JSON). """
#
        
#        super(SubstanceDefinitionStructure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceDefinitionStructure, self).elementProperties()
        js.extend([
            ("stereochemistry", "stereochemistry", codeableconcept.CodeableConcept, False, None, False),
            ("opticalActivity", "opticalActivity", codeableconcept.CodeableConcept, False, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("molecularFormulaByMoiety", "molecularFormulaByMoiety", str, False, None, False),
            ("isotope", "isotope", SubstanceDefinitionStructureIsotope, True, None, False),
            ("molecularWeight", "molecularWeight", SubstanceDefinitionStructureIsotopeMolecularWeight, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("representation", "representation", SubstanceDefinitionStructureRepresentation, True, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio


@dataclass
class SubstanceDefinitionStructureIsotope(backboneelement.BackboneElement):
    """ Applicable for single substances that contain a radionuclide or a non-
    natural isotopic ratio.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionStructureIsotope"
    identifier: Optional[identifier.Identifier] = None
    name: Optional[codeableconcept.CodeableConcept] = None
    substitution: Optional[codeableconcept.CodeableConcept] = None
    halfLife: Optional[quantity.Quantity] = None
    molecularWeight: Optional[SubstanceDefinitionStructureIsotopeMolecularWeight] = None

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
#        self.identifier = None
#        """ Substance identifier for each non-natural or radioisotope.
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#
#
#        self.name = None
#        """ Substance name for each non-natural or radioisotope.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.substitution = None
#        """ The type of isotopic substitution present in a single substance.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.halfLife = None
#        """ Half life - for a non-natural nuclide.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.molecularWeight = None
#        """ The molecular weight or weight range (for proteins, polymers or
        nucleic acids).
#        Type `SubstanceDefinitionStructureIsotopeMolecularWeight`
#
# (represented as `dict` in JSON). """
#
        
#        super(SubstanceDefinitionStructureIsotope, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceDefinitionStructureIsotope, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("name", "name", codeableconcept.CodeableConcept, False, None, False),
            ("substitution", "substitution", codeableconcept.CodeableConcept, False, None, False),
            ("halfLife", "halfLife", quantity.Quantity, False, None, False),
            ("molecularWeight", "molecularWeight", SubstanceDefinitionStructureIsotopeMolecularWeight, False, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio


@dataclass
class SubstanceDefinitionStructureIsotopeMolecularWeight(backboneelement.BackboneElement):
    """ The molecular weight or weight range (for proteins, polymers or nucleic
    acids).
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionStructureIsotopeMolecularWeight"
    method: Optional[codeableconcept.CodeableConcept] = None
    type: Optional[codeableconcept.CodeableConcept] = None
    amount: Optional[quantity.Quantity] = None

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
#        self.method = None
#        """ The method by which the molecular weight was determined.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ Type of molecular weight such as exact, average (also known as.
        number average), weight average.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.amount = None
#        """ Used to capture quantitative values for a variety of elements. If
        only limits are given, the arithmetic mean would be the average. If
        only a single definite value for a given element is given, it would
        be captured in this field.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
        
#        super(SubstanceDefinitionStructureIsotopeMolecularWeight, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceDefinitionStructureIsotopeMolecularWeight, self).elementProperties()
        js.extend([
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("amount", "amount", quantity.Quantity, False, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio


@dataclass
class SubstanceDefinitionStructureRepresentation(backboneelement.BackboneElement):
    """ Molecular structural representation.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionStructureRepresentation"
    type: Optional[codeableconcept.CodeableConcept] = None
    representation: Optional[str] = None
    attachment: Optional[attachment.Attachment] = None

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
#        self.type = None
#        """ The type of structure (e.g. Full, Partial, Representative).
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.representation = None
#        """ The structural representation as text string in a format e.g.
        InChI, SMILES, MOLFILE, CDX.
#        Type `str`
#
#. """
#
#
#        self.attachment = None
#        """ An attached file with the structural representation.
#        Type `Attachment`
#
# (represented as `dict` in JSON). """
#
        
#        super(SubstanceDefinitionStructureRepresentation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceDefinitionStructureRepresentation, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("representation", "representation", str, False, None, False),
            ("attachment", "attachment", attachment.Attachment, False, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio


@dataclass
class SubstanceDefinitionstr(backboneelement.BackboneElement):
    """ Codes associated with the substance.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionstr"
    code: Optional[codeableconcept.CodeableConcept] = None
    status: Optional[codeableconcept.CodeableConcept] = None
    statusDate: Optional[fhirdate.FHIRDate] = None
    comment: Optional[str] = None
    source: Optional[List[fhirreference.FHIRReference]] = empty_list()

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
#        self.code = None
#        """ The specific code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ Status of the code assignment.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.statusDate = None
#        """ The date at which the code status is changed as part of the
        terminology maintenance.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.comment = None
#        """ Any comment can be provided in this field, if necessary.
#        Type `str`
#
#. """
#
#
#        self.source = None
#        """ Supporting literature.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
        
#        super(SubstanceDefinitionstr, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceDefinitionstr, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio


@dataclass
class SubstanceDefinitionName(backboneelement.BackboneElement):
    """ Names applicable to this substance.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionName"
    name: str = None
    type: Optional[codeableconcept.CodeableConcept] = None
    status: Optional[codeableconcept.CodeableConcept] = None
    preferred: Optional[bool] = None
    language: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    domain: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    synonym: Optional[List[SubstanceDefinitionName]] = empty_list()
    translation: Optional[List[SubstanceDefinitionName]] = empty_list()
    official: Optional[List[SubstanceDefinitionNameOfficial]] = empty_list()
    source: Optional[List[fhirreference.FHIRReference]] = empty_list()

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
#        self.name = None
#        """ The actual name.
#        Type `str`
#
#. """
#
#
#        self.type = None
#        """ Name type.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ The status of the name.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.preferred = None
#        """ If this is the preferred name for this substance.
#        Type `bool`
#
#. """
#
#
#        self.language = None
#        """ Language of the name.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.domain = None
#        """ The use context of this name for example if there is a different
        name a drug active ingredient as opposed to a food colour additive.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.jurisdiction = None
#        """ The jurisdiction where this name applies.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.synonym = None
#        """ A synonym of this name.
#        List of `SubstanceDefinitionName` items
#
# (represented as `dict` in JSON). """
#
#
#        self.translation = None
#        """ A translation for this name.
#        List of `SubstanceDefinitionName` items
#
# (represented as `dict` in JSON). """
#
#
#        self.official = None
#        """ Details of the official nature of this name.
#        List of `SubstanceDefinitionNameOfficial` items
#
# (represented as `dict` in JSON). """
#
#
#        self.source = None
#        """ Supporting literature.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
        
#        super(SubstanceDefinitionName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceDefinitionName, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("preferred", "preferred", bool, False, None, False),
            ("language", "language", codeableconcept.CodeableConcept, True, None, False),
            ("domain", "domain", codeableconcept.CodeableConcept, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("synonym", "synonym", SubstanceDefinitionName, True, None, False),
            ("translation", "translation", SubstanceDefinitionName, True, None, False),
            ("official", "official", SubstanceDefinitionNameOfficial, True, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio


@dataclass
class SubstanceDefinitionNameOfficial(backboneelement.BackboneElement):
    """ Details of the official nature of this name.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionNameOfficial"
    authority: Optional[codeableconcept.CodeableConcept] = None
    status: Optional[codeableconcept.CodeableConcept] = None
    date: Optional[fhirdate.FHIRDate] = None

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
#        self.authority = None
#        """ Which authority uses this official name.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ The status of the official name.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.date = None
#        """ Date of official name change.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
        
#        super(SubstanceDefinitionNameOfficial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceDefinitionNameOfficial, self).elementProperties()
        js.extend([
            ("authority", "authority", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio


@dataclass
class SubstanceDefinitionRelationship(backboneelement.BackboneElement):
    """ A link between this substance and another, with details of the relationship.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionRelationship"
    substanceReference: Optional[fhirreference.FHIRReference] = None
    substanceCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    relationship: Optional[codeableconcept.CodeableConcept] = None
    isDefining: Optional[bool] = None
    amountQuantity: Optional[quantity.Quantity] = None
    amountRange: Optional[range.Range] = None
    amountRatio: Optional[ratio.Ratio] = None
    amountString: Optional[str] = None
    amountRatioLowLimit: Optional[ratio.Ratio] = None
    amountType: Optional[codeableconcept.CodeableConcept] = None
    source: Optional[List[fhirreference.FHIRReference]] = empty_list()

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
#        self.substanceReference = None
#        """ A pointer to another substance, as a resource or just a
        representational code.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.substanceCodeableConcept = None
#        """ A pointer to another substance, as a resource or just a
        representational code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.relationship = None
#        """ For example "salt to parent", "active moiety", "starting material".
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.isDefining = None
#        """ For example where an enzyme strongly bonds with a particular
        substance, this is a defining relationship for that enzyme, out of
        several possible substance relationships.
#        Type `bool`
#
#. """
#
#
#        self.amountQuantity = None
#        """ A numeric factor for the relationship, for instance to express that
        the salt of a substance has some percentage of the active substance
        in relation to some other.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.amountRange = None
#        """ A numeric factor for the relationship, for instance to express that
        the salt of a substance has some percentage of the active substance
        in relation to some other.
#        Type `Range`
#
# (represented as `dict` in JSON). """
#
#
#        self.amountRatio = None
#        """ A numeric factor for the relationship, for instance to express that
        the salt of a substance has some percentage of the active substance
        in relation to some other.
#        Type `Ratio`
#
# (represented as `dict` in JSON). """
#
#
#        self.amountString = None
#        """ A numeric factor for the relationship, for instance to express that
        the salt of a substance has some percentage of the active substance
        in relation to some other.
#        Type `str`
#
#. """
#
#
#        self.amountRatioLowLimit = None
#        """ For use when the numeric.
#        Type `Ratio`
#
# (represented as `dict` in JSON). """
#
#
#        self.amountType = None
#        """ An operator for the amount, for example "average", "approximately",
        "less than".
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.source = None
#        """ Supporting literature.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
        
#        super(SubstanceDefinitionRelationship, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceDefinitionRelationship, self).elementProperties()
        js.extend([
            ("substanceReference", "substanceReference", fhirreference.FHIRReference, False, "substance", False),
            ("substanceCodeableConcept", "substanceCodeableConcept", codeableconcept.CodeableConcept, False, "substance", False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
            ("isDefining", "isDefining", bool, False, None, False),
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("amountRange", "amountRange", range.Range, False, "amount", False),
            ("amountRatio", "amountRatio", ratio.Ratio, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("amountRatioLowLimit", "amountRatioLowLimit", ratio.Ratio, False, None, False),
            ("amountType", "amountType", codeableconcept.CodeableConcept, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
        ])
        return js
