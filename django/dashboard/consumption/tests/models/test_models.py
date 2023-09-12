from django.test import TestCase
from consumption.models import User, Consumption, AggregateUserDailyConsumption
from datetime import datetime

class UserModelTestCase(TestCase):
  def setUp(self):
    self.user1 = User.objects.create(id=1, area="a1", tariff="t1")
    self.user2 = User.objects.create(id=2, area="a2", tariff="t2")

  def test_user_creation(self):
    self.assertEqual(self.user1.id, 1)
    self.assertEqual(self.user1.area, "a1")
    self.assertEqual(self.user1.tariff, "t1")
    self.assertTrue(self.user1.token)

  # トークンが一意であること
  def test_unique_token_generation(self):
    self.assertNotEqual(self.user1.token, self.user2.token)

class ConsumptionModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, area="a1", tariff="t1")

    def test_consumption_creation(self):
        datetime_str = "2023-09-12 00:00:00"
        consumption = Consumption.objects.create(
            datetime=datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S'),
            consumption=50.0,
            user=self.user
        )
        self.assertEqual(consumption.datetime.strftime('%Y-%m-%d %H:%M:%S'), datetime_str)
        self.assertEqual(consumption.consumption, 50.0)
        self.assertEqual(consumption.user, self.user)

class AggregateUserDailyConsumptionModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, area="a1", tariff="t1")

    def test_aggregate_user_daily_consumption_creation(self):
        date_str = "2023-09-12"
        aggregate = AggregateUserDailyConsumption.objects.create(
            user=self.user,
            date=datetime.strptime(date_str, '%Y-%m-%d'),
            total_consumption=100.0,
            average_consumption=25.0
        )
        self.assertEqual(aggregate.user, self.user)
        self.assertEqual(aggregate.date.strftime('%Y-%m-%d'), date_str)
        self.assertEqual(aggregate.total_consumption, 100.0)
        self.assertEqual(aggregate.average_consumption, 25.0)
