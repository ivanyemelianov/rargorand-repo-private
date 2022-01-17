from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import NftCollection, Nft

# Create your tests here.
User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('Ivan', password='abc123')

    def test_user_pw(self):
        checked = self.user_a.check_password("abc123")
        self.assertTrue(checked)

class NftCollectionTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('Ivan', password='abc123')

        self.nftcollection_a = NftCollection.objects.create(
            name='Beargorand',
            user = self.user_a
        )
        self.nftcollection_b = NftCollection.objects.create(
            name='Bullgorand',
            user = self.user_a
        )
        self.nft_a = Nft.objects.create(
            nftcollection=self.nftcollection_a,
            name='Chicken'
        )
        self.nft_b = Nft.objects.create(
            nftcollection=self.nftcollection_a,
            name='Bull'
        )

    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_user_nftcollection_reverse_count(self):
        user = self.user_a 
        qs = user.nftcollection_set.all() 
        self.assertEqual(qs.count(), 2)

    def test_user_nftcollection_forward_count(self):
        user = self.user_a 
        qs = NftCollection.objects.filter(user=user)
        self.assertEqual(qs.count(), 2)

    def test_nft_reverse_count(self):
        nftcollection = self.nftcollection_a 
        qs = nftcollection.nft_set.all() 
        self.assertEqual(qs.count(), 2)

    def test_nft_count(self):
        nftcollection = self.nftcollection_a 
        qs = Nft.objects.filter(nftcollection=nftcollection)
        self.assertEqual(qs.count(), 2)

    def test_user_two_level_relation(self):
        user = self.user_a
        qs = Nft.objects.filter(nftcollection__user=user)
        self.assertEqual(qs.count(), 2)
    
    def test_user_two_level_relation_reverse(self):
        user = self.user_a
        nft_ids = list(user.nftcollection_set.all().values_list('nft__id', flat=True))
        qs = Nft.objects.filter(id__in=nft_ids)
        self.assertEqual(qs.count(), 2)

    def test_user_two_level_relation_via_nftcollection(self):
        user = self.user_a
        ids = user.nftcollection_set.all().values_list("id", flat=True)
        qs = Nft.objects.filter(nftcollection__id__in=ids)
        self.assertEqual(qs.count(), 2)
    

