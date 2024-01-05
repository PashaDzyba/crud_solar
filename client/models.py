from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)

    # Add other client-related fields here

    def __str__(self):
        return self.name


class House(models.Model):
    client = models.ForeignKey(Client, related_name='houses', on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

    # Add other house-related fields here

    def __str__(self):
        return self.address


class UnityOfConsumption(models.Model):
    house = models.OneToOneField('House', on_delete=models.CASCADE, related_name='uc')
    energy_consumed = models.FloatField(default=0)
    energy_generated = models.FloatField(default=0)
    energy_credit = models.FloatField(default=0)  # Surplus energy credit
    energy_rate = models.FloatField(default=0.10)  # Rate per unit
    is_generator = models.BooleanField(default=False)
    is_beneficiary = models.BooleanField(default=False)
    energy_suppliers = models.ManyToManyField('self', symmetrical=False, related_name='energy_recipients', blank=True)

    def calculate_bill(self):
        # Calculate bill based on energy consumed and credit
        bill_amount = (self.energy_consumed * self.energy_rate) - self.energy_credit
        bill_amount = max(bill_amount, 0)  # Ensure bill is not negative
        return bill_amount

    def handle_surplus_energy(self):
        # Calculate surplus energy
        surplus_energy = self.energy_generated - self.energy_consumed
        if surplus_energy > 0 and self.is_generator:
            # Add surplus to energy credit if it is a generator
            self.energy_credit += surplus_energy * self.energy_rate
        elif surplus_energy < 0 and self.is_beneficiary:
            # If it is a beneficiary, it can use the credit (if available)
            self.energy_credit = max(self.energy_credit + surplus_energy * self.energy_rate, 0)

    def add_energy_supplier(self, supplier_uc):
        """ Adds another UC as an energy supplier. """
        if supplier_uc.is_generator and not supplier_uc == self:
            self.energy_suppliers.add(supplier_uc)

    def add_energy_recipient(self, recipient_uc):
        """ Adds another UC as an energy recipient. """
        if recipient_uc.is_beneficiary and not recipient_uc == self:
            self.energy_recipients.add(recipient_uc)

    def get_energy_supplier_addresses(self):
        """ Retrieve the addresses of all energy suppliers. """
        return [supplier.house.address for supplier in self.energy_suppliers.all()]

    def save(self, *args, **kwargs):
        # Call handle_surplus_energy before saving
        self.handle_surplus_energy()
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return f"UC for {self.house} | Generator: {self.is_generator} | Beneficiary: {self.is_beneficiary}"


class SolarEnergySystem(models.Model):
    uc = models.OneToOneField(UnityOfConsumption, on_delete=models.CASCADE, related_name='solar_system')
    production = models.FloatField()

    # Add other solar energy system-related fields here

    def save(self, *args, **kwargs):
        # Update the energy_generated in the related UnityOfConsumption
        self.uc.energy_generated = self.production
        self.uc.is_generator = True  # If it has a solar energy system, it's a generator
        self.uc.save()
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return f"Solar System for UC of {self.uc.house}"
