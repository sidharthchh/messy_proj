from django.db import models
from django.contrib.auth.models import User
from sms_utils import send_sms


class KentUser(models.Model):
    WARRANTY_STATUS = (('warranty', 'warranty'),
                       ('warranty_expired', 'warranty_expired'),
                       ('amc 4500', 'amc 4500'),
                       ('amc 1000', 'amc 1000'),
                       ('amc 750', 'amc 750'))
    month = models.CharField(max_length=31, blank=True, null=True)
    purchase_date = models.DateField(null=True, blank=True)
    kro_number = models.CharField(max_length=31, null=True, blank=True)
    name = models.CharField(max_length=63)
    address = models.TextField(null=True, blank=True)
    landmark = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=511, null=True, blank=True)
    last_amc_date = models.DateField(null=True, blank=True)
    warranty_status = models.CharField(max_length=63, choices=WARRANTY_STATUS, null=True, blank=True)
    accessories = models.CharField(max_length=127, null=True, blank=True)
    remark = models.CharField(max_length=127, null=True, blank=True)
    area = models.CharField(max_length=1027, null=True, blank=True)
    sub_area = models.CharField(max_length=1027, null=True, blank=True)

    def __unicode__(self):
        return "{}-{}".format(self.name, self.phone)


class Employee(models.Model):
    name = models.CharField(max_length=63)
    phone = models.CharField(max_length=127)
    address = models.CharField(max_length=511)
    date_of_joining = models.DateField()

    def __unicode__(self):
        return "{}".format(self.name)


class Technician(models.Model):
    employee = models.ForeignKey(Employee, null=True)

    def __unicode__(self):
        return "{}".format(self.employee.name)


class ServiceTask(models.Model):
    customer = models.ForeignKey(KentUser)
    technician = models.ForeignKey(Technician, null=True, blank=True)
    date_and_time = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)
    technician_reached = models.DateTimeField(null=True, blank=True)
    technician_departed = models.DateTimeField(null=True, blank=True)

    def get_service_status(self):
        if not self.pk:
            # This is a new complaint
            message = "Your complaint for Kent has been registered. " \
                      "A technician will be attending you soon. Complaint Number:#"
        elif self.status:
            # The work has been done
            message = "Your Kent machine has been serviced. " \
                      "Please contact 9494949494 for further help. Complaint Number:#"

        return message

    def save(self, *args, **kwargs):
        # Need to send the customer a message that complaint has been
        # registered, serviced or cancelled.
        message = self.get_service_status()
        super(ServiceTask, self).save(*args, **kwargs)
        message = message + str(self.pk)
        send_sms(message, self.customer)

    def __unicode__(self):
        return "{} - {} - {}".format(self.customer, self.technician, self.date_and_time)


class EmployeeAttendance(models.Model):
    date = models.DateField()
    employees = models.ManyToManyField(Employee)

    def __unicode__(self):
        return "{}".format(self.date)


class Photo(models.Model):
    pic = models.FileField(upload_to='static/profile/')
    url = models.URLField(null=True, blank=True, max_length=2047)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return "{}".format(self.user.username)

    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)
        self.url = "/" + str(self.pic)
        super(Photo, self).save(*args, **kwargs)
