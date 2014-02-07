import unittest

from django.contrib.auth.models import User
from django.db import models

import autocomplete_light


class Noname(models.Model):
    number = models.CharField(max_length=100)


class Foo(models.Model):
    name = models.CharField(max_length=100)


class Bar(autocomplete_light.AutocompleteModelBase):
    pass


class Generic(autocomplete_light.AutocompleteGenericBase):
    choices = (
        User.objects.all(),
    )
    search_fields = (
        ('username',),
    )


class RegistryTestCase(unittest.TestCase):
    def setUp(self):
        self.registry = autocomplete_light.AutocompleteRegistry()

    def test_register_model(self):
        self.registry.register(Foo)
        self.assertIn('FooAutocomplete', self.registry.keys())

    def test_register_model_and_autocomplete(self):
        self.registry.register(Foo, Bar)
        self.assertIn('FooBar', self.registry.keys())

    def test_register_autocomplete(self):
        self.registry.register(Bar)
        self.assertIn('Bar', self.registry.keys())

    def test_unregister(self):
        self.registry.register(Bar)
        self.registry.unregister('Bar')
        self.assertEqual(list(self.registry.keys()), [])

    def test_register_with_kwargs(self):
        choices = ['foo']
        self.registry.register(Foo, search_name='search_name', choices=choices)
        self.assertEqual(self.registry['FooAutocomplete'].search_name,
            'search_name')
        self.assertEqual(self.registry['FooAutocomplete'].choices, choices)

    def test_register_with_custom_autocomplete_model_base(self):
        class NewBase(autocomplete_light.AutocompleteModelBase):
            new_base = True

        self.registry.autocomplete_model_base = NewBase
        self.registry.register(Foo)
        self.assertEqual(NewBase, self.registry['FooAutocomplete'].__base__)
        self.assertTrue(self.registry['FooAutocomplete'].new_base)

    def test_register_with_autocomplete_and_kwargs(self):
        self.registry.register(Foo, Bar, search_name='search_name')
        self.assertEqual(self.registry['FooBar'].search_name,
            'search_name')

    def test_register_with_custom_name(self):
        self.registry.register(Foo, Bar, name='BarFoo')
        self.assertIn('BarFoo', self.registry.keys())
        self.assertEqual(self.registry['BarFoo'].__name__, 'BarFoo')

    def test_register_no_name_fail(self):
        try:
            self.registry.register(Noname)
            self.fail('Should raise an exception when registering noname')
        except:
            pass

    def test_register_no_name_pass(self):
        self.registry.register(Noname, search_fields=('number',))

    def test_register_generic_with_custom_name(self):
        self.registry.register(Generic, name='foo')
        self.assertTrue('foo' in self.registry.keys())

    def test_raise_AutocompleteNotRegistered(self):
        try:
            self.registry['NotRegistered']
            self.fail('Should raise AutocompleteNotRegistered')
        except autocomplete_light.AutocompleteNotRegistered:
            pass

    def test_raise_NoGenericAutocompleteRegistered(self):
        self.assertRaises(autocomplete_light.NoGenericAutocompleteRegistered,
                          self.registry.autocomplete_for_generic)

    def test_autocomplete_for_model(self):
        class FirstAutocomplete(autocomplete_light.AutocompleteModelBase):
            pass

        class SecondAutocomplete(autocomplete_light.AutocompleteModelBase):
            pass

        self.registry.register(Foo, FirstAutocomplete)
        self.registry.register(Foo, SecondAutocomplete)

        self.assertTrue(issubclass(
            self.registry.autocomplete_for_model(Foo), FirstAutocomplete))

    def test_autocomplete_for_generic(self):
        class FirstAutocomplete(Generic):
            pass

        class SecondAutocomplete(Generic):
            pass

        self.registry.register(FirstAutocomplete)
        self.registry.register(SecondAutocomplete)

        self.assertTrue(issubclass(
            self.registry.autocomplete_for_generic(), FirstAutocomplete))


class RegistryGetAutocompleteFromArgTestCase(unittest.TestCase):
    def setUp(self):
        self.registry = autocomplete_light.AutocompleteRegistry()
        self.registry.register(Foo)
        self.registry.register(Generic)

    def test_from_string(self):
        a = self.registry.get_autocomplete_from_arg('FooAutocomplete')
        self.assertEqual(a.model, Foo)

    def test_from_model(self):
        a = self.registry.get_autocomplete_from_arg(Foo)
        self.assertEqual(a.model, Foo)

    def test_from_model_instance(self):
        a = self.registry.get_autocomplete_from_arg(Foo())
        self.assertEqual(a.model, Foo)

    def test_from_autocomplete_instance(self):
        a = self.registry.get_autocomplete_from_arg(Generic)
        self.assertEqual(a, Generic)

    def test_default_generic(self):
        a = self.registry.get_autocomplete_from_arg()
        self.assertTrue(issubclass(a, Generic))
