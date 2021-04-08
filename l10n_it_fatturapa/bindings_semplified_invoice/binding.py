# ./binding.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:636491146f120c417757144dba267e778e775c34
# Generated 2021-04-06 10:45:17.185726 by PyXB version 1.2.6 using Python 2.7.17.final.0
# Namespace http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:23b6277e-96c5-11eb-872d-080027bd11c0')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
from odoo.addons.l10n_it_fatturapa.bindings import _ds as _ImportedBinding__ds
# from . import _ds as _ImportedBinding__ds
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ds = _ImportedBinding__ds.Namespace
_Namespace_ds.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}CodiceDestinatarioType
class CodiceDestinatarioType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodiceDestinatarioType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 54, 2)
    _Documentation = None
CodiceDestinatarioType._CF_pattern = pyxb.binding.facets.CF_pattern()
CodiceDestinatarioType._CF_pattern.addPattern(pattern='[A-Z0-9]{7}')
CodiceDestinatarioType._InitializeFacetMap(CodiceDestinatarioType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CodiceDestinatarioType', CodiceDestinatarioType)
_module_typeBindings.CodiceDestinatarioType = CodiceDestinatarioType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}CodiceType
class CodiceType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodiceType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 65, 2)
    _Documentation = None
CodiceType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
CodiceType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(28))
CodiceType._InitializeFacetMap(CodiceType._CF_minLength,
   CodiceType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'CodiceType', CodiceType)
_module_typeBindings.CodiceType = CodiceType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}FormatoTrasmissioneType
class FormatoTrasmissioneType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FormatoTrasmissioneType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 71, 2)
    _Documentation = None
FormatoTrasmissioneType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FormatoTrasmissioneType, enum_prefix=None)
FormatoTrasmissioneType.FSM10 = FormatoTrasmissioneType._CF_enumeration.addEnumeration(unicode_value='FSM10', tag='FSM10')
FormatoTrasmissioneType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(5))
FormatoTrasmissioneType._InitializeFacetMap(FormatoTrasmissioneType._CF_enumeration,
   FormatoTrasmissioneType._CF_length)
Namespace.addCategoryObject('typeBinding', 'FormatoTrasmissioneType', FormatoTrasmissioneType)
_module_typeBindings.FormatoTrasmissioneType = FormatoTrasmissioneType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}Art73Type
class Art73Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Art73Type')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 106, 2)
    _Documentation = None
Art73Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Art73Type, enum_prefix=None)
Art73Type.SI = Art73Type._CF_enumeration.addEnumeration(unicode_value='SI', tag='SI')
Art73Type._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2))
Art73Type._InitializeFacetMap(Art73Type._CF_enumeration,
   Art73Type._CF_length)
Namespace.addCategoryObject('typeBinding', 'Art73Type', Art73Type)
_module_typeBindings.Art73Type = Art73Type

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}TipoDocumentoType
class TipoDocumentoType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TipoDocumentoType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 116, 2)
    _Documentation = None
TipoDocumentoType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoDocumentoType, enum_prefix=None)
TipoDocumentoType.TD07 = TipoDocumentoType._CF_enumeration.addEnumeration(unicode_value='TD07', tag='TD07')
TipoDocumentoType.TD08 = TipoDocumentoType._CF_enumeration.addEnumeration(unicode_value='TD08', tag='TD08')
TipoDocumentoType.TD09 = TipoDocumentoType._CF_enumeration.addEnumeration(unicode_value='TD09', tag='TD09')
TipoDocumentoType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(4))
TipoDocumentoType._InitializeFacetMap(TipoDocumentoType._CF_enumeration,
   TipoDocumentoType._CF_length)
Namespace.addCategoryObject('typeBinding', 'TipoDocumentoType', TipoDocumentoType)
_module_typeBindings.TipoDocumentoType = TipoDocumentoType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}SoggettoEmittenteType
class SoggettoEmittenteType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoggettoEmittenteType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 146, 2)
    _Documentation = None
SoggettoEmittenteType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SoggettoEmittenteType, enum_prefix=None)
SoggettoEmittenteType.CC = SoggettoEmittenteType._CF_enumeration.addEnumeration(unicode_value='CC', tag='CC')
SoggettoEmittenteType.TZ = SoggettoEmittenteType._CF_enumeration.addEnumeration(unicode_value='TZ', tag='TZ')
SoggettoEmittenteType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2))
SoggettoEmittenteType._InitializeFacetMap(SoggettoEmittenteType._CF_enumeration,
   SoggettoEmittenteType._CF_length)
Namespace.addCategoryObject('typeBinding', 'SoggettoEmittenteType', SoggettoEmittenteType)
_module_typeBindings.SoggettoEmittenteType = SoggettoEmittenteType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}RegimeFiscaleType
class RegimeFiscaleType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RegimeFiscaleType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 184, 2)
    _Documentation = None
RegimeFiscaleType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RegimeFiscaleType, enum_prefix=None)
RegimeFiscaleType.RF01 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF01', tag='RF01')
RegimeFiscaleType.RF02 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF02', tag='RF02')
RegimeFiscaleType.RF04 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF04', tag='RF04')
RegimeFiscaleType.RF05 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF05', tag='RF05')
RegimeFiscaleType.RF06 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF06', tag='RF06')
RegimeFiscaleType.RF07 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF07', tag='RF07')
RegimeFiscaleType.RF08 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF08', tag='RF08')
RegimeFiscaleType.RF09 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF09', tag='RF09')
RegimeFiscaleType.RF10 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF10', tag='RF10')
RegimeFiscaleType.RF11 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF11', tag='RF11')
RegimeFiscaleType.RF12 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF12', tag='RF12')
RegimeFiscaleType.RF13 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF13', tag='RF13')
RegimeFiscaleType.RF14 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF14', tag='RF14')
RegimeFiscaleType.RF15 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF15', tag='RF15')
RegimeFiscaleType.RF16 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF16', tag='RF16')
RegimeFiscaleType.RF17 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF17', tag='RF17')
RegimeFiscaleType.RF19 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF19', tag='RF19')
RegimeFiscaleType.RF18 = RegimeFiscaleType._CF_enumeration.addEnumeration(unicode_value='RF18', tag='RF18')
RegimeFiscaleType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(4))
RegimeFiscaleType._InitializeFacetMap(RegimeFiscaleType._CF_enumeration,
   RegimeFiscaleType._CF_length)
Namespace.addCategoryObject('typeBinding', 'RegimeFiscaleType', RegimeFiscaleType)
_module_typeBindings.RegimeFiscaleType = RegimeFiscaleType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}NaturaType
class NaturaType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NaturaType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 366, 2)
    _Documentation = None
NaturaType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NaturaType, enum_prefix=None)
NaturaType.N1 = NaturaType._CF_enumeration.addEnumeration(unicode_value='N1', tag='N1')
NaturaType.N2 = NaturaType._CF_enumeration.addEnumeration(unicode_value='N2', tag='N2')
NaturaType.N2_1 = NaturaType._CF_enumeration.addEnumeration(unicode_value='N2.1', tag='N2_1')
NaturaType.N2_2 = NaturaType._CF_enumeration.addEnumeration(unicode_value='N2.2', tag='N2_2')
NaturaType.N3 = NaturaType._CF_enumeration.addEnumeration(unicode_value='N3', tag='N3')
NaturaType.N3_1 = NaturaType._CF_enumeration.addEnumeration(unicode_value='N3.1', tag='N3_1')
NaturaType.N3_2 = NaturaType._CF_enumeration.addEnumeration(unicode_value='N3.2', tag='N3_2')
NaturaType.N3_3 = NaturaType._CF_enumeration.addEnumeration(unicode_value='N3.3', tag='N3_3')
NaturaType.N3_4 = NaturaType._CF_enumeration.addEnumeration(unicode_value='N3.4', tag='N3_4')
NaturaType.N3_5 = NaturaType._CF_enumeration.addEnumeration(unicode_value='N3.5', tag='N3_5')
NaturaType.N3_6 = NaturaType._CF_enumeration.addEnumeration(unicode_value='N3.6', tag='N3_6')
NaturaType.N4 = NaturaType._CF_enumeration.addEnumeration(unicode_value='N4', tag='N4')
NaturaType.N5 = NaturaType._CF_enumeration.addEnumeration(unicode_value='N5', tag='N5')
NaturaType._InitializeFacetMap(NaturaType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NaturaType', NaturaType)
_module_typeBindings.NaturaType = NaturaType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}CodiceFiscaleType
class CodiceFiscaleType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodiceFiscaleType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 437, 2)
    _Documentation = None
CodiceFiscaleType._CF_pattern = pyxb.binding.facets.CF_pattern()
CodiceFiscaleType._CF_pattern.addPattern(pattern='[A-Z0-9]{11,16}')
CodiceFiscaleType._InitializeFacetMap(CodiceFiscaleType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CodiceFiscaleType', CodiceFiscaleType)
_module_typeBindings.CodiceFiscaleType = CodiceFiscaleType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}SocioUnicoType
class SocioUnicoType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SocioUnicoType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 442, 2)
    _Documentation = None
