from django.test import TestCase
from utils.for_tests.base_for_authentication import (
    register_user,
    register_super_user
)
from utils.for_tests.base_for_create_itens import create_product
from django.urls import reverse, resolve
from django.utils.http import urlencode
from staff_management.forms import CrudProduct
from staff_management import views


class TestEditProductView(TestCase):
    def setUp(self):
        user = register_super_user()

        self.client.login(username='test', password='123')

        self.product = create_product(user)

        return super().setUp()

    def test_if_staff_edit_product_load_the_correct_view(self):
        response = resolve(reverse('staff:update_product', kwargs={'pk': '1'}))

        self.assertEqual(response.func.view_class, views.ProductUpdateView)

    def test_user_without_permission_redirects_from_staff_update_product(self):
        self.client.logout()
        register_user()

        self.client.login(username='Test', password='Test')

        response = self.client.get(
            reverse(
                'staff:update_product', kwargs={'pk': '1'}
            )
        )

        expected_url = reverse('authors:login') + '?' + urlencode(
            {'next': reverse(
                'staff:update_product', kwargs={'pk': '1'}
                )
             }
         )

        self.assertRedirects(response, expected_url)

    def test_user_with_permissions_can_update_product_in_staff(self):
        response = self.client.get(
            reverse(
                'staff:update_product', kwargs={'pk': '1'}
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_if_update_product_have_the_correct_template(self):
        response = self.client.get(
            reverse(
                'staff:update_product', kwargs={'pk': '1'}
            )
        )

        self.assertTemplateUsed(
            response,
            'staff_management/pages/crud_item.html'
        )

    def test_update_product_raises_404_if_not_found(self):
        response = self.client.post(
            reverse(
                'staff:update_product', kwargs={'pk': '2'}
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_staff_update_product_post_redirects_with_302(self):
        data = {
            'name': 'Test Product2',
            'price': '100',
            'description': 'Test2',
            'stock': '1',
            'is_published': True
        }

        response = self.client.post(
            reverse(
                'staff:update_product', kwargs={'pk': '1'}
            ), data=data
        )

        self.assertEqual(response.status_code, 302)

    def test_update_product_form_is_invalid_when_data_is_incomplete(self):
        data = {
            'name': 'a',
            'price': '-5',
            'description': '',
            'stock': '-1'
        }

        response = self.client.post(
            reverse(
                'staff:update_product', kwargs={'pk': '1'}
            ), data=data
        )

        form = CrudProduct(data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('price', form.errors)
        self.assertIn('Nome de produto muito pequeno,', form.errors['name'][0])
        self.assertIn('o valor do produto não pode ser menor ou igual a 0',
                      form.errors['price'][0]
                      )
        self.assertIn('o valor do stock não pode ser menor que 0',
                      form.errors['stock'][0]
                      )