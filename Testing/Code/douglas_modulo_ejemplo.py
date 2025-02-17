# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
elif six.PY2:
  import __builtin__

class yc_animal_douglas_modulo_ejemplo__animales_animal(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module douglas-modulo-ejemplo - based on the path /animales/animal. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__filo','__clase','__especie','__edad',)

  _yang_name = 'animal'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__edad = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={u'range': [u'1..300']}), is_leaf=True, yang_name="edad", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='edad', is_config=True)
    self.__especie = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="especie", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='string', is_config=True)
    self.__clase = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="clase", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='string', is_config=True)
    self.__filo = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="filo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='string', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'animales', u'animal']

  def _get_filo(self):
    """
    Getter method for filo, mapped from YANG variable /animales/animal/filo (string)
    """
    return self.__filo
      
  def _set_filo(self, v, load=False):
    """
    Setter method for filo, mapped from YANG variable /animales/animal/filo (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_filo is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_filo() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="filo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """filo must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="filo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='string', is_config=True)""",
        })

    self.__filo = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_filo(self):
    self.__filo = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="filo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='string', is_config=True)


  def _get_clase(self):
    """
    Getter method for clase, mapped from YANG variable /animales/animal/clase (string)
    """
    return self.__clase
      
  def _set_clase(self, v, load=False):
    """
    Setter method for clase, mapped from YANG variable /animales/animal/clase (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_clase is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_clase() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="clase", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """clase must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="clase", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='string', is_config=True)""",
        })

    self.__clase = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_clase(self):
    self.__clase = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="clase", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='string', is_config=True)


  def _get_especie(self):
    """
    Getter method for especie, mapped from YANG variable /animales/animal/especie (string)
    """
    return self.__especie
      
  def _set_especie(self, v, load=False):
    """
    Setter method for especie, mapped from YANG variable /animales/animal/especie (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_especie is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_especie() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="especie", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """especie must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="especie", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='string', is_config=True)""",
        })

    self.__especie = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_especie(self):
    self.__especie = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="especie", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='string', is_config=True)


  def _get_edad(self):
    """
    Getter method for edad, mapped from YANG variable /animales/animal/edad (edad)
    """
    return self.__edad
      
  def _set_edad(self, v, load=False):
    """
    Setter method for edad, mapped from YANG variable /animales/animal/edad (edad)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_edad is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_edad() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={u'range': [u'1..300']}), is_leaf=True, yang_name="edad", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='edad', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """edad must be of a type compatible with edad""",
          'defined-type': "douglas-modulo-ejemplo:edad",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={u'range': [u'1..300']}), is_leaf=True, yang_name="edad", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='edad', is_config=True)""",
        })

    self.__edad = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_edad(self):
    self.__edad = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={u'range': [u'1..300']}), is_leaf=True, yang_name="edad", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='edad', is_config=True)

  filo = __builtin__.property(_get_filo, _set_filo)
  clase = __builtin__.property(_get_clase, _set_clase)
  especie = __builtin__.property(_get_especie, _set_especie)
  edad = __builtin__.property(_get_edad, _set_edad)


  _pyangbind_elements = OrderedDict([('filo', filo), ('clase', clase), ('especie', especie), ('edad', edad), ])


class yc_animales_douglas_modulo_ejemplo__animales(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module douglas-modulo-ejemplo - based on the path /animales. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__animal',)

  _yang_name = 'animales'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__animal = YANGDynClass(base=YANGListType("especie",yc_animal_douglas_modulo_ejemplo__animales_animal, yang_name="animal", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='especie', extensions=None), is_container='list', yang_name="animal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='list', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'animales']

  def _get_animal(self):
    """
    Getter method for animal, mapped from YANG variable /animales/animal (list)
    """
    return self.__animal
      
  def _set_animal(self, v, load=False):
    """
    Setter method for animal, mapped from YANG variable /animales/animal (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_animal is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_animal() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("especie",yc_animal_douglas_modulo_ejemplo__animales_animal, yang_name="animal", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='especie', extensions=None), is_container='list', yang_name="animal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """animal must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("especie",yc_animal_douglas_modulo_ejemplo__animales_animal, yang_name="animal", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='especie', extensions=None), is_container='list', yang_name="animal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='list', is_config=True)""",
        })

    self.__animal = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_animal(self):
    self.__animal = YANGDynClass(base=YANGListType("especie",yc_animal_douglas_modulo_ejemplo__animales_animal, yang_name="animal", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='especie', extensions=None), is_container='list', yang_name="animal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='list', is_config=True)

  animal = __builtin__.property(_get_animal, _set_animal)


  _pyangbind_elements = OrderedDict([('animal', animal), ])


class douglas_modulo_ejemplo(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module douglas-modulo-ejemplo - based on the path /douglas-modulo-ejemplo. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Este es un módulo de ejemplo, el cuál modela a un animal
  """
  __slots__ = ('_path_helper', '_extmethods', '__animales',)

  _yang_name = 'douglas-modulo-ejemplo'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__animales = YANGDynClass(base=yc_animales_douglas_modulo_ejemplo__animales, is_container='container', yang_name="animales", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return []

  def _get_animales(self):
    """
    Getter method for animales, mapped from YANG variable /animales (container)
    """
    return self.__animales
      
  def _set_animales(self, v, load=False):
    """
    Setter method for animales, mapped from YANG variable /animales (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_animales is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_animales() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_animales_douglas_modulo_ejemplo__animales, is_container='container', yang_name="animales", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """animales must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_animales_douglas_modulo_ejemplo__animales, is_container='container', yang_name="animales", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='container', is_config=True)""",
        })

    self.__animales = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_animales(self):
    self.__animales = YANGDynClass(base=yc_animales_douglas_modulo_ejemplo__animales, is_container='container', yang_name="animales", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://www.uis.edu.co', defining_module='douglas-modulo-ejemplo', yang_type='container', is_config=True)

  animales = __builtin__.property(_get_animales, _set_animales)


  _pyangbind_elements = OrderedDict([('animales', animales), ])