SocioUnicoType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SocioUnicoType, enum_prefix=None)
SocioUnicoType.SU = SocioUnicoType._CF_enumeration.addEnumeration(unicode_value='SU', tag='SU')
SocioUnicoType.SM = SocioUnicoType._CF_enumeration.addEnumeration(unicode_value='SM', tag='SM')
SocioUnicoType._InitializeFacetMap(SocioUnicoType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SocioUnicoType', SocioUnicoType)
_module_typeBindings.SocioUnicoType = SocioUnicoType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}StatoLiquidazioneType
class StatoLiquidazioneType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StatoLiquidazioneType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 456, 2)
    _Documentation = None
StatoLiquidazioneType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StatoLiquidazioneType, enum_prefix=None)
StatoLiquidazioneType.LS = StatoLiquidazioneType._CF_enumeration.addEnumeration(unicode_value='LS', tag='LS')
StatoLiquidazioneType.LN = StatoLiquidazioneType._CF_enumeration.addEnumeration(unicode_value='LN', tag='LN')
StatoLiquidazioneType._InitializeFacetMap(StatoLiquidazioneType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'StatoLiquidazioneType', StatoLiquidazioneType)
_module_typeBindings.StatoLiquidazioneType = StatoLiquidazioneType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}String10Type
class String10Type (pyxb.binding.datatypes.normalizedString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'String10Type')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 470, 2)
    _Documentation = None
String10Type._CF_pattern = pyxb.binding.facets.CF_pattern()
String10Type._CF_pattern.addPattern(pattern='(\\p{IsBasicLatin}{1,10})')
String10Type._InitializeFacetMap(String10Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'String10Type', String10Type)
_module_typeBindings.String10Type = String10Type

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}String20Type
class String20Type (pyxb.binding.datatypes.normalizedString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'String20Type')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 475, 2)
    _Documentation = None
String20Type._CF_pattern = pyxb.binding.facets.CF_pattern()
String20Type._CF_pattern.addPattern(pattern='(\\p{IsBasicLatin}{1,20})')
String20Type._InitializeFacetMap(String20Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'String20Type', String20Type)
_module_typeBindings.String20Type = String20Type

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}String60LatinType
class String60LatinType (pyxb.binding.datatypes.normalizedString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'String60LatinType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 480, 2)
    _Documentation = None
String60LatinType._CF_pattern = pyxb.binding.facets.CF_pattern()
String60LatinType._CF_pattern.addPattern(pattern='[\\p{IsBasicLatin}\\p{IsLatin-1Supplement}]{1,60}')
String60LatinType._InitializeFacetMap(String60LatinType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'String60LatinType', String60LatinType)
_module_typeBindings.String60LatinType = String60LatinType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}String80LatinType
class String80LatinType (pyxb.binding.datatypes.normalizedString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'String80LatinType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 485, 2)
    _Documentation = None
String80LatinType._CF_pattern = pyxb.binding.facets.CF_pattern()
String80LatinType._CF_pattern.addPattern(pattern='[\\p{IsBasicLatin}\\p{IsLatin-1Supplement}]{1,80}')
String80LatinType._InitializeFacetMap(String80LatinType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'String80LatinType', String80LatinType)
_module_typeBindings.String80LatinType = String80LatinType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}String100LatinType
class String100LatinType (pyxb.binding.datatypes.normalizedString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'String100LatinType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 490, 2)
    _Documentation = None
String100LatinType._CF_pattern = pyxb.binding.facets.CF_pattern()
String100LatinType._CF_pattern.addPattern(pattern='[\\p{IsBasicLatin}\\p{IsLatin-1Supplement}]{1,100}')
String100LatinType._InitializeFacetMap(String100LatinType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'String100LatinType', String100LatinType)
_module_typeBindings.String100LatinType = String100LatinType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}String1000LatinType
class String1000LatinType (pyxb.binding.datatypes.normalizedString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'String1000LatinType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 495, 2)
    _Documentation = None
String1000LatinType._CF_pattern = pyxb.binding.facets.CF_pattern()
String1000LatinType._CF_pattern.addPattern(pattern='[\\p{IsBasicLatin}\\p{IsLatin-1Supplement}]{1,1000}')
String1000LatinType._InitializeFacetMap(String1000LatinType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'String1000LatinType', String1000LatinType)
_module_typeBindings.String1000LatinType = String1000LatinType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}ProvinciaType
class ProvinciaType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProvinciaType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 500, 2)
    _Documentation = None
ProvinciaType._CF_pattern = pyxb.binding.facets.CF_pattern()
ProvinciaType._CF_pattern.addPattern(pattern='[A-Z]{2}')
ProvinciaType._InitializeFacetMap(ProvinciaType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ProvinciaType', ProvinciaType)
_module_typeBindings.ProvinciaType = ProvinciaType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}NazioneType
class NazioneType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NazioneType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 505, 2)
    _Documentation = None
NazioneType._CF_pattern = pyxb.binding.facets.CF_pattern()
NazioneType._CF_pattern.addPattern(pattern='[A-Z]{2}')
NazioneType._InitializeFacetMap(NazioneType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'NazioneType', NazioneType)
_module_typeBindings.NazioneType = NazioneType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}DivisaType
class DivisaType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DivisaType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 510, 2)
    _Documentation = None
DivisaType._CF_pattern = pyxb.binding.facets.CF_pattern()
DivisaType._CF_pattern.addPattern(pattern='[A-Z]{3}')
DivisaType._InitializeFacetMap(DivisaType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DivisaType', DivisaType)
_module_typeBindings.DivisaType = DivisaType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}NumeroCivicoType
class NumeroCivicoType (pyxb.binding.datatypes.normalizedString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NumeroCivicoType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 515, 2)
    _Documentation = None
NumeroCivicoType._CF_pattern = pyxb.binding.facets.CF_pattern()
NumeroCivicoType._CF_pattern.addPattern(pattern='(\\p{IsBasicLatin}{1,8})')
NumeroCivicoType._InitializeFacetMap(NumeroCivicoType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'NumeroCivicoType', NumeroCivicoType)
_module_typeBindings.NumeroCivicoType = NumeroCivicoType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}EmailType
class EmailType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EmailType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 520, 2)
    _Documentation = None
EmailType._CF_pattern = pyxb.binding.facets.CF_pattern()
EmailType._CF_pattern.addPattern(pattern='([!#-\'*+/-9=?A-Z^-~-]+(\\.[!#-\'*+/-9=?A-Z^-~-]+)*|"(\\[\\]!#-[^-~ \\t]|(\\\\[\\t -~]))+")@([!#-\'*+/-9=?A-Z^-~-]+(\\.[!#-\'*+/-9=?A-Z^-~-]+)*|\\[[\\t -Z^-~]*\\])')
EmailType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
EmailType._InitializeFacetMap(EmailType._CF_pattern,
   EmailType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'EmailType', EmailType)
_module_typeBindings.EmailType = EmailType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}Amount2DecimalType
class Amount2DecimalType (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Amount2DecimalType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 527, 2)
    _Documentation = None
Amount2DecimalType._CF_pattern = pyxb.binding.facets.CF_pattern()
Amount2DecimalType._CF_pattern.addPattern(pattern='[\\-]?[0-9]{1,11}\\.[0-9]{2}')
Amount2DecimalType._InitializeFacetMap(Amount2DecimalType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'Amount2DecimalType', Amount2DecimalType)
_module_typeBindings.Amount2DecimalType = Amount2DecimalType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}RateType
class RateType (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RateType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 532, 2)
    _Documentation = None
RateType._CF_pattern = pyxb.binding.facets.CF_pattern()
RateType._CF_pattern.addPattern(pattern='[0-9]{1,3}\\.[0-9]{2}')
RateType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=RateType, value=pyxb.binding.datatypes.decimal('100.0'))
RateType._InitializeFacetMap(RateType._CF_pattern,
   RateType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'RateType', RateType)
_module_typeBindings.RateType = RateType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}CAPType
class CAPType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CAPType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 538, 2)
    _Documentation = None
CAPType._CF_pattern = pyxb.binding.facets.CF_pattern()
CAPType._CF_pattern.addPattern(pattern='[0-9][0-9][0-9][0-9][0-9]')
CAPType._InitializeFacetMap(CAPType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CAPType', CAPType)
_module_typeBindings.CAPType = CAPType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}DataFatturaType
class DataFatturaType (pyxb.binding.datatypes.date):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataFatturaType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 543, 2)
    _Documentation = None
DataFatturaType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=DataFatturaType, value=pyxb.binding.datatypes.date('1970-01-01'))
DataFatturaType._InitializeFacetMap(DataFatturaType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'DataFatturaType', DataFatturaType)
_module_typeBindings.DataFatturaType = DataFatturaType

# Atomic simple type: {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}BolloVirtualeType
class BolloVirtualeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BolloVirtualeType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 548, 2)
    _Documentation = None
BolloVirtualeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BolloVirtualeType, enum_prefix=None)
BolloVirtualeType.SI = BolloVirtualeType._CF_enumeration.addEnumeration(unicode_value='SI', tag='SI')
BolloVirtualeType._InitializeFacetMap(BolloVirtualeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BolloVirtualeType', BolloVirtualeType)
_module_typeBindings.BolloVirtualeType = BolloVirtualeType

# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}FatturaElettronicaHeaderType with content type ELEMENT_ONLY
class FatturaElettronicaHeaderType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}FatturaElettronicaHeaderType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FatturaElettronicaHeaderType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 27, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element DatiTrasmissione uses Python identifier DatiTrasmissione
    __DatiTrasmissione = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DatiTrasmissione'), 'DatiTrasmissione', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_FatturaElettronicaHeaderType_DatiTrasmissione', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 29, 6), )

    
    DatiTrasmissione = property(__DatiTrasmissione.value, __DatiTrasmissione.set, None, None)

    
    # Element CedentePrestatore uses Python identifier CedentePrestatore
    __CedentePrestatore = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CedentePrestatore'), 'CedentePrestatore', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_FatturaElettronicaHeaderType_CedentePrestatore', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 30, 6), )

    
    CedentePrestatore = property(__CedentePrestatore.value, __CedentePrestatore.set, None, None)

    
    # Element CessionarioCommittente uses Python identifier CessionarioCommittente
    __CessionarioCommittente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CessionarioCommittente'), 'CessionarioCommittente', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_FatturaElettronicaHeaderType_CessionarioCommittente', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 31, 6), )

    
    CessionarioCommittente = property(__CessionarioCommittente.value, __CessionarioCommittente.set, None, None)

    
    # Element SoggettoEmittente uses Python identifier SoggettoEmittente
    __SoggettoEmittente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SoggettoEmittente'), 'SoggettoEmittente', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_FatturaElettronicaHeaderType_SoggettoEmittente', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 32, 6), )

    
    SoggettoEmittente = property(__SoggettoEmittente.value, __SoggettoEmittente.set, None, None)

    _ElementMap.update({
        __DatiTrasmissione.name() : __DatiTrasmissione,
        __CedentePrestatore.name() : __CedentePrestatore,
        __CessionarioCommittente.name() : __CessionarioCommittente,
        __SoggettoEmittente.name() : __SoggettoEmittente
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FatturaElettronicaHeaderType = FatturaElettronicaHeaderType
Namespace.addCategoryObject('typeBinding', 'FatturaElettronicaHeaderType', FatturaElettronicaHeaderType)


# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}FatturaElettronicaBodyType with content type ELEMENT_ONLY
class FatturaElettronicaBodyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}FatturaElettronicaBodyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FatturaElettronicaBodyType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 35, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element DatiGenerali uses Python identifier DatiGenerali
    __DatiGenerali = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DatiGenerali'), 'DatiGenerali', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_FatturaElettronicaBodyType_DatiGenerali', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 37, 6), )

    
    DatiGenerali = property(__DatiGenerali.value, __DatiGenerali.set, None, None)

    
    # Element DatiBeniServizi uses Python identifier DatiBeniServizi
    __DatiBeniServizi = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DatiBeniServizi'), 'DatiBeniServizi', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_FatturaElettronicaBodyType_DatiBeniServizi', True, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 38, 6), )

    
    DatiBeniServizi = property(__DatiBeniServizi.value, __DatiBeniServizi.set, None, None)

    
    # Element Allegati uses Python identifier Allegati
    __Allegati = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Allegati'), 'Allegati', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_FatturaElettronicaBodyType_Allegati', True, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 39, 6), )

    
    Allegati = property(__Allegati.value, __Allegati.set, None, None)

    _ElementMap.update({
        __DatiGenerali.name() : __DatiGenerali,
        __DatiBeniServizi.name() : __DatiBeniServizi,
        __Allegati.name() : __Allegati
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FatturaElettronicaBodyType = FatturaElettronicaBodyType
Namespace.addCategoryObject('typeBinding', 'FatturaElettronicaBodyType', FatturaElettronicaBodyType)


# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}DatiTrasmissioneType with content type ELEMENT_ONLY
class DatiTrasmissioneType (pyxb.binding.basis.complexTypeDefinition):
    """Blocco relativo ai dati di trasmissione della Fattura Elettronica"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatiTrasmissioneType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 42, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element IdTrasmittente uses Python identifier IdTrasmittente
    __IdTrasmittente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'IdTrasmittente'), 'IdTrasmittente', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiTrasmissioneType_IdTrasmittente', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 47, 6), )

    
    IdTrasmittente = property(__IdTrasmittente.value, __IdTrasmittente.set, None, None)

    
    # Element ProgressivoInvio uses Python identifier ProgressivoInvio
    __ProgressivoInvio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ProgressivoInvio'), 'ProgressivoInvio', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiTrasmissioneType_ProgressivoInvio', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 48, 6), )

    
    ProgressivoInvio = property(__ProgressivoInvio.value, __ProgressivoInvio.set, None, None)

    
    # Element FormatoTrasmissione uses Python identifier FormatoTrasmissione
    __FormatoTrasmissione = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FormatoTrasmissione'), 'FormatoTrasmissione', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiTrasmissioneType_FormatoTrasmissione', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 49, 6), )

    
    FormatoTrasmissione = property(__FormatoTrasmissione.value, __FormatoTrasmissione.set, None, None)

    
    # Element CodiceDestinatario uses Python identifier CodiceDestinatario
    __CodiceDestinatario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodiceDestinatario'), 'CodiceDestinatario', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiTrasmissioneType_CodiceDestinatario', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 50, 6), )

    
    CodiceDestinatario = property(__CodiceDestinatario.value, __CodiceDestinatario.set, None, None)

    
    # Element PECDestinatario uses Python identifier PECDestinatario
    __PECDestinatario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PECDestinatario'), 'PECDestinatario', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiTrasmissioneType_PECDestinatario', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 51, 6), )

    
    PECDestinatario = property(__PECDestinatario.value, __PECDestinatario.set, None, None)

    _ElementMap.update({
        __IdTrasmittente.name() : __IdTrasmittente,
        __ProgressivoInvio.name() : __ProgressivoInvio,
        __FormatoTrasmissione.name() : __FormatoTrasmissione,
        __CodiceDestinatario.name() : __CodiceDestinatario,
        __PECDestinatario.name() : __PECDestinatario
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DatiTrasmissioneType = DatiTrasmissioneType
Namespace.addCategoryObject('typeBinding', 'DatiTrasmissioneType', DatiTrasmissioneType)


# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}IdFiscaleType with content type ELEMENT_ONLY
class IdFiscaleType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}IdFiscaleType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IdFiscaleType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 59, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element IdPaese uses Python identifier IdPaese
    __IdPaese = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'IdPaese'), 'IdPaese', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_IdFiscaleType_IdPaese', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 61, 6), )

    
    IdPaese = property(__IdPaese.value, __IdPaese.set, None, None)

    
    # Element IdCodice uses Python identifier IdCodice
    __IdCodice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'IdCodice'), 'IdCodice', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_IdFiscaleType_IdCodice', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 62, 6), )

    
    IdCodice = property(__IdCodice.value, __IdCodice.set, None, None)

    _ElementMap.update({
        __IdPaese.name() : __IdPaese,
        __IdCodice.name() : __IdCodice
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.IdFiscaleType = IdFiscaleType
Namespace.addCategoryObject('typeBinding', 'IdFiscaleType', IdFiscaleType)


# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}DatiGeneraliType with content type ELEMENT_ONLY
class DatiGeneraliType (pyxb.binding.basis.complexTypeDefinition):
    """Blocco relativo ai Dati Generali della Fattura Elettronica"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatiGeneraliType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 81, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element DatiGeneraliDocumento uses Python identifier DatiGeneraliDocumento
    __DatiGeneraliDocumento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DatiGeneraliDocumento'), 'DatiGeneraliDocumento', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiGeneraliType_DatiGeneraliDocumento', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 86, 6), )

    
    DatiGeneraliDocumento = property(__DatiGeneraliDocumento.value, __DatiGeneraliDocumento.set, None, None)

    
    # Element DatiFatturaRettificata uses Python identifier DatiFatturaRettificata
    __DatiFatturaRettificata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DatiFatturaRettificata'), 'DatiFatturaRettificata', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiGeneraliType_DatiFatturaRettificata', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 87, 6), )

    
    DatiFatturaRettificata = property(__DatiFatturaRettificata.value, __DatiFatturaRettificata.set, None, None)

    _ElementMap.update({
        __DatiGeneraliDocumento.name() : __DatiGeneraliDocumento,
        __DatiFatturaRettificata.name() : __DatiFatturaRettificata
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DatiGeneraliType = DatiGeneraliType
Namespace.addCategoryObject('typeBinding', 'DatiGeneraliType', DatiGeneraliType)


# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}DatiGeneraliDocumentoType with content type ELEMENT_ONLY
class DatiGeneraliDocumentoType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}DatiGeneraliDocumentoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatiGeneraliDocumentoType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 90, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element TipoDocumento uses Python identifier TipoDocumento
    __TipoDocumento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoDocumento'), 'TipoDocumento', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiGeneraliDocumentoType_TipoDocumento', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 92, 6), )

    
    TipoDocumento = property(__TipoDocumento.value, __TipoDocumento.set, None, None)

    
    # Element Divisa uses Python identifier Divisa
    __Divisa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Divisa'), 'Divisa', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiGeneraliDocumentoType_Divisa', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 93, 6), )

    
    Divisa = property(__Divisa.value, __Divisa.set, None, None)

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Data'), 'Data', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiGeneraliDocumentoType_Data', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 94, 6), )

    
    Data = property(__Data.value, __Data.set, None, None)

    
    # Element Numero uses Python identifier Numero
    __Numero = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Numero'), 'Numero', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiGeneraliDocumentoType_Numero', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 95, 6), )

    
    Numero = property(__Numero.value, __Numero.set, None, None)

    
    # Element BolloVirtuale uses Python identifier BolloVirtuale
    __BolloVirtuale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BolloVirtuale'), 'BolloVirtuale', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiGeneraliDocumentoType_BolloVirtuale', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 96, 6), )

    
    BolloVirtuale = property(__BolloVirtuale.value, __BolloVirtuale.set, None, None)

    _ElementMap.update({
        __TipoDocumento.name() : __TipoDocumento,
        __Divisa.name() : __Divisa,
        __Data.name() : __Data,
        __Numero.name() : __Numero,
        __BolloVirtuale.name() : __BolloVirtuale
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DatiGeneraliDocumentoType = DatiGeneraliDocumentoType
Namespace.addCategoryObject('typeBinding', 'DatiGeneraliDocumentoType', DatiGeneraliDocumentoType)


# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}DatiFatturaRettificataType with content type ELEMENT_ONLY
class DatiFatturaRettificataType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}DatiFatturaRettificataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatiFatturaRettificataType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 99, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element NumeroFR uses Python identifier NumeroFR
    __NumeroFR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroFR'), 'NumeroFR', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiFatturaRettificataType_NumeroFR', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 101, 6), )

    
    NumeroFR = property(__NumeroFR.value, __NumeroFR.set, None, None)

    
    # Element DataFR uses Python identifier DataFR
    __DataFR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataFR'), 'DataFR', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiFatturaRettificataType_DataFR', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 102, 6), )

    
    DataFR = property(__DataFR.value, __DataFR.set, None, None)

    
    # Element ElementiRettificati uses Python identifier ElementiRettificati
    __ElementiRettificati = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ElementiRettificati'), 'ElementiRettificati', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiFatturaRettificataType_ElementiRettificati', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 103, 6), )

    
    ElementiRettificati = property(__ElementiRettificati.value, __ElementiRettificati.set, None, None)

    _ElementMap.update({
        __NumeroFR.name() : __NumeroFR,
        __DataFR.name() : __DataFR,
        __ElementiRettificati.name() : __ElementiRettificati
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DatiFatturaRettificataType = DatiFatturaRettificataType
Namespace.addCategoryObject('typeBinding', 'DatiFatturaRettificataType', DatiFatturaRettificataType)


# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}IndirizzoType with content type ELEMENT_ONLY
class IndirizzoType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}IndirizzoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IndirizzoType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 136, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Indirizzo uses Python identifier Indirizzo
    __Indirizzo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Indirizzo'), 'Indirizzo', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_IndirizzoType_Indirizzo', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 138, 6), )

    
    Indirizzo = property(__Indirizzo.value, __Indirizzo.set, None, None)

    
    # Element NumeroCivico uses Python identifier NumeroCivico
    __NumeroCivico = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroCivico'), 'NumeroCivico', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_IndirizzoType_NumeroCivico', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 139, 6), )

    
    NumeroCivico = property(__NumeroCivico.value, __NumeroCivico.set, None, None)

    
    # Element CAP uses Python identifier CAP
    __CAP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CAP'), 'CAP', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_IndirizzoType_CAP', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 140, 6), )

    
    CAP = property(__CAP.value, __CAP.set, None, None)

    
    # Element Comune uses Python identifier Comune
    __Comune = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comune'), 'Comune', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_IndirizzoType_Comune', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 141, 6), )

    
    Comune = property(__Comune.value, __Comune.set, None, None)

    
    # Element Provincia uses Python identifier Provincia
    __Provincia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Provincia'), 'Provincia', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_IndirizzoType_Provincia', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 142, 6), )

    
    Provincia = property(__Provincia.value, __Provincia.set, None, None)

    
    # Element Nazione uses Python identifier Nazione
    __Nazione = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Nazione'), 'Nazione', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_IndirizzoType_Nazione', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 143, 6), )

    
    Nazione = property(__Nazione.value, __Nazione.set, None, None)

    _ElementMap.update({
        __Indirizzo.name() : __Indirizzo,
        __NumeroCivico.name() : __NumeroCivico,
        __CAP.name() : __CAP,
        __Comune.name() : __Comune,
        __Provincia.name() : __Provincia,
        __Nazione.name() : __Nazione
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.IndirizzoType = IndirizzoType
Namespace.addCategoryObject('typeBinding', 'IndirizzoType', IndirizzoType)


# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}CedentePrestatoreType with content type ELEMENT_ONLY
class CedentePrestatoreType (pyxb.binding.basis.complexTypeDefinition):
    """Blocco relativo ai dati del Cedente / Prestatore"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CedentePrestatoreType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 161, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element IdFiscaleIVA uses Python identifier IdFiscaleIVA
    __IdFiscaleIVA = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'IdFiscaleIVA'), 'IdFiscaleIVA', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_CedentePrestatoreType_IdFiscaleIVA', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 166, 6), )

    
    IdFiscaleIVA = property(__IdFiscaleIVA.value, __IdFiscaleIVA.set, None, None)

    
    # Element CodiceFiscale uses Python identifier CodiceFiscale
    __CodiceFiscale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodiceFiscale'), 'CodiceFiscale', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_CedentePrestatoreType_CodiceFiscale', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 167, 6), )

    
    CodiceFiscale = property(__CodiceFiscale.value, __CodiceFiscale.set, None, None)

    
    # Element Denominazione uses Python identifier Denominazione
    __Denominazione = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Denominazione'), 'Denominazione', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_CedentePrestatoreType_Denominazione', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 170, 10), )

    
    Denominazione = property(__Denominazione.value, __Denominazione.set, None, None)

    
    # Element Nome uses Python identifier Nome
    __Nome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Nome'), 'Nome', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_CedentePrestatoreType_Nome', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 173, 10), )

    
    Nome = property(__Nome.value, __Nome.set, None, None)

    
    # Element Cognome uses Python identifier Cognome
    __Cognome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cognome'), 'Cognome', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_CedentePrestatoreType_Cognome', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 174, 10), )

    
    Cognome = property(__Cognome.value, __Cognome.set, None, None)

    
    # Element Sede uses Python identifier Sede
    __Sede = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Sede'), 'Sede', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_CedentePrestatoreType_Sede', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 177, 6), )

    
    Sede = property(__Sede.value, __Sede.set, None, None)

    
    # Element StabileOrganizzazione uses Python identifier StabileOrganizzazione
    __StabileOrganizzazione = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'StabileOrganizzazione'), 'StabileOrganizzazione', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_CedentePrestatoreType_StabileOrganizzazione', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 178, 6), )

    
    StabileOrganizzazione = property(__StabileOrganizzazione.value, __StabileOrganizzazione.set, None, None)

    
    # Element RappresentanteFiscale uses Python identifier RappresentanteFiscale
    __RappresentanteFiscale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RappresentanteFiscale'), 'RappresentanteFiscale', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_CedentePrestatoreType_RappresentanteFiscale', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 179, 6), )

    
    RappresentanteFiscale = property(__RappresentanteFiscale.value, __RappresentanteFiscale.set, None, None)

    
    # Element IscrizioneREA uses Python identifier IscrizioneREA
    __IscrizioneREA = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'IscrizioneREA'), 'IscrizioneREA', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_CedentePrestatoreType_IscrizioneREA', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 180, 6), )

    
    IscrizioneREA = property(__IscrizioneREA.value, __IscrizioneREA.set, None, None)

    
    # Element RegimeFiscale uses Python identifier RegimeFiscale
    __RegimeFiscale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RegimeFiscale'), 'RegimeFiscale', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_CedentePrestatoreType_RegimeFiscale', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 181, 3), )

    
    RegimeFiscale = property(__RegimeFiscale.value, __RegimeFiscale.set, None, None)

    _ElementMap.update({
        __IdFiscaleIVA.name() : __IdFiscaleIVA,
        __CodiceFiscale.name() : __CodiceFiscale,
        __Denominazione.name() : __Denominazione,
        __Nome.name() : __Nome,
        __Cognome.name() : __Cognome,
        __Sede.name() : __Sede,
        __StabileOrganizzazione.name() : __StabileOrganizzazione,
        __RappresentanteFiscale.name() : __RappresentanteFiscale,
        __IscrizioneREA.name() : __IscrizioneREA,
        __RegimeFiscale.name() : __RegimeFiscale
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CedentePrestatoreType = CedentePrestatoreType
Namespace.addCategoryObject('typeBinding', 'CedentePrestatoreType', CedentePrestatoreType)


# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}IscrizioneREAType with content type ELEMENT_ONLY
class IscrizioneREAType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}IscrizioneREAType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IscrizioneREAType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 279, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Ufficio uses Python identifier Ufficio
    __Ufficio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Ufficio'), 'Ufficio', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_IscrizioneREAType_Ufficio', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 281, 6), )

    
    Ufficio = property(__Ufficio.value, __Ufficio.set, None, None)

    
    # Element NumeroREA uses Python identifier NumeroREA
    __NumeroREA = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroREA'), 'NumeroREA', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_IscrizioneREAType_NumeroREA', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 282, 6), )

    
    NumeroREA = property(__NumeroREA.value, __NumeroREA.set, None, None)

    
    # Element CapitaleSociale uses Python identifier CapitaleSociale
    __CapitaleSociale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CapitaleSociale'), 'CapitaleSociale', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_IscrizioneREAType_CapitaleSociale', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 283, 6), )

    
    CapitaleSociale = property(__CapitaleSociale.value, __CapitaleSociale.set, None, None)

    
    # Element SocioUnico uses Python identifier SocioUnico
    __SocioUnico = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SocioUnico'), 'SocioUnico', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_IscrizioneREAType_SocioUnico', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 284, 6), )

    
    SocioUnico = property(__SocioUnico.value, __SocioUnico.set, None, None)

    
    # Element StatoLiquidazione uses Python identifier StatoLiquidazione
    __StatoLiquidazione = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'StatoLiquidazione'), 'StatoLiquidazione', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_IscrizioneREAType_StatoLiquidazione', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 285, 6), )

    
    StatoLiquidazione = property(__StatoLiquidazione.value, __StatoLiquidazione.set, None, None)

    _ElementMap.update({
        __Ufficio.name() : __Ufficio,
        __NumeroREA.name() : __NumeroREA,
        __CapitaleSociale.name() : __CapitaleSociale,
        __SocioUnico.name() : __SocioUnico,
        __StatoLiquidazione.name() : __StatoLiquidazione
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.IscrizioneREAType = IscrizioneREAType
Namespace.addCategoryObject('typeBinding', 'IscrizioneREAType', IscrizioneREAType)


# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}RappresentanteFiscaleType with content type ELEMENT_ONLY
class RappresentanteFiscaleType (pyxb.binding.basis.complexTypeDefinition):
    """Blocco relativo ai dati del Rappresentante Fiscale"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RappresentanteFiscaleType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 288, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element IdFiscaleIVA uses Python identifier IdFiscaleIVA
    __IdFiscaleIVA = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'IdFiscaleIVA'), 'IdFiscaleIVA', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_RappresentanteFiscaleType_IdFiscaleIVA', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 293, 3), )

    
    IdFiscaleIVA = property(__IdFiscaleIVA.value, __IdFiscaleIVA.set, None, None)

    
    # Element Denominazione uses Python identifier Denominazione
    __Denominazione = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Denominazione'), 'Denominazione', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_RappresentanteFiscaleType_Denominazione', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 296, 10), )

    
    Denominazione = property(__Denominazione.value, __Denominazione.set, None, None)

    
    # Element Nome uses Python identifier Nome
    __Nome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Nome'), 'Nome', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_RappresentanteFiscaleType_Nome', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 299, 10), )

    
    Nome = property(__Nome.value, __Nome.set, None, None)

    
    # Element Cognome uses Python identifier Cognome
    __Cognome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cognome'), 'Cognome', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_RappresentanteFiscaleType_Cognome', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 300, 10), )

    
    Cognome = property(__Cognome.value, __Cognome.set, None, None)

    _ElementMap.update({
        __IdFiscaleIVA.name() : __IdFiscaleIVA,
        __Denominazione.name() : __Denominazione,
        __Nome.name() : __Nome,
        __Cognome.name() : __Cognome
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RappresentanteFiscaleType = RappresentanteFiscaleType
Namespace.addCategoryObject('typeBinding', 'RappresentanteFiscaleType', RappresentanteFiscaleType)


# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}CessionarioCommittenteType with content type ELEMENT_ONLY
class CessionarioCommittenteType (pyxb.binding.basis.complexTypeDefinition):
    """Blocco relativo ai dati del Cessionario / Committente"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CessionarioCommittenteType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 305, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element IdentificativiFiscali uses Python identifier IdentificativiFiscali
    __IdentificativiFiscali = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'IdentificativiFiscali'), 'IdentificativiFiscali', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_CessionarioCommittenteType_IdentificativiFiscali', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 310, 6), )

    
    IdentificativiFiscali = property(__IdentificativiFiscali.value, __IdentificativiFiscali.set, None, None)

    
    # Element AltriDatiIdentificativi uses Python identifier AltriDatiIdentificativi
    __AltriDatiIdentificativi = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AltriDatiIdentificativi'), 'AltriDatiIdentificativi', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_CessionarioCommittenteType_AltriDatiIdentificativi', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 311, 6), )

    
    AltriDatiIdentificativi = property(__AltriDatiIdentificativi.value, __AltriDatiIdentificativi.set, None, None)

    _ElementMap.update({
        __IdentificativiFiscali.name() : __IdentificativiFiscali,
        __AltriDatiIdentificativi.name() : __AltriDatiIdentificativi
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CessionarioCommittenteType = CessionarioCommittenteType
Namespace.addCategoryObject('typeBinding', 'CessionarioCommittenteType', CessionarioCommittenteType)


# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}IdentificativiFiscaliType with content type ELEMENT_ONLY
class IdentificativiFiscaliType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}IdentificativiFiscaliType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IdentificativiFiscaliType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 314, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element IdFiscaleIVA uses Python identifier IdFiscaleIVA
    __IdFiscaleIVA = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'IdFiscaleIVA'), 'IdFiscaleIVA', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_IdentificativiFiscaliType_IdFiscaleIVA', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 316, 6), )

    
    IdFiscaleIVA = property(__IdFiscaleIVA.value, __IdFiscaleIVA.set, None, None)

    
    # Element CodiceFiscale uses Python identifier CodiceFiscale
    __CodiceFiscale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodiceFiscale'), 'CodiceFiscale', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_IdentificativiFiscaliType_CodiceFiscale', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 317, 6), )

    
    CodiceFiscale = property(__CodiceFiscale.value, __CodiceFiscale.set, None, None)

    _ElementMap.update({
        __IdFiscaleIVA.name() : __IdFiscaleIVA,
        __CodiceFiscale.name() : __CodiceFiscale
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.IdentificativiFiscaliType = IdentificativiFiscaliType
Namespace.addCategoryObject('typeBinding', 'IdentificativiFiscaliType', IdentificativiFiscaliType)


# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}AltriDatiIdentificativiType with content type ELEMENT_ONLY
class AltriDatiIdentificativiType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}AltriDatiIdentificativiType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AltriDatiIdentificativiType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 320, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Denominazione uses Python identifier Denominazione
    __Denominazione = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Denominazione'), 'Denominazione', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_AltriDatiIdentificativiType_Denominazione', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 324, 10), )

    
    Denominazione = property(__Denominazione.value, __Denominazione.set, None, None)

    
    # Element Nome uses Python identifier Nome
    __Nome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Nome'), 'Nome', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_AltriDatiIdentificativiType_Nome', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 327, 10), )

    
    Nome = property(__Nome.value, __Nome.set, None, None)

    
    # Element Cognome uses Python identifier Cognome
    __Cognome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cognome'), 'Cognome', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_AltriDatiIdentificativiType_Cognome', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 328, 10), )

    
    Cognome = property(__Cognome.value, __Cognome.set, None, None)

    
    # Element Sede uses Python identifier Sede
    __Sede = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Sede'), 'Sede', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_AltriDatiIdentificativiType_Sede', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 331, 6), )

    
    Sede = property(__Sede.value, __Sede.set, None, None)

    
    # Element StabileOrganizzazione uses Python identifier StabileOrganizzazione
    __StabileOrganizzazione = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'StabileOrganizzazione'), 'StabileOrganizzazione', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_AltriDatiIdentificativiType_StabileOrganizzazione', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 332, 6), )

    
    StabileOrganizzazione = property(__StabileOrganizzazione.value, __StabileOrganizzazione.set, None, None)

    
    # Element RappresentanteFiscale uses Python identifier RappresentanteFiscale
    __RappresentanteFiscale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RappresentanteFiscale'), 'RappresentanteFiscale', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_AltriDatiIdentificativiType_RappresentanteFiscale', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 333, 6), )

    
    RappresentanteFiscale = property(__RappresentanteFiscale.value, __RappresentanteFiscale.set, None, None)

    _ElementMap.update({
        __Denominazione.name() : __Denominazione,
        __Nome.name() : __Nome,
        __Cognome.name() : __Cognome,
        __Sede.name() : __Sede,
        __StabileOrganizzazione.name() : __StabileOrganizzazione,
        __RappresentanteFiscale.name() : __RappresentanteFiscale
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AltriDatiIdentificativiType = AltriDatiIdentificativiType
Namespace.addCategoryObject('typeBinding', 'AltriDatiIdentificativiType', AltriDatiIdentificativiType)


# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}DatiBeniServiziType with content type ELEMENT_ONLY
class DatiBeniServiziType (pyxb.binding.basis.complexTypeDefinition):
    """Blocco relativo ai dati di Beni Servizi della Fattura	Elettronica"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatiBeniServiziType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 336, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Descrizione uses Python identifier Descrizione
    __Descrizione = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Descrizione'), 'Descrizione', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiBeniServiziType_Descrizione', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 341, 6), )

    
    Descrizione = property(__Descrizione.value, __Descrizione.set, None, None)

    
    # Element Importo uses Python identifier Importo
    __Importo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Importo'), 'Importo', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiBeniServiziType_Importo', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 342, 6), )

    
    Importo = property(__Importo.value, __Importo.set, None, None)

    
    # Element DatiIVA uses Python identifier DatiIVA
    __DatiIVA = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DatiIVA'), 'DatiIVA', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiBeniServiziType_DatiIVA', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 343, 6), )

    
    DatiIVA = property(__DatiIVA.value, __DatiIVA.set, None, None)

    
    # Element Natura uses Python identifier Natura
    __Natura = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Natura'), 'Natura', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiBeniServiziType_Natura', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 344, 6), )

    
    Natura = property(__Natura.value, __Natura.set, None, None)

    
    # Element RiferimentoNormativo uses Python identifier RiferimentoNormativo
    __RiferimentoNormativo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RiferimentoNormativo'), 'RiferimentoNormativo', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiBeniServiziType_RiferimentoNormativo', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 345, 6), )

    
    RiferimentoNormativo = property(__RiferimentoNormativo.value, __RiferimentoNormativo.set, None, None)

    _ElementMap.update({
        __Descrizione.name() : __Descrizione,
        __Importo.name() : __Importo,
        __DatiIVA.name() : __DatiIVA,
        __Natura.name() : __Natura,
        __RiferimentoNormativo.name() : __RiferimentoNormativo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DatiBeniServiziType = DatiBeniServiziType
Namespace.addCategoryObject('typeBinding', 'DatiBeniServiziType', DatiBeniServiziType)


# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}DatiIVAType with content type ELEMENT_ONLY
class DatiIVAType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}DatiIVAType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatiIVAType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 348, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Imposta uses Python identifier Imposta
    __Imposta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Imposta'), 'Imposta', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiIVAType_Imposta', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 350, 6), )

    
    Imposta = property(__Imposta.value, __Imposta.set, None, None)

    
    # Element Aliquota uses Python identifier Aliquota
    __Aliquota = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Aliquota'), 'Aliquota', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_DatiIVAType_Aliquota', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 351, 3), )

    
    Aliquota = property(__Aliquota.value, __Aliquota.set, None, None)

    _ElementMap.update({
        __Imposta.name() : __Imposta,
        __Aliquota.name() : __Aliquota
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DatiIVAType = DatiIVAType
Namespace.addCategoryObject('typeBinding', 'DatiIVAType', DatiIVAType)


# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}AllegatiType with content type ELEMENT_ONLY
class AllegatiType (pyxb.binding.basis.complexTypeDefinition):
    """Blocco relativo ai dati di eventuali allegati"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AllegatiType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 354, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element NomeAttachment uses Python identifier NomeAttachment
    __NomeAttachment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NomeAttachment'), 'NomeAttachment', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_AllegatiType_NomeAttachment', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 359, 6), )

    
    NomeAttachment = property(__NomeAttachment.value, __NomeAttachment.set, None, None)

    
    # Element AlgoritmoCompressione uses Python identifier AlgoritmoCompressione
    __AlgoritmoCompressione = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AlgoritmoCompressione'), 'AlgoritmoCompressione', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_AllegatiType_AlgoritmoCompressione', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 360, 6), )

    
    AlgoritmoCompressione = property(__AlgoritmoCompressione.value, __AlgoritmoCompressione.set, None, None)

    
    # Element FormatoAttachment uses Python identifier FormatoAttachment
    __FormatoAttachment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FormatoAttachment'), 'FormatoAttachment', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_AllegatiType_FormatoAttachment', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 361, 6), )

    
    FormatoAttachment = property(__FormatoAttachment.value, __FormatoAttachment.set, None, None)

    
    # Element DescrizioneAttachment uses Python identifier DescrizioneAttachment
    __DescrizioneAttachment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DescrizioneAttachment'), 'DescrizioneAttachment', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_AllegatiType_DescrizioneAttachment', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 362, 6), )

    
    DescrizioneAttachment = property(__DescrizioneAttachment.value, __DescrizioneAttachment.set, None, None)

    
    # Element Attachment uses Python identifier Attachment
    __Attachment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Attachment'), 'Attachment', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_AllegatiType_Attachment', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 363, 6), )

    
    Attachment = property(__Attachment.value, __Attachment.set, None, None)

    _ElementMap.update({
        __NomeAttachment.name() : __NomeAttachment,
        __AlgoritmoCompressione.name() : __AlgoritmoCompressione,
        __FormatoAttachment.name() : __FormatoAttachment,
        __DescrizioneAttachment.name() : __DescrizioneAttachment,
        __Attachment.name() : __Attachment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AllegatiType = AllegatiType
Namespace.addCategoryObject('typeBinding', 'AllegatiType', AllegatiType)


# Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}FatturaElettronicaType with content type ELEMENT_ONLY
class FatturaElettronicaType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.0}FatturaElettronicaType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FatturaElettronicaType')
    _XSDLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 18, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element FatturaElettronicaHeader uses Python identifier FatturaElettronicaHeader
    __FatturaElettronicaHeader = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FatturaElettronicaHeader'), 'FatturaElettronicaHeader', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_FatturaElettronicaType_FatturaElettronicaHeader', False, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 20, 6), )

    
    FatturaElettronicaHeader = property(__FatturaElettronicaHeader.value, __FatturaElettronicaHeader.set, None, None)

    
    # Element FatturaElettronicaBody uses Python identifier FatturaElettronicaBody
    __FatturaElettronicaBody = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FatturaElettronicaBody'), 'FatturaElettronicaBody', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_FatturaElettronicaType_FatturaElettronicaBody', True, pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 21, 6), )

    
    FatturaElettronicaBody = property(__FatturaElettronicaBody.value, __FatturaElettronicaBody.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), 'Signature', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_FatturaElettronicaType_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 43, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    
    # Attribute versione uses Python identifier versione
    __versione = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'versione'), 'versione', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_FatturaElettronicaType_versione', _module_typeBindings.FormatoTrasmissioneType, required=True)
    __versione._DeclarationLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 24, 4)
    __versione._UseLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 24, 4)
    
    versione = property(__versione.value, __versione.set, None, None)

    
    # Attribute SistemaEmittente uses Python identifier SistemaEmittente
    __SistemaEmittente = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SistemaEmittente'), 'SistemaEmittente', '__httpivaservizi_agenziaentrate_gov_itdocsxsdfatturev1_0_FatturaElettronicaType_SistemaEmittente', _module_typeBindings.String10Type)
    __SistemaEmittente._DeclarationLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 25, 4)
    __SistemaEmittente._UseLocation = pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 25, 4)
    
    SistemaEmittente = property(__SistemaEmittente.value, __SistemaEmittente.set, None, None)

    _ElementMap.update({
        __FatturaElettronicaHeader.name() : __FatturaElettronicaHeader,
        __FatturaElettronicaBody.name() : __FatturaElettronicaBody,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        __versione.name() : __versione,
        __SistemaEmittente.name() : __SistemaEmittente
    })
_module_typeBindings.FatturaElettronicaType = FatturaElettronicaType
Namespace.addCategoryObject('typeBinding', 'FatturaElettronicaType', FatturaElettronicaType)


FatturaElettronicaSemplificata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FatturaElettronicaSemplificata'), FatturaElettronicaType, documentation='\n\t\t\t\tXML schema fatture destinate a privati in forma semplificata 1.0.1\n\t\t\t', location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 11, 2))
Namespace.addCategoryObject('elementBinding', FatturaElettronicaSemplificata.name().localName(), FatturaElettronicaSemplificata)



FatturaElettronicaHeaderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DatiTrasmissione'), DatiTrasmissioneType, scope=FatturaElettronicaHeaderType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 29, 6)))

FatturaElettronicaHeaderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CedentePrestatore'), CedentePrestatoreType, scope=FatturaElettronicaHeaderType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 30, 6)))

FatturaElettronicaHeaderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CessionarioCommittente'), CessionarioCommittenteType, scope=FatturaElettronicaHeaderType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 31, 6)))

FatturaElettronicaHeaderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SoggettoEmittente'), SoggettoEmittenteType, scope=FatturaElettronicaHeaderType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 32, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 32, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FatturaElettronicaHeaderType._UseForTag(pyxb.namespace.ExpandedName(None, 'DatiTrasmissione')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 29, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FatturaElettronicaHeaderType._UseForTag(pyxb.namespace.ExpandedName(None, 'CedentePrestatore')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 30, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FatturaElettronicaHeaderType._UseForTag(pyxb.namespace.ExpandedName(None, 'CessionarioCommittente')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 31, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FatturaElettronicaHeaderType._UseForTag(pyxb.namespace.ExpandedName(None, 'SoggettoEmittente')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 32, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FatturaElettronicaHeaderType._Automaton = _BuildAutomaton()




FatturaElettronicaBodyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DatiGenerali'), DatiGeneraliType, scope=FatturaElettronicaBodyType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 37, 6)))

FatturaElettronicaBodyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DatiBeniServizi'), DatiBeniServiziType, scope=FatturaElettronicaBodyType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 38, 6)))

FatturaElettronicaBodyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Allegati'), AllegatiType, scope=FatturaElettronicaBodyType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 39, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 39, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FatturaElettronicaBodyType._UseForTag(pyxb.namespace.ExpandedName(None, 'DatiGenerali')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 37, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FatturaElettronicaBodyType._UseForTag(pyxb.namespace.ExpandedName(None, 'DatiBeniServizi')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 38, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FatturaElettronicaBodyType._UseForTag(pyxb.namespace.ExpandedName(None, 'Allegati')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 39, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FatturaElettronicaBodyType._Automaton = _BuildAutomaton_()




DatiTrasmissioneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'IdTrasmittente'), IdFiscaleType, scope=DatiTrasmissioneType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 47, 6)))

DatiTrasmissioneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ProgressivoInvio'), String10Type, scope=DatiTrasmissioneType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 48, 6)))

DatiTrasmissioneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FormatoTrasmissione'), FormatoTrasmissioneType, scope=DatiTrasmissioneType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 49, 6)))

DatiTrasmissioneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodiceDestinatario'), CodiceDestinatarioType, scope=DatiTrasmissioneType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 50, 6)))

DatiTrasmissioneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PECDestinatario'), EmailType, scope=DatiTrasmissioneType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 51, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 51, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatiTrasmissioneType._UseForTag(pyxb.namespace.ExpandedName(None, 'IdTrasmittente')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 47, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatiTrasmissioneType._UseForTag(pyxb.namespace.ExpandedName(None, 'ProgressivoInvio')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 48, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatiTrasmissioneType._UseForTag(pyxb.namespace.ExpandedName(None, 'FormatoTrasmissione')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 49, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DatiTrasmissioneType._UseForTag(pyxb.namespace.ExpandedName(None, 'CodiceDestinatario')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 50, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DatiTrasmissioneType._UseForTag(pyxb.namespace.ExpandedName(None, 'PECDestinatario')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 51, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DatiTrasmissioneType._Automaton = _BuildAutomaton_2()




IdFiscaleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'IdPaese'), NazioneType, scope=IdFiscaleType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 61, 6)))

IdFiscaleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'IdCodice'), CodiceType, scope=IdFiscaleType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 62, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(IdFiscaleType._UseForTag(pyxb.namespace.ExpandedName(None, 'IdPaese')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 61, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(IdFiscaleType._UseForTag(pyxb.namespace.ExpandedName(None, 'IdCodice')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 62, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
IdFiscaleType._Automaton = _BuildAutomaton_3()




DatiGeneraliType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DatiGeneraliDocumento'), DatiGeneraliDocumentoType, scope=DatiGeneraliType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 86, 6)))

DatiGeneraliType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DatiFatturaRettificata'), DatiFatturaRettificataType, scope=DatiGeneraliType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 87, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 87, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DatiGeneraliType._UseForTag(pyxb.namespace.ExpandedName(None, 'DatiGeneraliDocumento')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 86, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DatiGeneraliType._UseForTag(pyxb.namespace.ExpandedName(None, 'DatiFatturaRettificata')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 87, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DatiGeneraliType._Automaton = _BuildAutomaton_4()




DatiGeneraliDocumentoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoDocumento'), TipoDocumentoType, scope=DatiGeneraliDocumentoType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 92, 6)))

DatiGeneraliDocumentoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Divisa'), DivisaType, scope=DatiGeneraliDocumentoType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 93, 6)))

DatiGeneraliDocumentoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Data'), DataFatturaType, scope=DatiGeneraliDocumentoType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 94, 6)))

DatiGeneraliDocumentoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Numero'), String20Type, scope=DatiGeneraliDocumentoType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 95, 6)))

DatiGeneraliDocumentoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BolloVirtuale'), BolloVirtualeType, scope=DatiGeneraliDocumentoType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 96, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 96, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatiGeneraliDocumentoType._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoDocumento')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 92, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatiGeneraliDocumentoType._UseForTag(pyxb.namespace.ExpandedName(None, 'Divisa')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 93, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatiGeneraliDocumentoType._UseForTag(pyxb.namespace.ExpandedName(None, 'Data')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 94, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DatiGeneraliDocumentoType._UseForTag(pyxb.namespace.ExpandedName(None, 'Numero')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 95, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DatiGeneraliDocumentoType._UseForTag(pyxb.namespace.ExpandedName(None, 'BolloVirtuale')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 96, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DatiGeneraliDocumentoType._Automaton = _BuildAutomaton_5()




DatiFatturaRettificataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroFR'), String20Type, scope=DatiFatturaRettificataType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 101, 6)))

DatiFatturaRettificataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataFR'), DataFatturaType, scope=DatiFatturaRettificataType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 102, 6)))

DatiFatturaRettificataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ElementiRettificati'), String1000LatinType, scope=DatiFatturaRettificataType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 103, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatiFatturaRettificataType._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroFR')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 101, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatiFatturaRettificataType._UseForTag(pyxb.namespace.ExpandedName(None, 'DataFR')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 102, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DatiFatturaRettificataType._UseForTag(pyxb.namespace.ExpandedName(None, 'ElementiRettificati')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 103, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DatiFatturaRettificataType._Automaton = _BuildAutomaton_6()




IndirizzoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Indirizzo'), String60LatinType, scope=IndirizzoType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 138, 6)))

IndirizzoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroCivico'), NumeroCivicoType, scope=IndirizzoType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 139, 6)))

IndirizzoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CAP'), CAPType, scope=IndirizzoType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 140, 6)))

IndirizzoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comune'), String60LatinType, scope=IndirizzoType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 141, 6)))

IndirizzoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Provincia'), ProvinciaType, scope=IndirizzoType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 142, 6)))

IndirizzoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Nazione'), NazioneType, scope=IndirizzoType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 143, 6), unicode_default='IT'))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 139, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 142, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(IndirizzoType._UseForTag(pyxb.namespace.ExpandedName(None, 'Indirizzo')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 138, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(IndirizzoType._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroCivico')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 139, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(IndirizzoType._UseForTag(pyxb.namespace.ExpandedName(None, 'CAP')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 140, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(IndirizzoType._UseForTag(pyxb.namespace.ExpandedName(None, 'Comune')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 141, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(IndirizzoType._UseForTag(pyxb.namespace.ExpandedName(None, 'Provincia')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 142, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(IndirizzoType._UseForTag(pyxb.namespace.ExpandedName(None, 'Nazione')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 143, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
IndirizzoType._Automaton = _BuildAutomaton_7()




CedentePrestatoreType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'IdFiscaleIVA'), IdFiscaleType, scope=CedentePrestatoreType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 166, 6)))

CedentePrestatoreType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodiceFiscale'), CodiceFiscaleType, scope=CedentePrestatoreType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 167, 6)))

CedentePrestatoreType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Denominazione'), String80LatinType, scope=CedentePrestatoreType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 170, 10)))

CedentePrestatoreType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Nome'), String60LatinType, scope=CedentePrestatoreType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 173, 10)))

CedentePrestatoreType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cognome'), String60LatinType, scope=CedentePrestatoreType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 174, 10)))

CedentePrestatoreType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Sede'), IndirizzoType, scope=CedentePrestatoreType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 177, 6)))

CedentePrestatoreType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'StabileOrganizzazione'), IndirizzoType, scope=CedentePrestatoreType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 178, 6)))

CedentePrestatoreType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RappresentanteFiscale'), RappresentanteFiscaleType, scope=CedentePrestatoreType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 179, 6)))

CedentePrestatoreType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'IscrizioneREA'), IscrizioneREAType, scope=CedentePrestatoreType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 180, 6)))

CedentePrestatoreType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RegimeFiscale'), RegimeFiscaleType, scope=CedentePrestatoreType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 181, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 167, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 178, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 179, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 180, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CedentePrestatoreType._UseForTag(pyxb.namespace.ExpandedName(None, 'IdFiscaleIVA')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 166, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CedentePrestatoreType._UseForTag(pyxb.namespace.ExpandedName(None, 'CodiceFiscale')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 167, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CedentePrestatoreType._UseForTag(pyxb.namespace.ExpandedName(None, 'Denominazione')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 170, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CedentePrestatoreType._UseForTag(pyxb.namespace.ExpandedName(None, 'Nome')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 173, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CedentePrestatoreType._UseForTag(pyxb.namespace.ExpandedName(None, 'Cognome')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 174, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CedentePrestatoreType._UseForTag(pyxb.namespace.ExpandedName(None, 'Sede')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 177, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CedentePrestatoreType._UseForTag(pyxb.namespace.ExpandedName(None, 'StabileOrganizzazione')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 178, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CedentePrestatoreType._UseForTag(pyxb.namespace.ExpandedName(None, 'RappresentanteFiscale')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 179, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CedentePrestatoreType._UseForTag(pyxb.namespace.ExpandedName(None, 'IscrizioneREA')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 180, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CedentePrestatoreType._UseForTag(pyxb.namespace.ExpandedName(None, 'RegimeFiscale')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 181, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CedentePrestatoreType._Automaton = _BuildAutomaton_8()




IscrizioneREAType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Ufficio'), ProvinciaType, scope=IscrizioneREAType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 281, 6)))

IscrizioneREAType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroREA'), String20Type, scope=IscrizioneREAType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 282, 6)))

IscrizioneREAType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CapitaleSociale'), Amount2DecimalType, scope=IscrizioneREAType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 283, 6)))

IscrizioneREAType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SocioUnico'), SocioUnicoType, scope=IscrizioneREAType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 284, 6)))

IscrizioneREAType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'StatoLiquidazione'), StatoLiquidazioneType, scope=IscrizioneREAType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 285, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 283, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 284, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(IscrizioneREAType._UseForTag(pyxb.namespace.ExpandedName(None, 'Ufficio')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 281, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(IscrizioneREAType._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroREA')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 282, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(IscrizioneREAType._UseForTag(pyxb.namespace.ExpandedName(None, 'CapitaleSociale')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 283, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(IscrizioneREAType._UseForTag(pyxb.namespace.ExpandedName(None, 'SocioUnico')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 284, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(IscrizioneREAType._UseForTag(pyxb.namespace.ExpandedName(None, 'StatoLiquidazione')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 285, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
IscrizioneREAType._Automaton = _BuildAutomaton_9()




RappresentanteFiscaleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'IdFiscaleIVA'), IdFiscaleType, scope=RappresentanteFiscaleType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 293, 3)))

RappresentanteFiscaleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Denominazione'), String80LatinType, scope=RappresentanteFiscaleType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 296, 10)))

RappresentanteFiscaleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Nome'), String60LatinType, scope=RappresentanteFiscaleType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 299, 10)))

RappresentanteFiscaleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cognome'), String60LatinType, scope=RappresentanteFiscaleType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 300, 10)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RappresentanteFiscaleType._UseForTag(pyxb.namespace.ExpandedName(None, 'IdFiscaleIVA')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 293, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RappresentanteFiscaleType._UseForTag(pyxb.namespace.ExpandedName(None, 'Denominazione')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 296, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RappresentanteFiscaleType._UseForTag(pyxb.namespace.ExpandedName(None, 'Nome')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 299, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RappresentanteFiscaleType._UseForTag(pyxb.namespace.ExpandedName(None, 'Cognome')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 300, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RappresentanteFiscaleType._Automaton = _BuildAutomaton_10()




CessionarioCommittenteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'IdentificativiFiscali'), IdentificativiFiscaliType, scope=CessionarioCommittenteType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 310, 6)))

CessionarioCommittenteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AltriDatiIdentificativi'), AltriDatiIdentificativiType, scope=CessionarioCommittenteType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 311, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 311, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CessionarioCommittenteType._UseForTag(pyxb.namespace.ExpandedName(None, 'IdentificativiFiscali')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 310, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CessionarioCommittenteType._UseForTag(pyxb.namespace.ExpandedName(None, 'AltriDatiIdentificativi')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 311, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CessionarioCommittenteType._Automaton = _BuildAutomaton_11()




IdentificativiFiscaliType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'IdFiscaleIVA'), IdFiscaleType, scope=IdentificativiFiscaliType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 316, 6)))

IdentificativiFiscaliType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodiceFiscale'), CodiceFiscaleType, scope=IdentificativiFiscaliType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 317, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 316, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 317, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IdentificativiFiscaliType._UseForTag(pyxb.namespace.ExpandedName(None, 'IdFiscaleIVA')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 316, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IdentificativiFiscaliType._UseForTag(pyxb.namespace.ExpandedName(None, 'CodiceFiscale')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 317, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IdentificativiFiscaliType._Automaton = _BuildAutomaton_12()




AltriDatiIdentificativiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Denominazione'), String80LatinType, scope=AltriDatiIdentificativiType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 324, 10)))

AltriDatiIdentificativiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Nome'), String60LatinType, scope=AltriDatiIdentificativiType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 327, 10)))

AltriDatiIdentificativiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cognome'), String60LatinType, scope=AltriDatiIdentificativiType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 328, 10)))

AltriDatiIdentificativiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Sede'), IndirizzoType, scope=AltriDatiIdentificativiType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 331, 6)))

AltriDatiIdentificativiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'StabileOrganizzazione'), IndirizzoType, scope=AltriDatiIdentificativiType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 332, 6)))

AltriDatiIdentificativiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RappresentanteFiscale'), RappresentanteFiscaleType, scope=AltriDatiIdentificativiType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 333, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 332, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 333, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AltriDatiIdentificativiType._UseForTag(pyxb.namespace.ExpandedName(None, 'Denominazione')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 324, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AltriDatiIdentificativiType._UseForTag(pyxb.namespace.ExpandedName(None, 'Nome')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 327, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AltriDatiIdentificativiType._UseForTag(pyxb.namespace.ExpandedName(None, 'Cognome')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 328, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AltriDatiIdentificativiType._UseForTag(pyxb.namespace.ExpandedName(None, 'Sede')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 331, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AltriDatiIdentificativiType._UseForTag(pyxb.namespace.ExpandedName(None, 'StabileOrganizzazione')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 332, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AltriDatiIdentificativiType._UseForTag(pyxb.namespace.ExpandedName(None, 'RappresentanteFiscale')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 333, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AltriDatiIdentificativiType._Automaton = _BuildAutomaton_13()




DatiBeniServiziType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Descrizione'), String1000LatinType, scope=DatiBeniServiziType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 341, 6)))

DatiBeniServiziType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Importo'), Amount2DecimalType, scope=DatiBeniServiziType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 342, 6)))

DatiBeniServiziType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DatiIVA'), DatiIVAType, scope=DatiBeniServiziType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 343, 6)))

DatiBeniServiziType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Natura'), NaturaType, scope=DatiBeniServiziType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 344, 6)))

DatiBeniServiziType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RiferimentoNormativo'), String100LatinType, scope=DatiBeniServiziType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 345, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 344, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 345, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatiBeniServiziType._UseForTag(pyxb.namespace.ExpandedName(None, 'Descrizione')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 341, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatiBeniServiziType._UseForTag(pyxb.namespace.ExpandedName(None, 'Importo')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 342, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DatiBeniServiziType._UseForTag(pyxb.namespace.ExpandedName(None, 'DatiIVA')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 343, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DatiBeniServiziType._UseForTag(pyxb.namespace.ExpandedName(None, 'Natura')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 344, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DatiBeniServiziType._UseForTag(pyxb.namespace.ExpandedName(None, 'RiferimentoNormativo')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 345, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DatiBeniServiziType._Automaton = _BuildAutomaton_14()




DatiIVAType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Imposta'), Amount2DecimalType, scope=DatiIVAType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 350, 6)))

DatiIVAType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Aliquota'), RateType, scope=DatiIVAType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 351, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 350, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 351, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DatiIVAType._UseForTag(pyxb.namespace.ExpandedName(None, 'Imposta')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 350, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DatiIVAType._UseForTag(pyxb.namespace.ExpandedName(None, 'Aliquota')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 351, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DatiIVAType._Automaton = _BuildAutomaton_15()




AllegatiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NomeAttachment'), String60LatinType, scope=AllegatiType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 359, 6)))

AllegatiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AlgoritmoCompressione'), String10Type, scope=AllegatiType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 360, 6)))

AllegatiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FormatoAttachment'), String10Type, scope=AllegatiType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 361, 6)))

AllegatiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DescrizioneAttachment'), String100LatinType, scope=AllegatiType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 362, 6)))

AllegatiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Attachment'), pyxb.binding.datatypes.base64Binary, scope=AllegatiType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 363, 6)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 360, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 361, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 362, 6))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AllegatiType._UseForTag(pyxb.namespace.ExpandedName(None, 'NomeAttachment')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 359, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AllegatiType._UseForTag(pyxb.namespace.ExpandedName(None, 'AlgoritmoCompressione')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 360, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AllegatiType._UseForTag(pyxb.namespace.ExpandedName(None, 'FormatoAttachment')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 361, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AllegatiType._UseForTag(pyxb.namespace.ExpandedName(None, 'DescrizioneAttachment')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 362, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AllegatiType._UseForTag(pyxb.namespace.ExpandedName(None, 'Attachment')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 363, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AllegatiType._Automaton = _BuildAutomaton_16()




FatturaElettronicaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FatturaElettronicaHeader'), FatturaElettronicaHeaderType, scope=FatturaElettronicaType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 20, 6)))

FatturaElettronicaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FatturaElettronicaBody'), FatturaElettronicaBodyType, scope=FatturaElettronicaType, location=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 21, 6)))

FatturaElettronicaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), _ImportedBinding__ds.SignatureType, scope=FatturaElettronicaType, location=pyxb.utils.utility.Location('http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 43, 0)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 22, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FatturaElettronicaType._UseForTag(pyxb.namespace.ExpandedName(None, 'FatturaElettronicaHeader')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 20, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FatturaElettronicaType._UseForTag(pyxb.namespace.ExpandedName(None, 'FatturaElettronicaBody')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 21, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FatturaElettronicaType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature')), pyxb.utils.utility.Location('/srv/webapp/odoo-12/buildout/parts/cogito/accounting_full/bindings_semplified_invoice/xsd/Schema_Fattura_semplificata.xsd', 22, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FatturaElettronicaType._Automaton = _BuildAutomaton_17()

